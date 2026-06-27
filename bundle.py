#!/usr/bin/env python3
"""Reassemble ssdl.spec.md from the split sources listed in bundler.manifest.yml.

Concatenates: stub + toc + every file under `order:` (in order). The split files are
verbatim section/component slices, so the bundle is a byte-for-byte reproduction of the
spec. Usage: python3 bundle.py [output_path]   (default: ssdl.spec.md)
"""
import sys

def parse_manifest(path="bundler.manifest.yml"):
    stub = toc = None
    order = []
    mode = None
    for ln in open(path, encoding="utf-8"):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if ln.startswith("stub:"):
            stub = ln.split(":", 1)[1].strip()
        elif ln.startswith("toc:"):
            toc = ln.split(":", 1)[1].strip()
        elif ln.startswith("order:"):
            mode = "order"
        elif ln.startswith("components:"):
            mode = "components"
        elif mode == "order" and s.startswith("- "):
            order.append(s[2:].strip())
    return stub, toc, order

def build():
    stub, toc, order = parse_manifest()
    rd = lambda p: open(p, encoding="utf-8").read()
    return rd(stub) + rd(toc) + "".join(rd(p) for p in order)

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "ssdl.spec.md"
    open(out, "w", encoding="utf-8").write(build())
    print("wrote", out)
