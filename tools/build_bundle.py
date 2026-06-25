#!/usr/bin/env python3
"""Build tools/bundle.json from the OKF markdown bundle.

Vendored, dependency-light re-implementation of the OKF viewer graph builder
(okf/src/enrichment_agent/viewer/generator.py: _walk_concepts / _build_graph /
_extract_links). Keeps this repo reproducible from a clean clone without the
upstream okf package.

  bundle/*.md  ->  build_bundle.py  ->  tools/bundle.json {nodes,edges,bodies,types,palette}
  tools/bundle.json  ->  gen_viz_v2.py  ->  docs/map.html

Usage:
  python3 tools/build_bundle.py            # write tools/bundle.json
  python3 tools/build_bundle.py --check    # parity check vs existing, no write
"""
import json
import os
import re
import sys

import yaml  # PyYAML

_HERE = os.path.dirname(os.path.abspath(__file__))
_BUNDLE_ROOT = os.path.abspath(os.path.join(_HERE, "..", "bundle"))
_OUT = os.path.join(_HERE, "bundle.json")

_INDEX_NAME = "index.md"
_LINK_RE = re.compile(r"\]\(([^)\s]+\.md)(?:#[A-Za-z0-9_\-]*)?\)")
_FM_DELIM = "---"

# Mirrors generator.py _TYPE_PALETTE (+ Assignment). Node fill colors here are
# NOT what the published map uses — gen_viz_v2.py overrides via its own warm
# TYPE_COLORS — but kept for parity with the upstream bundle schema.
_TYPE_PALETTE = {
    "BigQuery Dataset": "#8b5cf6",
    "BigQuery Table": "#3b82f6",
    "Reference": "#10b981",
    "Course": "#6366f1",
    "Session": "#06b6d4",
    "Concept": "#f43f5e",
    "Assignment": "#f59e0b",
}
_DEFAULT_NODE_COLOR = "#64748b"


def _parse_doc(text):
    """Return (frontmatter dict, body str). Mirrors OKFDocument.parse."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != _FM_DELIM:
        return {}, text
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == _FM_DELIM:
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("Unterminated YAML frontmatter block")
    fm = yaml.safe_load("\n".join(lines[1:end_idx])) or {}
    if not isinstance(fm, dict):
        raise ValueError("Frontmatter must be a YAML mapping")
    body = "\n".join(lines[end_idx + 1:])
    if body.startswith("\n"):
        body = body[1:]
    return fm, body


def _iter_md(root):
    for dirpath, _dirs, files in os.walk(root):
        for name in sorted(files):
            if name.endswith(".md") and name != _INDEX_NAME:
                yield os.path.join(dirpath, name)


def _rel_id(path, root):
    rel = os.path.relpath(path, root)
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel.replace(os.sep, "/")


def _extract_links(body, doc_dir, root):
    out, seen = [], set()
    root_abs = os.path.abspath(root)
    for m in _LINK_RE.finditer(body):
        target = m.group(1)
        if "://" in target or target.startswith("/"):
            continue
        resolved = os.path.abspath(os.path.join(doc_dir, target))
        rel = os.path.relpath(resolved, root_abs)
        if rel.startswith(".."):
            continue
        rel = rel.replace(os.sep, "/")
        if rel.endswith(".md"):
            rel = rel[:-3]
        if rel and rel not in seen:
            seen.add(rel)
            out.append(rel)
    return out


def build(root):
    concepts = []
    for path in sorted(_iter_md(root), key=lambda p: _rel_id(p, root)):
        try:
            fm, body = _parse_doc(open(path, encoding="utf-8").read())
        except ValueError:
            continue
        cid = _rel_id(path, root)
        tags = fm.get("tags") or []
        if not isinstance(tags, list):
            tags = [str(tags)]
        concepts.append({
            "id": cid,
            "type": str(fm.get("type") or "Unknown"),
            "title": str(fm.get("title") or cid),
            "description": str(fm.get("description") or ""),
            "resource": str(fm.get("resource") or ""),
            "tags": [str(t) for t in tags],
            "body": body or "",
            "links_to": _extract_links(body or "", os.path.dirname(path), root),
        })

    ids = {c["id"] for c in concepts}
    nodes, edges, bodies, seen_edges = [], [], {}, set()
    for c in concepts:
        color = _TYPE_PALETTE.get(c["type"], _DEFAULT_NODE_COLOR)
        nodes.append({"data": {
            "id": c["id"],
            "label": c["title"] or c["id"],
            "type": c["type"],
            "description": c["description"],
            "resource": c["resource"],
            "tags": c["tags"],
            "color": color,
            "size": 30 + min(60, len(c["body"]) // 200),
        }})
        bodies[c["id"]] = c["body"]
        for target in c["links_to"]:
            if target == c["id"] or target not in ids:
                continue
            key = (c["id"], target)
            if key in seen_edges:
                continue
            seen_edges.add(key)
            edges.append({"data": {
                "id": f"{c['id']}__{target}",
                "source": c["id"],
                "target": target,
            }})

    return {
        "nodes": nodes,
        "edges": edges,
        "bodies": bodies,
        "types": sorted({c["type"] for c in concepts}),
        "palette": _TYPE_PALETTE,
    }


def main():
    graph = build(_BUNDLE_ROOT)
    check = "--check" in sys.argv
    if check:
        cur = json.load(open(_OUT, encoding="utf-8"))
        cn, ce = len(cur["nodes"]), len(cur["edges"])
        gn, ge = len(graph["nodes"]), len(graph["edges"])
        cur_bodies, new_bodies = cur["bodies"], graph["bodies"]
        body_diff = [k for k in set(cur_bodies) | set(new_bodies)
                     if cur_bodies.get(k) != new_bodies.get(k)]
        print(f"current : nodes={cn} edges={ce} types={cur['types']}")
        print(f"rebuilt : nodes={gn} edges={ge} types={graph['types']}")
        print(f"body mismatches: {len(body_diff)}", body_diff[:10])
        ok = (cn == gn and ce == ge and not body_diff)
        print("PARITY OK" if ok else "PARITY FAIL")
        sys.exit(0 if ok else 1)
    json.dump(graph, open(_OUT, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"wrote {_OUT}: nodes={len(graph['nodes'])} "
          f"edges={len(graph['edges'])} types={graph['types']}")


if __name__ == "__main__":
    main()
