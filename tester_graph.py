#!/usr/bin/env python3

import subprocess
import sys
import tempfile
from pathlib import Path

import networkx as nx


def run(program, args, cwd):
    return subprocess.run(
        [sys.executable, str(program)] + args,
        cwd=cwd,
        capture_output=True,
        text=True,
        timeout=10,
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 test_graph.py graph.py")
        sys.exit(1)

    program = Path(sys.argv[1]).resolve()

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)

        G = nx.Graph()
        G.add_nodes_from(["J", "K", "L", "M", "N", "P"])
        G.add_edges_from([
            ("J", "K"),
            ("K", "L"),
            ("L", "M"),
            ("M", "N"),
        ])

        gml = tmp / "test.gml"
        nx.write_gml(G, gml)

        # READ
        r = run(program, ["read", str(gml), "L"], tmp)

        required = [
            "VERTICES 6",
            "EDGES 4",
            "DEGREES J:1 K:2 L:2 M:2 N:1 P:0",
            "DEGREE_SUM 8",
            "ODD_DEGREE_COUNT 2",
            "COMPONENTS 2",
            "COMPONENT_SIZES 5 1",
            "GIANT_COMPONENT YES",
            "DISTANCES J:2 K:1 L:0 M:1 N:2 P:-1",
        ]

        read_ok = (
            r.returncode == 0
            and r.stdout.strip().splitlines() == required
        )

        print("read:", "PASS" if read_ok else "FAIL")

        # ERDOS
        random_gml = tmp / "student_er.gml"

        r = run(
            program,
            ["erdos", "15", "0.9", "72", str(random_gml)],
            tmp,
        )

        er_ok = (
            r.returncode == 0
            and random_gml.exists()
            and random_gml.stat().st_size > 0
        )

        print("erdos:", "PASS" if er_ok else "FAIL")

        # DISPLAY
        image = tmp / "student.png"

        r = run(
            program,
            ["display", str(random_gml), str(image)],
            tmp,
        )

        display_ok = (
            r.returncode == 0
            and image.exists()
            and image.stat().st_size > 0
        )

        print("display:", "PASS" if display_ok else "FAIL")


if __name__ == "__main__":
    main()