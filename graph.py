#!/usr/bin/env python3
"""CECS 427 - Graph Analysis assignment.

Usage:
    python3 graph.py erdos N C SEED OUTPUT.gml
    python3 graph.py read GRAPH.gml SOURCE
    python3 graph.py display GRAPH.gml OUTPUT.png

---------------------------------------------------------------------------
Generative AI Disclosure (Syllabus Section 16)
---------------------------------------------------------------------------
The following generative AI tools were used in this assignment:
    Cursor IDE agent (Composer)

Usage of AI:
    - Used AI to brainstorm structure, map lecture definitions to required
      output fields.
    - Verified behavior with tester_graph.py and the README workflow.
---------------------------------------------------------------------------
"""

import math
import os
import sys
from collections import deque

import networkx as nx


def fail(message):
    """Print an error to stderr and exit with a nonzero status."""
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_graph(path):
    """Read an undirected graph from a GML file, exiting nonzero on failure."""
    if not os.path.isfile(path):
        fail(f"file not found: {path}")
    try:
        return nx.read_gml(path)
    except Exception as exc:
        fail(f"could not read GML file {path}: {exc}")


def component_sizes(G):
    """Connected component sizes, largest to smallest."""
    return sorted((len(c) for c in nx.connected_components(G)), reverse=True)


def has_giant_component(G):
    """A giant component contains at least half of the graph's vertices."""
    n = G.number_of_nodes()
    if n == 0:
        return False
    return max(component_sizes(G)) >= n / 2


def sorted_nodes(G):
    """Vertices in alphabetical order by label."""
    return sorted(G.nodes(), key=str)


def bfs_distances(G, source):
    """BFS shortest-path distances from source (unweighted graph)."""
    dist = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


def cmd_erdos(args):
    if len(args) != 4:
        fail("usage: graph.py erdos N C SEED OUTPUT.gml")

    try:
        n = int(args[0])
        c = float(args[1])
        seed = int(args[2])
    except ValueError:
        fail("N and SEED must be integers, C must be a number")

    output = args[3]

    if n <= 0:
        fail("N must be positive")
    if c < 0:
        fail("C must be nonnegative")

    p = c * math.log(n) / n
    if p > 1:
        p = 1.0

    G = nx.erdos_renyi_graph(n, p, seed=seed)

    try:
        nx.write_gml(G, output)
    except Exception as exc:
        fail(f"could not write GML file {output}: {exc}")

    sizes = component_sizes(G)
    largest = sizes[0] if sizes else 0

    print(f"VERTICES {G.number_of_nodes()}")
    print(f"P {p:.6f}")
    print(f"EDGES {G.number_of_edges()}")
    print(f"COMPONENTS {len(sizes)}")
    print(f"LARGEST_COMPONENT {largest}")
    print(f"GIANT_COMPONENT {'YES' if has_giant_component(G) else 'NO'}")
    print(f"GRAPH_FILE {output}")


def cmd_read(args):
    if len(args) != 2:
        fail("usage: graph.py read GRAPH.gml SOURCE")

    G = load_graph(args[0])
    source = args[1]

    if source not in G:
        resolved = None
        try:
            candidate = int(source)
            if candidate in G:
                resolved = candidate
        except ValueError:
            pass
        if resolved is None:
            fail(f"source vertex not in graph: {source}")
        source = resolved

    nodes = sorted_nodes(G)
    degrees = dict(G.degree())
    sizes = component_sizes(G)
    dist = bfs_distances(G, source)

    print(f"VERTICES {G.number_of_nodes()}")
    print(f"EDGES {G.number_of_edges()}")
    print("DEGREES " + " ".join(f"{v}:{degrees[v]}" for v in nodes))
    print(f"DEGREE_SUM {sum(degrees.values())}")
    print(f"ODD_DEGREE_COUNT {sum(1 for d in degrees.values() if d % 2 == 1)}")
    print(f"COMPONENTS {len(sizes)}")
    print("COMPONENT_SIZES " + " ".join(str(s) for s in sizes))
    print(f"GIANT_COMPONENT {'YES' if has_giant_component(G) else 'NO'}")
    print("DISTANCES " + " ".join(f"{v}:{dist.get(v, -1)}" for v in nodes))


def cmd_display(args):
    if len(args) != 2:
        fail("usage: graph.py display GRAPH.gml OUTPUT.png")

    G = load_graph(args[0])
    output = args[1]

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    pos = nx.spring_layout(G, seed=427)
    plt.figure(figsize=(8, 6))
    nx.draw_networkx_nodes(G, pos)
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    plt.axis("off")

    try:
        plt.savefig(output)
    except Exception as exc:
        fail(f"could not save image {output}: {exc}")
    finally:
        plt.close()

    print(f"GRAPH_IMAGE {output}")


def main():
    if len(sys.argv) < 2:
        fail("usage: graph.py erdos|read|display ...")

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "erdos":
        cmd_erdos(args)
    elif command == "read":
        cmd_read(args)
    elif command == "display":
        cmd_display(args)
    else:
        fail(f"unknown command: {command}")


if __name__ == "__main__":
    main()
