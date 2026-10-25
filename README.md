# Graph Analysis

CECS 427 (Network Analysis) assignment: create, analyze, and visualize graphs from the command line, including Erdős–Rényi random graphs and giant-component detection.

## Features

- **`erdos`** – generate an Erdős–Rényi random graph G(n, p) with `p = C·ln(n)/n` (capped at 1) and save it as GML. Reports vertices, edges, components, largest component, and whether a giant component exists.
- **`read`** – load a GML graph and report degrees, the Handshaking Theorem degree sum, odd-degree vertex count, connected components, giant-component status, and BFS distances from a source vertex.
- **`display`** – render the graph (vertices, edges, labels) to a PNG using NetworkX and Matplotlib.

Invalid input (unknown command, missing arguments, missing file, bad source vertex, `N <= 0`, `C < 0`) exits with a nonzero status. There are no interactive prompts.

## Requirements

- Python 3
- [NetworkX](https://networkx.org/)
- [Matplotlib](https://matplotlib.org/)

```bash
pip install networkx matplotlib
```

## Usage

```bash
python3 graph.py erdos N C SEED OUTPUT.gml
python3 graph.py read GRAPH.gml SOURCE
python3 graph.py display GRAPH.gml OUTPUT.png
```

Example workflow:

```bash
python3 graph.py erdos 100 1.5 427 random.gml
python3 graph.py read random.gml 0
python3 graph.py display random.gml random.png
```

Sample output of `read`:

```
VERTICES 6
EDGES 5
DEGREES A:1 B:2 C:2 D:2 E:2 F:1
DEGREE_SUM 10
ODD_DEGREE_COUNT 2
COMPONENTS 1
COMPONENT_SIZES 6
GIANT_COMPONENT YES
DISTANCES A:0 B:1 C:2 D:3 E:4 F:5
```

## Testing

`tester_graph.py` runs the program against the assignment's requirements:

```bash
python3 tester_graph.py graph.py
```

## Project Structure

| File | Description |
| --- | --- |
| `graph.py` | Main program (`erdos`, `read`, `display` commands) |
| `tester_graph.py` | Command-line test harness |
| `random.gml` / `random.png` | Example generated graph and its visualization |
| `ASSIGNMENT.md` | Original assignment instructions |

## Generative AI Disclosure

Generative AI (Cursor IDE agent) was used to help structure the program and map lecture definitions to the required output. See the header of `graph.py` for details.
