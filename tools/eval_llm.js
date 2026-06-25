/*
 * eval_llm.js — grades the LLM ANSWER layer (summarization + grounding + refusal).
 * Needs a Gemini key (the tool layer is graded separately by eval_kb.js).
 *
 *   GEMINI_KEY=AIza...  node tools/eval_llm.js
 *   GEMINI_KEY=...  MODEL=gemini-2.5-flash  node tools/eval_llm.js
 *
 * Replicates ask.html's function-calling loop in Node and checks each answer
 * against expected grounded facts. Heuristic (substring) grading — enough to
 * catch "it just searched / it hallucinated / it didn't summarize".
 */
const fs = require("fs");
const path = require("path");

const KEY = process.env.GEMINI_KEY || process.env.GOOGLE_API_KEY;
const MODEL = process.env.MODEL || "gemini-2.5-flash";
if (!KEY) { console.error("Set GEMINI_KEY=... (get one free at aistudio.google.com)"); process.exit(2); }

globalThis.window = globalThis;
globalThis.BUNDLE = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "docs", "kb-data.json"), "utf8"));
require(path.join(__dirname, "..", "docs", "kb-tools.js"));

const SYSTEM = `You are a tutor for an open DBA knowledge base on Emerging Technologies, Generative AI & AI. Answer ONLY from the knowledge base using the provided tools. Always call a tool before answering — start with search_knowledge_base. Ground every claim in retrieved content and name the source nodes. If the KB doesn't cover something, say so plainly rather than inventing. Be concise and structured.`;

async function askGemini(q) {
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${encodeURIComponent(KEY)}`;
  const contents = [{ role: "user", parts: [{ text: q }] }];
  const toolsUsed = [];
  for (let step = 0; step < 6; step++) {
    const body = { system_instruction: { parts: [{ text: SYSTEM }] }, contents, tools: [{ function_declarations: KB.TOOL_SCHEMAS }] };
    const res = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    if (!res.ok) throw new Error("Gemini " + res.status + ": " + (await res.text()).slice(0, 200));
    const data = await res.json();
    const parts = ((data.candidates || [])[0] || {}).content?.parts || [];
    const calls = parts.filter((p) => p.functionCall);
    if (calls.length) {
      contents.push({ role: "model", parts });
      const responses = calls.map((c) => {
        toolsUsed.push(c.functionCall.name);
        return { functionResponse: { name: c.functionCall.name, response: { result: KB.call(c.functionCall.name, c.functionCall.args || {}) } } };
      });
      contents.push({ role: "user", parts: responses });
      continue;
    }
    return { text: parts.map((p) => p.text || "").join(""), toolsUsed };
  }
  return { text: "(max steps)", toolsUsed };
}

// case: { q, all?: [...], any?: [...], none?: [...], tool?: name }
const CASES = [
  { name: "summarize DARWIN (real synthesis)", q: "Summarize the DARWIN framework in a few sentences.",
    any: ["data", "algorithm", "infrastructure", "responsibility", "workflow"], minAny: 3 },
  { name: "rubric retrieval + answer", q: "What is the grading rubric for the C6 Responsible AI assignment?",
    any: ["rubric", "%", "points", "criteria", "evaluation", "weight"], tool: "get_assignment_rubric" },
  { name: "RLHF locating", q: "Which session covers RLHF and reasoning models?",
    any: ["session 02", "rlhf", "reasoning"] },
  { name: "concept relationship", q: "How does prompt engineering relate to agentic AI in this KB?",
    all: ["prompt", "agent"] },
  { name: "REFUSAL on absent topic", q: "What does the knowledge base say about baking sourdough bread?",
    any: ["not", "doesn't", "does not", "no information", "isn't covered", "not covered", "outside"], none: ["preheat", "yeast starter", "knead the dough"] },
];

const lc = (s) => (s || "").toLowerCase();
const countAny = (t, arr) => arr.filter((x) => lc(t).includes(lc(x))).length;

(async () => {
  await KB.load();
  console.log(`Model: ${MODEL}\n`);
  let pass = 0, fail = 0;
  for (const c of CASES) {
    let ok = true, why = [];
    try {
      const { text, toolsUsed } = await askGemini(c.q);
      if (c.all) { for (const w of c.all) if (!lc(text).includes(lc(w))) { ok = false; why.push("missing:" + w); } }
      if (c.any) { const n = countAny(text, c.any); const need = c.minAny || 1; if (n < need) { ok = false; why.push(`any<${need} (got ${n})`); } }
      if (c.none) { for (const w of c.none) if (lc(text).includes(lc(w))) { ok = false; why.push("hallucinated:" + w); } }
      if (c.tool && !toolsUsed.includes(c.tool)) { ok = false; why.push("did not call " + c.tool); }
      console.log(`${ok ? "  PASS" : "✗ FAIL"}  ${c.name}`);
      console.log(`        tools: [${[...new Set(toolsUsed)].join(", ")}]`);
      console.log(`        answer: ${text.replace(/\s+/g, " ").slice(0, 160)}…`);
      if (!ok) console.log(`        why: ${why.join("; ")}`);
    } catch (e) { ok = false; console.log(`✗ FAIL  ${c.name} — ${e.message}`); }
    ok ? pass++ : fail++;
    console.log("");
  }
  console.log(`${fail === 0 ? "ALL PASS" : fail + " FAILED"}  (${pass}/${pass + fail})`);
  process.exit(fail ? 1 : 0);
})();
