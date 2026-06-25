/*
 * kb-tools.js — the durable "spine" for the DBA Knowledge Base.
 *
 * Eight read-only tools over the OKF graph (bundle.json / window.BUNDLE).
 * Framework-agnostic, zero dependencies, pure functions. Drive them with:
 *   - a local in-browser LLM (WebAIAgent / Chrome built-in AI),
 *   - a cloud LLM via function calling (Gemini / OpenAI),
 *   - or plain UI.
 * Write the tools ONCE; expose them many ways.
 *
 * Usage:
 *   await KB.load();                 // loads window.BUNDLE or fetches kb-data.json
 *   KB.tools.search_knowledge_base({ query: "DARWIN framework" });
 *   KB.TOOL_SCHEMAS                  // JSON-schema function declarations for an LLM
 */
(function (global) {
  "use strict";

  const KB = {
    data: null,            // { nodes, edges, bodies, types, palette }
    _nodes: new Map(),     // id -> nodeData
    _adj: new Map(),       // id -> Set(neighbourId)   (undirected)
    _index: [],            // [{ id, hay }] lowercased searchable text
  };

  // ---- loading ---------------------------------------------------------------
  KB.load = async function (url = "kb-data.json") {
    if (KB.data) return KB.data;
    let bundle = global.BUNDLE && global.BUNDLE.nodes ? global.BUNDLE : null;
    if (!bundle) {
      const res = await fetch(url);
      if (!res.ok) throw new Error("Could not load KB data: " + res.status);
      bundle = await res.json();
    }
    KB.data = bundle;
    _buildIndexes();
    return bundle;
  };

  function _buildIndexes() {
    const { nodes, edges, bodies } = KB.data;
    KB._nodes.clear(); KB._adj.clear(); KB._index = [];
    for (const n of nodes) {
      const d = n.data;
      KB._nodes.set(d.id, d);
      KB._adj.set(d.id, new Set());
      const body = (bodies && bodies[d.id]) || "";
      const tags = Array.isArray(d.tags) ? d.tags.join(" ") : (d.tags || "");
      KB._index.push({
        id: d.id,
        hay: (d.label + " " + (d.description || "") + " " + tags + " " + body).toLowerCase(),
      });
    }
    for (const e of edges) {
      const { source, target } = e.data;
      if (KB._adj.has(source)) KB._adj.get(source).add(target);
      if (KB._adj.has(target)) KB._adj.get(target).add(source);
    }
  }

  // ---- helpers ---------------------------------------------------------------
  function node(id) { return KB._nodes.get(id) || null; }

  function nodeUrl(id) { return "map.html#" + encodeURIComponent(id); }

  function brief(id) {
    const d = node(id);
    if (!d) return null;
    return { id, label: d.label, type: d.type, url: nodeUrl(id) };
  }

  // Resolve a free-text query (label, partial label, or exact id) to a node id.
  function resolveId(q) {
    if (!q) return null;
    if (KB._nodes.has(q)) return q;
    const ql = q.toLowerCase().trim();
    let best = null, bestScore = -1;
    for (const [id, d] of KB._nodes) {
      const label = d.label.toLowerCase();
      let s = -1;
      if (label === ql || id.toLowerCase() === ql) s = 100;
      else if (label.startsWith(ql)) s = 80;
      else if (label.includes(ql)) s = 60;
      else if (id.toLowerCase().includes(ql)) s = 40;
      if (s > bestScore) { bestScore = s; best = id; }
    }
    if (best && bestScore >= 40) return best;
    const hits = _search(q, 1);
    return hits.length ? hits[0].id : null;
  }

  function _tokens(s) {
    return (s.toLowerCase().match(/[a-z0-9]+/g) || []).filter((t) => t.length > 1);
  }

  // Weighted keyword relevance over label/description/tags/body.
  function _search(query, limit = 8, typeFilter = null) {
    const toks = _tokens(query);
    if (!toks.length) return [];
    const out = [];
    for (const entry of KB._index) {
      const d = node(entry.id);
      if (typeFilter && d.type !== typeFilter) continue;
      const label = d.label.toLowerCase();
      const desc = (d.description || "").toLowerCase();
      let score = 0;
      for (const t of toks) {
        if (label.includes(t)) score += 8;
        if (desc.includes(t)) score += 3;
        const m = entry.hay.split(t).length - 1;
        if (m) score += Math.min(6, m); // body/tag frequency, capped
      }
      if (score > 0) out.push({ id: entry.id, score });
    }
    out.sort((a, b) => b.score - a.score);
    return out.slice(0, limit);
  }

  function snippet(id, query, len = 220) {
    const body = (KB.data.bodies && KB.data.bodies[id]) || node(id).description || "";
    const toks = _tokens(query);
    const lc = body.toLowerCase();
    let pos = -1;
    for (const t of toks) { const p = lc.indexOf(t); if (p >= 0) { pos = p; break; } }
    let start = pos < 0 ? 0 : Math.max(0, pos - 60);
    let s = body.slice(start, start + len).replace(/\s+/g, " ").trim();
    if (start > 0) s = "…" + s;
    if (start + len < body.length) s += "…";
    return s;
  }

  // Extract a named markdown section (e.g. "Rubric", "Citations") from a body.
  function section(body, names) {
    const lines = body.split("\n");
    const re = new RegExp("^#{1,4}\\s+.*(" + names.join("|") + ")", "i");
    let start = -1;
    for (let i = 0; i < lines.length; i++) { if (re.test(lines[i])) { start = i; break; } }
    if (start < 0) return null;
    const level = (lines[start].match(/^#+/) || ["#"])[0].length;
    let end = lines.length;
    for (let i = start + 1; i < lines.length; i++) {
      const h = lines[i].match(/^#+/);
      if (h && h[0].length <= level) { end = i; break; }
    }
    return lines.slice(start, end).join("\n").trim();
  }

  // ---- the eight tools -------------------------------------------------------
  const tools = {
    /* 1 */ search_knowledge_base({ query, type = null, limit = 8 }) {
      const hits = _search(query, limit, type);
      return {
        query,
        results: hits.map((h) => {
          const d = node(h.id);
          return { id: h.id, label: d.label, type: d.type, snippet: snippet(h.id, query), url: nodeUrl(h.id) };
        }),
      };
    },

    /* 2 */ get_node({ id }) {
      const rid = resolveId(id);
      const d = rid && node(rid);
      if (!d) return { error: "No node matching '" + id + "'." };
      return {
        id: rid, label: d.label, type: d.type, description: d.description,
        tags: d.tags, resource: d.resource || null, url: nodeUrl(rid),
        body: (KB.data.bodies && KB.data.bodies[rid]) || "",
      };
    },

    /* 3 */ get_related({ id }) {
      const rid = resolveId(id);
      if (!rid || !KB._adj.has(rid)) return { error: "No node matching '" + id + "'." };
      const groups = {};
      for (const nb of KB._adj.get(rid)) {
        const d = node(nb); if (!d) continue;
        (groups[d.type] = groups[d.type] || []).push(brief(nb));
      }
      return { id: rid, label: node(rid).label, related: groups };
    },

    /* 4 */ get_course_outline({ course }) {
      let rid = resolveId(course);
      if (rid && node(rid).type !== "Course") {
        // climb to a connected Course if the user named a session/concept
        for (const nb of KB._adj.get(rid) || []) if (node(nb) && node(nb).type === "Course") { rid = nb; break; }
      }
      if (!rid || node(rid).type !== "Course") return { error: "No course matching '" + course + "'." };
      const sessions = [], assignments = [];
      for (const nb of KB._adj.get(rid)) {
        const d = node(nb);
        if (d.type === "Session") sessions.push(brief(nb));
        else if (d.type === "Assignment") assignments.push(brief(nb));
      }
      const num = (b) => { const m = b.id.match(/session-(\d+)/); return m ? +m[1] : 999; };
      sessions.sort((a, b) => num(a) - num(b));
      return { course: node(rid).label, id: rid, url: nodeUrl(rid), sessions, assignments };
    },

    /* 5 */ find_concept({ topic, limit = 5 }) {
      const hits = _search(topic, 12, "Concept").slice(0, limit);
      return {
        topic,
        concepts: hits.map((h) => {
          const taught = [];
          for (const nb of KB._adj.get(h.id) || []) if (node(nb) && node(nb).type === "Session") taught.push(brief(nb));
          return { id: h.id, label: node(h.id).label, snippet: snippet(h.id, topic), taught_in: taught, url: nodeUrl(h.id) };
        }),
      };
    },

    /* 6 */ get_assignment_rubric({ id }) {
      const rid = resolveId(id);
      const d = rid && node(rid);
      if (!d) return { error: "No assignment matching '" + id + "'." };
      const body = (KB.data.bodies && KB.data.bodies[rid]) || "";
      const rubric = section(body, ["Rubric", "Evaluation", "Grading", "Assessment"]);
      return { id: rid, label: d.label, type: d.type, rubric: rubric || "(No explicit rubric section found.)", url: nodeUrl(rid) };
    },

    /* 7 */ explain_path({ from, to }) {
      const a = resolveId(from), b = resolveId(to);
      if (!a || !b) return { error: "Could not resolve both endpoints." };
      if (a === b) return { path: [brief(a)] };
      const prev = new Map([[a, null]]); const q = [a];
      while (q.length) {
        const cur = q.shift();
        if (cur === b) break;
        for (const nb of KB._adj.get(cur) || []) if (!prev.has(nb)) { prev.set(nb, cur); q.push(nb); }
      }
      if (!prev.has(b)) return { from: node(a).label, to: node(b).label, path: null, note: "No connecting path." };
      const path = []; for (let c = b; c != null; c = prev.get(c)) path.unshift(brief(c));
      return { from: node(a).label, to: node(b).label, hops: path.length - 1, path };
    },

    /* 8 */ cite({ id }) {
      const rid = resolveId(id);
      const d = rid && node(rid);
      if (!d) return { error: "No node matching '" + id + "'." };
      const body = (KB.data.bodies && KB.data.bodies[rid]) || "";
      const cites = section(body, ["Citations", "References", "Sources"]);
      return { id: rid, label: d.label, type: d.type, url: nodeUrl(rid), citation: cites || (d.label + " — DBA Knowledge Base.") };
    },
  };

  // ---- function-calling schemas (for an LLM) ---------------------------------
  const S = (props, req) => ({ type: "object", properties: props, required: req || [] });
  const str = (description) => ({ type: "string", description });
  const TOOL_SCHEMAS = [
    { name: "search_knowledge_base", description: "Search the DBA knowledge base (courses, sessions, concepts, references, assignments) by keyword/topic. Use this first for any open question.", parameters: S({ query: str("What to search for"), type: { type: "string", enum: ["Course", "Session", "Concept", "Reference", "Assignment"], description: "Optional node-type filter" } }, ["query"]) },
    { name: "get_node", description: "Get the full content (markdown body, tags, description) of one node by its label or id.", parameters: S({ id: str("Node label or id") }, ["id"]) },
    { name: "get_related", description: "List the graph neighbours of a node — what connects to it — grouped by type.", parameters: S({ id: str("Node label or id") }, ["id"]) },
    { name: "get_course_outline", description: "List the ordered sessions and assignments for a course.", parameters: S({ course: str("Course label or id") }, ["course"]) },
    { name: "find_concept", description: "Find concept nodes matching a topic and the sessions that teach each one.", parameters: S({ topic: str("Concept/topic to find") }, ["topic"]) },
    { name: "get_assignment_rubric", description: "Return the complete grading rubric for an assignment.", parameters: S({ id: str("Assignment label or id") }, ["id"]) },
    { name: "explain_path", description: "Find the shortest connecting path between two nodes/concepts across the graph.", parameters: S({ from: str("Start node"), to: str("End node") }, ["from", "to"]) },
    { name: "cite", description: "Return citation/provenance for a node.", parameters: S({ id: str("Node label or id") }, ["id"]) },
  ];

  // Dispatch a tool call by name (used by the LLM function-calling loop).
  KB.call = function (name, args) {
    if (!tools[name]) return { error: "Unknown tool: " + name };
    try { return tools[name](args || {}); } catch (e) { return { error: String(e) }; }
  };

  KB.tools = tools;
  KB.TOOL_SCHEMAS = TOOL_SCHEMAS;
  KB.resolveId = resolveId;
  KB.nodeUrl = nodeUrl;
  KB.stats = () => ({ nodes: KB._nodes.size, edges: KB.data ? KB.data.edges.length : 0, types: KB.data ? KB.data.types : [] });

  global.KB = KB;
})(typeof window !== "undefined" ? window : this);
