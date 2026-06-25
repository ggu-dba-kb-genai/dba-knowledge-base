/*
 * eval_kb.js — deterministic eval for the KB tool layer (no LLM needed).
 * Run:  node tools/eval_kb.js
 * Checks that each tool returns correct, grounded data for known queries.
 * The LLM phrasing varies; these tool results do NOT — so this is the
 * reliable regression gate. LLM-answer grading lives in eval_llm.js (needs a key).
 */
const fs = require("fs");
const path = require("path");

globalThis.window = globalThis;
globalThis.BUNDLE = JSON.parse(fs.readFileSync(path.join(__dirname, "..", "docs", "kb-data.json"), "utf8"));
require(path.join(__dirname, "..", "docs", "kb-tools.js"));

let pass = 0, fail = 0;
const log = (ok, name, detail) => {
  console.log(`${ok ? "  PASS" : "✗ FAIL"}  ${name}${detail ? "  — " + detail : ""}`);
  ok ? pass++ : fail++;
};
const has = (s, sub) => (s || "").toLowerCase().includes(sub.toLowerCase());

(async () => {
  await KB.load();
  console.log("KB:", JSON.stringify(KB.stats()), "\n");

  // 1 — search surfaces the right node type/topic
  {
    const r = KB.tools.search_knowledge_base({ query: "RLHF reasoning models reinforcement learning", limit: 5 });
    const top3 = r.results.slice(0, 3).map((h) => h.label).join(" | ");
    log(r.results.some((h) => has(h.label, "RLHF")), "search RLHF", top3.slice(0, 70));
  }

  // 2 — course outline: ordered sessions + assignment present
  {
    const r = KB.tools.get_course_outline({ course: "Responsible AI" });
    const ordered = r.sessions.length >= 3 && has(r.sessions[0].label, "Session 01");
    log(ordered && r.assignments.length >= 1, "course outline ordered", `${r.sessions.length} sessions, ${r.assignments.length} assignments, first=${r.sessions[0] && r.sessions[0].label.slice(0,18)}`);
  }

  // 3 — rubric extraction returns real content (not the placeholder)
  {
    const r = KB.tools.get_assignment_rubric({ id: "C6 Assignment 1" });
    const real = r.rubric && r.rubric.length > 60 && !has(r.rubric, "No explicit rubric");
    log(real, "rubric extraction", `${(r.rubric||"").length} chars`);
  }

  // 4 — graph path between two concepts
  {
    const r = KB.tools.explain_path({ from: "prompt engineering", to: "agentic ai" });
    log(r.path && r.path.length >= 2 && r.hops <= 3, "explain_path", r.path ? r.path.map((p)=>p.label.split(" ")[0]).join("->") + " (" + r.hops + " hops)" : "no path");
  }

  // 5 — find_concept returns concept nodes + where taught
  {
    const r = KB.tools.find_concept({ topic: "agentic autonomous agents" });
    const c = r.concepts[0];
    log(c && has(c.label, "Agentic") && c.taught_in.length > 0, "find_concept", c ? `${c.label.slice(0,28)} taught in ${c.taught_in.length}` : "none");
  }

  // 6 — fuzzy get_node resolves a vague phrase to the right node + full body
  {
    const r = KB.tools.get_node({ id: "session 03 algorithm ideation" });
    log(!r.error && has(r.label, "Session 03") && r.body.length > 2000, "fuzzy get_node", r.error || `${r.label.slice(0,30)} | ${r.body.length} chars`);
  }

  // 7 — citation provenance
  {
    const o = KB.tools.get_course_outline({ course: "Responsible AI" });
    const r = KB.tools.cite({ id: o.sessions[1] ? o.sessions[1].id : "c6" });
    log(r.citation && r.citation.length > 10, "cite provenance", (r.citation||"").replace(/\n/g," ").slice(0, 50));
  }

  // 8 — NEGATIVE: off-topic query should NOT surface a strong on-topic match
  //     (this is the case the LLM must REFUSE on; here we just confirm retrieval is weak)
  {
    const r = KB.tools.search_knowledge_base({ query: "sourdough bread baking fermentation recipe", limit: 3 });
    const weak = r.results.length === 0 || r.results.every((h) => !has(h.label, "bread") && !has(h.label, "sourdough") && !has(h.label, "baking"));
    log(weak, "negative / off-topic retrieval weak", `${r.results.length} hits, top=${r.results[0] ? r.results[0].label.slice(0,30) : "none"}`);
  }

  console.log(`\n${fail === 0 ? "ALL PASS" : fail + " FAILED"}  (${pass}/${pass + fail})`);
  process.exit(fail ? 1 : 0);
})();
