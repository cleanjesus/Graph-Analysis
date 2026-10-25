Objective
Create, read, analyze, and display graphs. Refer to the lecture slides on Graphs, Components, Breadth-First Search, Giant Components, and Erdős–Rényi graphs.

Your program must be named:

graph.py
Interactive menus and input() are prohibited. All operations must be selected using command-line arguments.

Commands
Your program must support the following three commands.

Create an Erdős–Rényi Graph
python3 graph.py erdos N C SEED OUTPUT.gml
Example:

python3 graph.py erdos 100 1.5 427 random.gml
Read and Analyze a Graph
python3 graph.py read GRAPH.gml SOURCE
Example:

python3 graph.py read network.gml A
Display a Graph
python3 graph.py display GRAPH.gml OUTPUT.png
Example:

python3 graph.py display network.gml network.png
The commands can be combined into a workflow. For example:

python3 graph.py erdos 100 1.5 427 random.gml
python3 graph.py read random.gml 0
python3 graph.py display random.gml random.png
Command 1: erdos
python3 graph.py erdos N C SEED OUTPUT.gml
Create an Erdős–Rényi graph using the () model from the lecture slides.

The parameters are:

N: number of vertices.

C: constant used to calculate (p).

SEED: random seed.

OUTPUT.gml: GML file to create.

Calculate the probability using the function specified in the lecture:



If p > 1, use p = 1.

Create the graph using:

nx.erdos_renyi_graph(n, p, seed=seed)
Save it using:

nx.write_gml(...)
Print:

VERTICES <number>
P <probability>
EDGES <number>
COMPONENTS <number>
LARGEST_COMPONENT <number>
GIANT_COMPONENT <YES|NO>
GRAPH_FILE <filename>
Print P to six decimal places.

A giant component is a component containing at least half of the graph's vertices, according to the definition in the slides.

Command 2: read
python3 graph.py read GRAPH.gml SOURCE
Read an undirected graph from a GML file using:

nx.read_gml(...)
Analyze the graph using the definitions and BFS material in the lecture slides.

Print:

VERTICES <number>
EDGES <number>
DEGREES <vertex:degree ...>
DEGREE_SUM <number>
ODD_DEGREE_COUNT <number>
COMPONENTS <number>
COMPONENT_SIZES <sizes>
GIANT_COMPONENT <YES|NO>
DISTANCES <vertex:distance ...>
Requirements:

List vertices alphabetically in DEGREES.

List component sizes from largest to smallest.

Determine whether the graph contains a giant component.

Calculate BFS distances starting at SOURCE.

List vertices alphabetically in DISTANCES.

Use -1 for an unreachable vertex.

DEGREE_SUM should demonstrate the Handshaking Theorem from the slides.

ODD_DEGREE_COUNT should be consistent with the odd-degree theorem from the slides.

Example:

VERTICES 6
EDGES 5
DEGREES A:1 B:2 C:2 D:2 E:2 F:1
DEGREE_SUM 10
ODD_DEGREE_COUNT 2
COMPONENTS 1
COMPONENT_SIZES 6
GIANT_COMPONENT YES
DISTANCES A:0 B:1 C:2 D:3 E:4 F:5
Command 3: display
python3 graph.py display GRAPH.gml OUTPUT.png
Read the GML graph and display its structure using NetworkX and Matplotlib.

The visualization must contain:

vertices,

edges,

vertex labels.

Use a NetworkX layout such as:

nx.spring_layout(...)
Save the visualization to the filename supplied by OUTPUT.png.

Do not use:

plt.show()
After successfully creating the image, print:

GRAPH_IMAGE <filename>
For example:

GRAPH_IMAGE network.png
Error Handling
The program must terminate with a nonzero exit status for invalid input, including:

unknown command,

missing command-line arguments,

nonexistent GML file,

invalid source vertex,

N <= 0,

C < 0.

Submission
Submit (do not submit zip files):

graph.py
Your program will be tested entirely from the command line. Do not include an interactive menu. Submissions that do not follow the requirement will receive 0 points. 