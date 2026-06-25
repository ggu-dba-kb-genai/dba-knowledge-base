#!/usr/bin/env python3
import json, os

_HERE = os.path.dirname(os.path.abspath(__file__))
bundle_json = open(os.path.join(_HERE, 'bundle.json'), encoding='utf-8').read()

HEAD = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DBA Knowledge Map</title>
<script src="https://cdn.jsdelivr.net/npm/cytoscape@3.28.1/dist/cytoscape.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/marked@12.0.0/marked.min.js"></script>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<style>
:root {
  --bg:           #f5f4ed;
  --bg2:          #faf9f5;
  --bg3:          #e8e6dc;
  --border:       #f0eee6;
  --border-warm:  #e8e6dc;
  --accent:       #c96442;
  --accent2:      #d97757;
  --green:        #2a6b42;
  --yellow:       #9a6520;
  --text:         #141413;
  --muted:        #5e5d59;
  --text3:        #87867f;
  --text-light:   #b0aea5;
  --dark:         #141413;
  --dark2:        #30302e;
  --header-h:     58px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

body {
  font-family: system-ui, -apple-system, sans-serif;
  font-size: 14px;
  color: var(--text);
  background: var(--bg);
  display: flex; flex-direction: column;
  height: 100vh; overflow: hidden;
  line-height: 1.5;
}

/* ── Header ── */
header {
  height: var(--header-h);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 18px;
  background: var(--dark);
  flex-shrink: 0;
  gap: 14px;
  border-bottom: 2px solid var(--accent);
}
.title-block { display: flex; align-items: center; gap: 10px; flex-shrink: 0; }
.logo-icon {
  width: 32px; height: 32px;
  background: var(--accent); border-radius: 6px;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0;
}
.logo-icon svg { display: block; }
.title-block h1 {
  font-family: Georgia, serif; font-size: 16px; font-weight: 500;
  color: #fff; line-height: 1.1; letter-spacing: -0.2px;
}
.title-block .sub {
  font-size: 10px; color: var(--text3);
  letter-spacing: 0.5px; text-transform: uppercase;
}
.controls { display: flex; align-items: center; gap: 8px; flex-wrap: nowrap; }
.controls input[type="search"],
.controls select {
  font-size: 12px; padding: 5px 9px;
  border: 1px solid #3a3938; border-radius: 5px;
  background: #252522; color: var(--text-light);
  outline: none; transition: border-color 0.15s;
}
.controls input[type="search"] { width: 180px; }
.controls input[type="search"]:focus,
.controls select:focus { border-color: var(--accent); }
.controls select option { background: #252522; }
.btn {
  display: inline-flex; align-items: center; gap: 5px;
  font-family: inherit; font-size: 12px; font-weight: 500;
  padding: 5px 11px;
  border-radius: 5px; border: 1px solid #3a3938;
  background: #252522; color: var(--text-light);
  cursor: pointer; transition: all 0.15s; white-space: nowrap;
}
.btn:hover { background: #333330; border-color: var(--accent); color: #fff; }

/* ── Main layout ── */
main {
  display: flex; flex: 1; min-height: 0;
}

/* ── Graph area ── */
#graph-container {
  flex: 1 1 65%; min-width: 0;
  position: relative; background: var(--bg); overflow: hidden;
}
#graph-container::before {
  content: ""; position: absolute; inset: 0; pointer-events: none; z-index: 0;
  background-image:
    linear-gradient(rgba(201,100,66,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(201,100,66,0.05) 1px, transparent 1px);
  background-size: 36px 36px;
}
#graph { width: 100%; height: 100%; position: relative; z-index: 1; }

/* ── Resize handle ── */
#resize-handle {
  width: 5px; cursor: col-resize;
  background: var(--border-warm); flex-shrink: 0;
  transition: background 0.2s;
}
#resize-handle:hover, #resize-handle.active { background: var(--accent); }

/* ── Detail panel ── */
#detail {
  flex: 0 0 390px; display: flex; flex-direction: column;
  background: var(--bg2);
  border-left: 1px solid var(--border-warm);
  overflow: hidden; min-width: 260px; max-width: 65vw;
}
#detail.collapsed { flex-basis: 0; min-width: 0; border: none; }

/* Dashboard */
#dashboard {
  flex: 1; overflow-y: auto; padding: 24px 20px;
  display: flex; flex-direction: column; gap: 20px;
}
#dashboard h2 {
  font-family: Georgia, serif; font-size: 19px; font-weight: 500;
  color: var(--text); line-height: 1.3;
}
.dash-sub { font-size: 13px; color: var(--muted); line-height: 1.65; }
.stat-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 9px; }
.stat-card {
  background: var(--bg); border: 1px solid var(--border-warm);
  border-radius: 8px; padding: 12px 14px;
}
.stat-card .n {
  font-family: Georgia, serif; font-size: 26px; font-weight: 500;
  color: var(--accent); line-height: 1;
}
.stat-card .label {
  font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px;
  color: var(--muted); margin-top: 3px;
}
.section-head {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.6px;
  color: var(--muted); font-weight: 600; margin-bottom: 8px;
}
.legend-item {
  display: flex; align-items: center; gap: 10px;
  padding: 7px 9px; border-radius: 6px; margin-bottom: 4px;
  font-size: 13px; cursor: pointer; transition: background 0.15s;
}
.legend-item:hover { background: var(--bg3); }
.legend-dot { width: 13px; height: 13px; border-radius: 50%; flex-shrink: 0; }
.legend-dot.diamond { border-radius: 2px; transform: rotate(45deg); }
.legend-dot.square { border-radius: 2px; }
.legend-cnt { color: var(--muted); font-size: 11px; margin-left: auto; }
.hint-list { list-style: none; }
.hint-list li {
  font-size: 12px; color: var(--muted); padding: 5px 0;
  border-bottom: 1px solid var(--border);
  display: flex; gap: 8px; align-items: flex-start;
  line-height: 1.5;
}
.hint-list li:last-child { border-bottom: none; }
.key {
  background: var(--bg3); padding: 1px 6px; border-radius: 3px;
  font-size: 11px; color: var(--text); flex-shrink: 0; font-weight: 500;
}

/* ── Detail content ── */
#detail-content {
  display: none;  /* JS sets to flex when active */
  flex-direction: column;
  flex: 1; min-height: 0; overflow: hidden;
}
#detail-content.active { display: flex; }

.detail-head {
  padding: 16px 18px 0;
  border-bottom: 1px solid var(--border-warm);
  flex-shrink: 0; background: var(--bg2);
}
.detail-meta { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; flex-wrap: wrap; }
.type-chip {
  display: inline-block; padding: 2px 10px;
  border-radius: 20px; font-size: 10px; font-weight: 700;
  color: #fff; text-transform: uppercase; letter-spacing: 0.4px;
  flex-shrink: 0;
}
.node-id {
  font-family: monospace; font-size: 10px;
  color: var(--text3); background: var(--bg3);
  padding: 2px 6px; border-radius: 3px;
  word-break: break-all; max-width: 100%;
}
.detail-head h2 {
  font-family: Georgia, serif;
  font-size: 17px; font-weight: 500;
  color: var(--text); line-height: 1.3;
  margin-bottom: 12px; word-break: break-word;
}
.tab-nav { display: flex; }
.tab-btn {
  font-family: inherit; font-size: 12px; font-weight: 500;
  padding: 7px 14px; background: none; border: none;
  cursor: pointer; color: var(--muted);
  border-bottom: 2px solid transparent;
  transition: all 0.15s;
}
.tab-btn:hover { color: var(--text); }
.tab-btn.active { color: var(--accent); border-bottom-color: var(--accent); }

.tab-body {
  flex: 1; overflow-y: auto; min-height: 0;
}
.tab-pane { display: none; padding: 16px 18px; }
.tab-pane.active { display: block; }

.prop-row { margin-bottom: 18px; }
.prop-label {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.6px;
  color: var(--muted); font-weight: 600; margin-bottom: 5px;
}
.prop-value {
  font-size: 13px; color: var(--text); line-height: 1.65;
}
.prop-value a { color: var(--accent); text-decoration: none; }
.prop-value a:hover { text-decoration: underline; }
.tag-list { display: flex; flex-wrap: wrap; gap: 6px; }
.tag {
  display: inline-block; padding: 3px 9px;
  border-radius: 4px; background: rgba(201,100,66,0.08);
  border: 1px solid rgba(201,100,66,0.2);
  color: var(--accent); font-size: 11px; font-weight: 500;
}
.conn-section { margin-bottom: 18px; }
.conn-section-head {
  font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px;
  color: var(--muted); font-weight: 600; margin-bottom: 7px;
}
.conn-list { list-style: none; }
.conn-list li {
  display: flex; align-items: center; gap: 8px;
  padding: 7px 10px; border-radius: 6px;
  border: 1px solid var(--border-warm);
  background: var(--bg); margin-bottom: 5px;
  cursor: pointer; transition: all 0.15s;
}
.conn-list li:hover { border-color: var(--accent); background: rgba(201,100,66,0.04); }
.conn-name { flex: 1; min-width: 0; }
.conn-name span {
  display: block; font-size: 12px; font-weight: 500; color: var(--text);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.conn-badge {
  font-size: 9px; font-weight: 700; color: #fff;
  text-transform: uppercase; padding: 2px 7px;
  border-radius: 10px; flex-shrink: 0; letter-spacing: 0.3px;
}
.no-conns { font-size: 13px; color: var(--muted); padding: 8px 0; }

/* ── Rendered markdown body ── */
.meta-strip { margin-bottom: 16px; }
.meta-divider {
  height: 1px; background: var(--border-warm);
  margin: 4px 0 16px;
}
.md-body {
  font-size: 13.5px; line-height: 1.7; color: var(--text);
  word-wrap: break-word;
}
.md-body > *:first-child { margin-top: 0; }
.md-body h1, .md-body h2, .md-body h3, .md-body h4 {
  font-family: Georgia, serif; font-weight: 500;
  line-height: 1.3; margin: 22px 0 8px;
}
.md-body h1 { font-size: 19px; color: var(--text); }
.md-body h2 {
  font-size: 16px; color: var(--accent);
  padding-bottom: 5px; border-bottom: 1px solid var(--border-warm);
}
.md-body h3 { font-size: 14px; color: var(--muted); }
.md-body h4 { font-size: 13px; color: var(--yellow); font-weight: 600; }
.md-body p { margin: 10px 0; }
.md-body ul, .md-body ol { margin: 10px 0; padding-left: 22px; }
.md-body li { margin: 5px 0; }
.md-body a { color: var(--accent); text-decoration: none; }
.md-body a:hover { text-decoration: underline; }
.md-body a.internal {
  border-bottom: 1px dashed var(--accent);
  cursor: pointer;
}
.md-body strong { font-weight: 600; color: var(--text); }
.md-body em { font-style: italic; }
.md-body code {
  font-family: ui-monospace, "SF Mono", Menlo, monospace;
  font-size: 12px; background: var(--bg3);
  padding: 1px 5px; border-radius: 3px; color: var(--text);
}
.md-body pre {
  background: var(--bg3); border: 1px solid var(--border-warm);
  border-radius: 7px; padding: 12px 14px; overflow-x: auto;
  margin: 12px 0;
}
.md-body pre code { background: none; padding: 0; font-size: 12px; }
.md-body blockquote {
  margin: 12px 0; padding: 4px 14px;
  border-left: 3px solid var(--accent);
  color: var(--muted); background: rgba(201,100,66,0.05);
  border-radius: 0 6px 6px 0;
}
.md-body hr { border: none; border-top: 1px solid var(--border-warm); margin: 18px 0; }
.md-body img { max-width: 100%; height: auto; border-radius: 6px; }
.md-body table {
  border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 12.5px;
}
.md-body th, .md-body td {
  border: 1px solid var(--border-warm); padding: 6px 10px; text-align: left;
}
.md-body th { background: var(--bg3); font-weight: 600; }
.md-body .katex { font-size: 1.02em; }
.md-body .katex-display { margin: 12px 0; overflow-x: auto; overflow-y: hidden; }

/* ── Minimap ── */
#minimap {
  position: absolute; bottom: 12px; right: 12px; z-index: 10;
  background: var(--bg2); border: 1px solid var(--border-warm);
  border-radius: 7px; padding: 5px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.07);
  cursor: pointer;
}
#minimap canvas { display: block; border-radius: 3px; }
#mm-label {
  font-size: 9px; text-align: center; color: var(--text3);
  text-transform: uppercase; letter-spacing: 0.5px;
  padding: 2px 0 1px;
}

/* ── Graph toolbar ── */
.graph-toolbar {
  position: absolute; bottom: 12px; left: 12px; z-index: 10;
  display: flex; flex-direction: column; gap: 5px;
}
.tb-btn {
  width: 32px; height: 32px; border-radius: 7px;
  border: 1px solid var(--border-warm); background: var(--bg2);
  color: var(--muted); font-size: 16px; cursor: pointer;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 1px 5px rgba(0,0,0,0.06);
  transition: all 0.15s;
}
.tb-btn:hover { border-color: var(--accent); color: var(--accent); }

/* ── Course context bar ── */
#course-ctx {
  position: absolute; top: 10px; left: 50%; transform: translateX(-50%);
  z-index: 10; background: var(--bg2);
  border: 1px solid var(--border-warm); border-radius: 20px;
  padding: 5px 14px; font-size: 12px; color: var(--muted);
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
  display: none; align-items: center; gap: 8px; white-space: nowrap;
}
#course-ctx.on { display: flex; }
#course-ctx strong { color: var(--text); }
#course-ctx .back {
  color: var(--accent); cursor: pointer; font-weight: 500;
  background: none; border: none; font-size: 12px;
  font-family: inherit; padding: 0;
}
#course-ctx .back:hover { text-decoration: underline; }

/* ── Scrollbars ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-warm); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--text3); }
</style>
</head>
<body>
<header>
  <div class="title-block">
    <div class="logo-icon">
      <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5">
        <circle cx="12" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><circle cx="19" cy="19" r="2"/>
        <path d="M12 7v5l-5 5M12 12l5 5"/>
      </svg>
    </div>
    <div>
      <h1>DBA Knowledge Map</h1>
      <span class="sub">6 courses · 106 nodes · 1,044 connections</span>
    </div>
  </div>
  <div class="controls">
    <input type="search" id="search" placeholder="Search…">
    <select id="filter-type">
      <option value="">All types</option>
      <option value="Course">Courses</option>
      <option value="Concept">Concepts</option>
      <option value="Session">Sessions</option>
      <option value="Reference">References</option>
    </select>
    <button class="btn" id="btn-expand">↓ Expand all</button>
    <button class="btn" id="btn-collapse">↑ Overview</button>
    <button class="btn" id="btn-sidebar">⊟</button>
  </div>
</header>

<main>
  <section id="graph-container">
    <div id="graph"></div>
    <div id="course-ctx">
      <button class="back" id="btn-back">← All courses</button>
      <strong id="ctx-label"></strong>
      <span id="ctx-count"></span>
    </div>
    <div id="minimap">
      <div id="mm-label">Overview</div>
      <canvas id="mm-canvas" width="160" height="106"></canvas>
    </div>
    <div class="graph-toolbar">
      <button class="tb-btn" id="btn-zi" title="Zoom in">+</button>
      <button class="tb-btn" id="btn-zo" title="Zoom out">−</button>
      <button class="tb-btn" id="btn-fit" title="Fit">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"/>
        </svg>
      </button>
    </div>
  </section>

  <div id="resize-handle"></div>

  <section id="detail">
    <!-- Default: dashboard -->
    <div id="dashboard">
      <div>
        <h2>Knowledge Map</h2>
        <p class="dash-sub">Navigate your DBA curriculum. Click a course node to expand its sessions, or click any node to inspect details.</p>
      </div>
      <div>
        <div class="section-head">Summary</div>
        <div class="stat-grid">
          <div class="stat-card"><div class="n">6</div><div class="label">Courses</div></div>
          <div class="stat-card"><div class="n">73</div><div class="label">Sessions</div></div>
          <div class="stat-card"><div class="n">23</div><div class="label">Concepts</div></div>
          <div class="stat-card"><div class="n">1,044</div><div class="label">Connections</div></div>
        </div>
      </div>
      <div>
        <div class="section-head">Node types</div>
        <div class="legend-item" data-filter="Course">
          <span class="legend-dot" style="background:#c96442"></span>
          Course <span class="legend-cnt">6 · click to expand</span>
        </div>
        <div class="legend-item" data-filter="Session">
          <span class="legend-dot" style="background:#b8864e"></span>
          Session <span class="legend-cnt">73 · hidden in overview</span>
        </div>
        <div class="legend-item" data-filter="Concept">
          <span class="legend-dot diamond" style="background:#2a6b42"></span>
          Concept <span class="legend-cnt">23 · always visible</span>
        </div>
        <div class="legend-item" data-filter="Reference">
          <span class="legend-dot square" style="background:#87867f"></span>
          Reference <span class="legend-cnt">4</span>
        </div>
      </div>
      <div>
        <div class="section-head">How to explore</div>
        <ul class="hint-list">
          <li><span class="key">Click course</span> Expand / collapse sessions</li>
          <li><span class="key">Click node</span> See details in this panel</li>
          <li><span class="key">Scroll</span> Zoom the graph</li>
          <li><span class="key">Drag</span> Pan the graph or resize this panel</li>
          <li><span class="key">Search</span> Filter by name or tag</li>
        </ul>
      </div>
    </div>

    <!-- Node detail -->
    <div id="detail-content">
      <div class="detail-head">
        <div class="detail-meta">
          <span class="type-chip" id="d-chip"></span>
          <span class="node-id" id="d-id"></span>
        </div>
        <h2 id="d-title"></h2>
        <nav class="tab-nav">
          <button class="tab-btn active" data-tab="overview">Overview</button>
          <button class="tab-btn" data-tab="connections">Connections</button>
        </nav>
      </div>
      <div class="tab-body">
        <div id="tab-overview" class="tab-pane active"></div>
        <div id="tab-connections" class="tab-pane"></div>
      </div>
    </div>
  </section>
</main>

<script>
window.BUNDLE_NAME = "dba-knowledge";
window.BUNDLE = '''

MIDDLE = r''';

(function () {
"use strict";

// ── Palette ───────────────────────────────────────────────────
const TYPE_COLORS = {
  Course:    '#c96442',
  Session:   '#b8864e',
  Concept:   '#2a6b42',
  Reference: '#87867f',
};

const COURSE_COLORS = {
  'courses/c1-emerging-digital-technologies': '#c96442',
  'courses/c2-foundations-ml-ai':             '#2a6b42',
  'courses/c3-deep-learning':                 '#9a6520',
  'courses/c4-genai-pretrained-models':       '#6b3a1a',
  'courses/c5-ai-project-design':             '#4a7a3a',
  'courses/c6-responsible-ai':                '#7a4a2a',
};

// ── Helpers ───────────────────────────────────────────────────
function sessionParent(id) {
  if (!id || !id.startsWith('sessions/')) return null;
  const m = id.replace('sessions/', '').match(/^(.+)-session-\d+$/);
  return m ? 'courses/' + m[1] : null;
}

function nodeColor(d) {
  if (d.type === 'Session') return COURSE_COLORS[sessionParent(d.id)] || TYPE_COLORS.Session;
  return TYPE_COLORS[d.type] || '#87867f';
}

function esc(s) {
  return String(s || '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// ── Markdown body link/math helpers (ported from canonical viewer) ─
function toExternalUrl(uri) {
  if (!uri) return uri;
  const m = /^youtube:\/\/([A-Za-z0-9_-]+)/.exec(uri);
  if (m) return 'https://www.youtube.com/watch?v=' + m[1];
  return uri;
}

function resolveConceptHref(href, currentId) {
  if (!href || !href.endsWith('.md')) return null;
  let path = href.split('#')[0].split('?')[0].slice(0, -3);
  let parts;
  if (path.startsWith('/')) {
    parts = path.slice(1).split('/');
  } else {
    const dir = currentId.split('/').slice(0, -1);
    parts = dir.concat(path.split('/'));
  }
  const out = [];
  for (const seg of parts) {
    if (seg === '' || seg === '.') continue;
    if (seg === '..') { out.pop(); continue; }
    out.push(seg);
  }
  const target = out.join('/');
  return NI[target] ? target : null;
}

function rewriteInternalLinks(root, currentId) {
  root.querySelectorAll('a[href]').forEach(a => {
    const href = a.getAttribute('href');
    if (!href) return;
    const target = resolveConceptHref(href, currentId || '');
    if (target) {
      a.className = 'internal';
      a.dataset.target = target;
      a.setAttribute('href', 'javascript:void(0)');
      a.addEventListener('click', e => { e.preventDefault(); showDetail(target); });
      return;
    }
    if (href.startsWith('youtube://')) a.setAttribute('href', toExternalUrl(href));
    a.setAttribute('target', '_blank');
    a.setAttribute('rel', 'noopener');
  });
}

function linkifyCodeUrls(root) {
  root.querySelectorAll('code').forEach(code => {
    const txt = (code.textContent || '').trim();
    if (/^(https?:\/\/\S+|youtube:\/\/[A-Za-z0-9_-]+)$/.test(txt)) {
      const a = document.createElement('a');
      a.href = toExternalUrl(txt);
      a.textContent = txt;
      a.target = '_blank';
      a.rel = 'noopener';
      code.replaceWith(a);
    }
  });
}

function renderMath(el) {
  if (typeof renderMathInElement === 'undefined') return;
  try {
    renderMathInElement(el, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '$', right: '$', display: false },
        { left: '\\(', right: '\\)', display: false },
        { left: '\\[', right: '\\]', display: true },
      ],
      throwOnError: false,
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    });
  } catch (e) { /* noop */ }
}

// ── Build elements ────────────────────────────────────────────
const bundle = window.BUNDLE;
const elems = [];
for (const n of bundle.nodes) {
  elems.push({ data: { ...n.data, color: nodeColor(n.data) } });
}
for (const e of bundle.edges) {
  elems.push({ data: { ...e.data } });
}

// Node index for fast lookup
const NI = {};
for (const n of bundle.nodes) NI[n.data.id] = n.data;

// ── Cytoscape styles ──────────────────────────────────────────
const styles = [
  {
    selector: 'node',
    style: {
      label: 'data(label)',
      'text-wrap': 'wrap',
      'text-max-width': '88px',
      'font-family': 'system-ui, sans-serif',
      'font-size': '10px',
      color: '#141413',
      'text-valign': 'bottom',
      'text-halign': 'center',
      'text-margin-y': 4,
      'text-outline-width': 2,
      'text-outline-color': '#f5f4ed',
      'background-color': 'data(color)',
      'border-width': 2,
      'border-color': 'rgba(0,0,0,0.18)',
      width: 'mapData(size, 20, 120, 28, 68)',
      height: 'mapData(size, 20, 120, 28, 68)',
      shape: 'ellipse',
    }
  },
  {
    selector: 'node[type = "Course"]',
    style: {
      width: 88, height: 88,
      shape: 'round-rectangle',
      'font-size': '11px',
      'font-weight': 'bold',
      color: '#ffffff',
      'text-outline-width': 0,
      'text-valign': 'center',
      'text-halign': 'center',
      'text-margin-y': 0,
      'text-max-width': '80px',
      'border-width': 3,
      'border-color': 'rgba(0,0,0,0.22)',
      'z-index': 10,
    }
  },
  {
    selector: 'node[type = "Concept"]',
    style: {
      shape: 'diamond',
      color: '#141413',
      'text-outline-color': '#f5f4ed',
      'text-outline-width': 2,
      'text-valign': 'bottom',
      'font-size': '10px',
      'font-weight': '600',
    }
  },
  {
    selector: 'node[type = "Session"]',
    style: {
      width: 30, height: 30,
      shape: 'ellipse',
      'font-size': '8px',
      color: '#141413',
      'text-outline-color': '#f5f4ed',
      'text-outline-width': 1.5,
      'border-width': 1.5,
    }
  },
  {
    selector: 'node[type = "Reference"]',
    style: {
      shape: 'round-rectangle',
      width: 40, height: 40,
      color: '#141413',
      'text-outline-color': '#f5f4ed',
      'text-outline-width': 2,
      'text-valign': 'bottom',
      'font-size': '10px',
    }
  },
  {
    selector: 'edge',
    style: {
      width: 1,
      'line-color': '#cbc8bf',
      'target-arrow-color': '#cbc8bf',
      'target-arrow-shape': 'triangle',
      'curve-style': 'bezier',
      opacity: 0.5,
      'arrow-scale': 0.6,
    }
  },
  {
    selector: 'node:selected',
    style: {
      'border-color': '#c96442',
      'border-width': 4,
      'overlay-color': '#c96442',
      'overlay-opacity': 0.08,
      'overlay-padding': 6,
    }
  },
  {
    selector: '.faded',
    style: { opacity: 0.1 }
  },
  {
    selector: '.faded-e',
    style: { opacity: 0.05 }
  },
  {
    selector: '.srch-match',
    style: {
      'border-color': '#9a6520',
      'border-width': 3,
      'overlay-color': '#9a6520',
      'overlay-opacity': 0.1,
      'overlay-padding': 5,
    }
  },
  {
    selector: '.srch-dim',
    style: { opacity: 0.1 }
  },
];

// ── Init Cytoscape ────────────────────────────────────────────
const cy = cytoscape({
  container: document.getElementById('graph'),
  elements: elems,
  style: styles,
  layout: { name: 'preset' },
  minZoom: 0.04, maxZoom: 4,
  wheelSensitivity: 0.25,
});

// ── Session expansion ─────────────────────────────────────────
const expanded = new Set();

function sessionsOf(courseId) {
  return cy.nodes().filter(n =>
    n.data('type') === 'Session' && sessionParent(n.id()) === courseId
  );
}

// Initially hide all sessions
cy.nodes('[type = "Session"]').style('display', 'none');

function expandCourse(cid) {
  const course = cy.getElementById(cid);
  const sessions = sessionsOf(cid);
  if (!sessions.length) return;

  sessions.style('display', 'element');
  expanded.add(cid);

  // Radial position around course
  const pos = course.position();
  const n = sessions.length;
  const r = 130 + n * 7;
  sessions.forEach((s, i) => {
    const a = (2 * Math.PI * i / n) - Math.PI / 2;
    s.position({ x: pos.x + r * Math.cos(a), y: pos.y + r * Math.sin(a) });
  });

  updateCtxBar();
}

function collapseCourse(cid) {
  sessionsOf(cid).style('display', 'none');
  expanded.delete(cid);
  updateCtxBar();
}

function updateCtxBar() {
  const ctx = document.getElementById('course-ctx');
  if (expanded.size === 0) {
    ctx.classList.remove('on');
  } else if (expanded.size === 1) {
    const cid = [...expanded][0];
    const d = NI[cid];
    document.getElementById('ctx-label').textContent = d ? d.label : cid;
    const sc = sessionsOf(cid).length;
    document.getElementById('ctx-count').textContent = sc + ' sessions';
    ctx.classList.add('on');
  } else {
    document.getElementById('ctx-label').textContent = expanded.size + ' courses expanded';
    document.getElementById('ctx-count').textContent = '';
    ctx.classList.add('on');
  }
}

document.getElementById('btn-back').addEventListener('click', () => {
  for (const c of [...expanded]) collapseCourse(c);
  setTimeout(() => { cy.fit(cy.elements(':visible'), 50); drawMM(); }, 100);
});

cy.on('tap', 'node[type = "Course"]', evt => {
  const id = evt.target.id();
  if (expanded.has(id)) {
    collapseCourse(id);
    setTimeout(() => { cy.fit(cy.elements(':visible'), 60); drawMM(); }, 100);
  } else {
    expandCourse(id);
    setTimeout(() => drawMM(), 300);
  }
});

// ── Expand / Collapse all buttons ─────────────────────────────
document.getElementById('btn-expand').addEventListener('click', () => {
  cy.nodes('[type = "Course"]').forEach(c => {
    if (!expanded.has(c.id())) expandCourse(c.id());
  });
  setTimeout(() => { cy.fit(cy.elements(':visible'), 40); drawMM(); }, 150);
});

document.getElementById('btn-collapse').addEventListener('click', () => {
  for (const c of [...expanded]) collapseCourse(c);
  setTimeout(() => { cy.fit(cy.elements(':visible'), 50); drawMM(); }, 100);
});

// ── Initial layout (visible nodes only) ──────────────────────
setTimeout(() => {
  cy.nodes(':visible').layout({
    name: 'cose',
    animate: false, fit: true, padding: 60,
    nodeRepulsion: () => 14000, nodeOverlap: 24,
    idealEdgeLength: () => 85, edgeElasticity: () => 50,
    gravity: 0.7, numIter: 900, randomize: false,
  }).run();
  setTimeout(drawMM, 300);
}, 40);

// ── Detail panel ──────────────────────────────────────────────
let activeTab = 'overview';

function showDash() {
  document.getElementById('dashboard').style.display = 'flex';
  document.getElementById('detail-content').classList.remove('active');
  cy.elements().unselect();
}

function showDetail(nid) {
  const d = NI[nid];
  if (!d) return;

  document.getElementById('dashboard').style.display = 'none';
  document.getElementById('detail-content').classList.add('active');

  // Header
  const chip = document.getElementById('d-chip');
  chip.textContent = d.type;
  chip.style.background = nodeColor(d);
  document.getElementById('d-id').textContent = nid;
  document.getElementById('d-title').textContent = d.label || nid;

  // Tab content
  renderOverview(d, nid);
  renderConns(nid);
  setTab(activeTab);
}

function renderOverview(d, nid) {
  const pane = document.getElementById('tab-overview');

  // ── Compact meta strip (tags · resource · course) ──
  let meta = '';
  if (d.tags && d.tags.length) {
    const tags = d.tags.map(t => `<span class="tag">${esc(t)}</span>`).join('');
    meta += `<div class="prop-row">
  <div class="prop-label">Tags</div>
  <div class="prop-value tag-list">${tags}</div>
</div>`;
  }
  if (d.resource) {
    const url = d.resource.startsWith('youtube://') ?
      'https://www.youtube.com/watch?v=' + d.resource.replace('youtube://', '') :
      d.resource;
    meta += `<div class="prop-row">
  <div class="prop-label">Resource</div>
  <div class="prop-value"><a href="${esc(url)}" target="_blank" rel="noopener">${esc(url)}</a></div>
</div>`;
  }
  if (d.type === 'Session') {
    const pid = sessionParent(nid);
    const pd = pid ? NI[pid] : null;
    if (pd) {
      meta += `<div class="prop-row">
  <div class="prop-label">Course</div>
  <div class="prop-value">
    <span class="tag" style="cursor:pointer" onclick="showDetail('${esc(pid)}')">${esc(pd.label)}</span>
  </div>
</div>`;
    }
  }

  const bodyMd = (window.BUNDLE.bodies && window.BUNDLE.bodies[nid]) || '';
  const hasBody = bodyMd.trim().length > 0;

  pane.innerHTML =
    (meta ? `<div class="meta-strip">${meta}</div>` : '') +
    (hasBody && meta ? '<div class="meta-divider"></div>' : '') +
    '<div class="md-body" id="md-body"></div>';

  // ── Render full markdown body ──
  const bodyEl = document.getElementById('md-body');
  if (hasBody && typeof marked !== 'undefined') {
    try {
      bodyEl.innerHTML = marked.parse(bodyMd, { gfm: true, breaks: false });
    } catch (e) {
      bodyEl.textContent = bodyMd;
    }
    rewriteInternalLinks(bodyEl, nid);
    linkifyCodeUrls(bodyEl);
    renderMath(bodyEl);
  } else if (hasBody) {
    bodyEl.textContent = bodyMd;
  } else if (d.description) {
    bodyEl.innerHTML = `<p>${esc(d.description)}</p>`;
  } else {
    bodyEl.innerHTML = '<p style="color:var(--muted)">No detailed content for this node.</p>';
  }
}

function renderConns(nid) {
  const pane = document.getElementById('tab-connections');
  const node = cy.getElementById(nid);
  if (!node.length) { pane.innerHTML = '<p class="no-conns">No connections.</p>'; return; }

  const incoming = [], outgoing = [];
  node.connectedEdges().forEach(e => {
    const src = e.data('source'), tgt = e.data('target');
    if (src === nid) { const d = NI[tgt]; if (d) outgoing.push(d); }
    else { const d = NI[src]; if (d) incoming.push(d); }
  });

  function list(items) {
    if (!items.length) return '<p class="no-conns" style="font-size:12px">None</p>';
    return '<ul class="conn-list">' + items.map(d =>
      `<li onclick="showDetail('${esc(d.id)}')">
        <div class="conn-name"><span>${esc(d.label || d.id)}</span></div>
        <span class="conn-badge" style="background:${nodeColor(d)}">${d.type}</span>
      </li>`
    ).join('') + '</ul>';
  }

  let h = '';
  if (outgoing.length) h += `<div class="conn-section"><div class="conn-section-head">Links to (${outgoing.length})</div>${list(outgoing)}</div>`;
  if (incoming.length) h += `<div class="conn-section"><div class="conn-section-head">Linked from (${incoming.length})</div>${list(incoming)}</div>`;
  pane.innerHTML = h || '<p class="no-conns">No connections found.</p>';
}

// Expose for inline onclick
window.showDetail = showDetail;

// ── Tabs ──────────────────────────────────────────────────────
function setTab(name) {
  activeTab = name;
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.toggle('active', b.dataset.tab === name));
  document.querySelectorAll('.tab-pane').forEach(p => p.classList.toggle('active', p.id === 'tab-' + name));
}

document.querySelectorAll('.tab-btn').forEach(b => {
  b.addEventListener('click', () => setTab(b.dataset.tab));
});

// ── Node click ────────────────────────────────────────────────
cy.on('tap', 'node', evt => showDetail(evt.target.id()));
cy.on('tap', evt => { if (evt.target === cy) showDash(); });

// ── Hover ─────────────────────────────────────────────────────
cy.on('mouseover', 'node', evt => {
  const n = evt.target;
  n.neighborhood('node').addClass('faded');
  n.neighborhood('node').forEach(nb => nb.removeClass('faded'));
});
cy.on('mouseout', 'node', () => cy.nodes().removeClass('faded'));

// ── Search ────────────────────────────────────────────────────
let srchTimer;
document.getElementById('search').addEventListener('input', e => {
  clearTimeout(srchTimer);
  srchTimer = setTimeout(() => doSearch(e.target.value), 200);
});

function doSearch(q) {
  cy.elements().removeClass('srch-match srch-dim');
  q = q.trim().toLowerCase();
  if (!q) return;
  const matched = cy.nodes().filter(n => {
    const d = n.data();
    return (d.label || '').toLowerCase().includes(q) ||
           (d.description || '').toLowerCase().includes(q) ||
           (d.tags || []).some(t => t.toLowerCase().includes(q));
  });
  cy.nodes().not(matched).addClass('srch-dim');
  cy.edges().addClass('srch-dim');
  matched.addClass('srch-match');
}

// ── Type filter ───────────────────────────────────────────────
document.getElementById('filter-type').addEventListener('change', e => {
  const v = e.target.value;
  if (!v) {
    cy.nodes().style('display', '');
    cy.nodes('[type = "Session"]').style('display', 'none');
  } else {
    cy.nodes().forEach(n => n.style('display', n.data('type') === v ? 'element' : 'none'));
    cy.fit(cy.elements(':visible'), 50);
  }
  setTimeout(drawMM, 200);
});

// Legend filter clicks
document.querySelectorAll('.legend-item[data-filter]').forEach(el => {
  el.addEventListener('click', () => {
    document.getElementById('filter-type').value = el.dataset.filter;
    document.getElementById('filter-type').dispatchEvent(new Event('change'));
  });
});

// ── Toolbar ───────────────────────────────────────────────────
document.getElementById('btn-zi').addEventListener('click', () =>
  cy.zoom({ level: cy.zoom() * 1.3, renderedPosition: { x: cy.width() / 2, y: cy.height() / 2 } }));
document.getElementById('btn-zo').addEventListener('click', () =>
  cy.zoom({ level: cy.zoom() * 0.75, renderedPosition: { x: cy.width() / 2, y: cy.height() / 2 } }));
document.getElementById('btn-fit').addEventListener('click', () => cy.fit(cy.elements(':visible'), 50));
document.getElementById('btn-sidebar').addEventListener('click', () => {
  document.getElementById('detail').classList.toggle('collapsed');
  document.getElementById('resize-handle').style.display =
    document.getElementById('detail').classList.contains('collapsed') ? 'none' : '';
  setTimeout(() => cy.resize(), 350);
});

// ── Resize handle ─────────────────────────────────────────────
(function() {
  const handle = document.getElementById('resize-handle');
  const det = document.getElementById('detail');
  let drag = false;
  handle.addEventListener('mousedown', e => { drag = true; handle.classList.add('active'); document.body.style.cursor = 'col-resize'; e.preventDefault(); });
  document.addEventListener('mousemove', e => {
    if (!drag) return;
    const W = document.body.clientWidth;
    let w = Math.max(260, Math.min(Math.floor(W * 0.72), W - e.clientX));
    det.style.flexBasis = w + 'px';
    cy.resize();
  });
  document.addEventListener('mouseup', () => {
    if (drag) { drag = false; handle.classList.remove('active'); document.body.style.cursor = ''; cy.resize(); setTimeout(drawMM, 100); }
  });
})();

// ── Minimap ───────────────────────────────────────────────────
const mmCanvas = document.getElementById('mm-canvas');
const mmCtx = mmCanvas.getContext('2d');
const MM_W = mmCanvas.width, MM_H = mmCanvas.height;

function drawMM() {
  mmCtx.clearRect(0, 0, MM_W, MM_H);
  mmCtx.fillStyle = '#f5f4ed';
  mmCtx.fillRect(0, 0, MM_W, MM_H);

  const vis = cy.nodes(':visible');
  if (!vis.length) return;
  const bb = vis.boundingBox();
  if (!bb || bb.w < 1 || bb.h < 1) return;

  const pad = 8;
  const sc = Math.min((MM_W - pad * 2) / bb.w, (MM_H - pad * 2) / bb.h);
  const ox = pad + (MM_W - pad * 2 - bb.w * sc) / 2 - bb.x1 * sc;
  const oy = pad + (MM_H - pad * 2 - bb.h * sc) / 2 - bb.y1 * sc;

  // Edges
  mmCtx.lineWidth = 0.4;
  mmCtx.strokeStyle = 'rgba(94,93,89,0.2)';
  cy.edges(':visible').forEach(e => {
    const s = e.source().position(), t = e.target().position();
    mmCtx.beginPath();
    mmCtx.moveTo(s.x * sc + ox, s.y * sc + oy);
    mmCtx.lineTo(t.x * sc + ox, t.y * sc + oy);
    mmCtx.stroke();
  });

  // Nodes
  vis.forEach(n => {
    const p = n.position(), type = n.data('type');
    const r = type === 'Course' ? 5 : type === 'Concept' ? 3.5 : 2;
    mmCtx.beginPath();
    mmCtx.arc(p.x * sc + ox, p.y * sc + oy, r, 0, Math.PI * 2);
    mmCtx.fillStyle = nodeColor(n.data());
    mmCtx.fill();
  });

  // Viewport rectangle
  const ext = cy.extent();
  mmCtx.strokeStyle = '#c96442';
  mmCtx.lineWidth = 1.5;
  mmCtx.strokeRect(ext.x1 * sc + ox, ext.y1 * sc + oy, (ext.x2 - ext.x1) * sc, (ext.y2 - ext.y1) * sc);
}

// Throttled minimap update
let mmPending = false;
cy.on('render', () => {
  if (mmPending) return;
  mmPending = true;
  requestAnimationFrame(() => { drawMM(); mmPending = false; });
});

// Click minimap to pan
mmCanvas.addEventListener('click', e => {
  const rect = mmCanvas.getBoundingClientRect();
  const mx = e.clientX - rect.left, my = e.clientY - rect.top;
  const vis = cy.nodes(':visible');
  if (!vis.length) return;
  const bb = vis.boundingBox();
  const pad = 8;
  const sc = Math.min((MM_W - pad * 2) / bb.w, (MM_H - pad * 2) / bb.h);
  const ox = pad + (MM_W - pad * 2 - bb.w * sc) / 2 - bb.x1 * sc;
  const oy = pad + (MM_H - pad * 2 - bb.h * sc) / 2 - bb.y1 * sc;
  cy.animate({ pan: { x: cy.width() / 2 - ((mx - ox) / sc) * cy.zoom(), y: cy.height() / 2 - ((my - oy) / sc) * cy.zoom() }, duration: 300, easing: 'ease-out' });
});

})();
</script>
</body>
</html>'''

out = os.path.abspath(os.path.join(_HERE, '..', 'docs', 'map.html'))
with open(out, 'w', encoding='utf-8') as f:
    f.write(HEAD)
    f.write(bundle_json)
    f.write(MIDDLE)

import os
sz = os.path.getsize(out)
print(f"Written: {out}")
print(f"Size: {sz:,} bytes ({sz/1024/1024:.2f} MB)")
