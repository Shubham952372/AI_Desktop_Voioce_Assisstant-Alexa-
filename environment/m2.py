import sys
import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    prev_nodes = {}

    while pq:
        current_dist, current_node = pq.pop(0)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                pq.append((distance, neighbor))
                prev_nodes[neighbor] = current_node

    return distances, prev_nodes

def print_shortest_paths(distances, prev_nodes, start):
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, f"Shortest paths from '{start}':\n")
    for node, distance in distances.items():
        if distance == sys.maxsize:
            output_text.insert(tk.END, f"No path exists to {node}\n")
        else:
            path = []
            current = node
            while current != start:
                path.append(current)
                current = prev_nodes[current]
            path.append(start)
            path.reverse()
            output_text.insert(tk.END, f"{node}: {' -> '.join(path)} (Cost: {distance})\n")

def visualize_graph():
    G = nx.Graph()
    for node, neighbors in graph.items():
        G.add_node(node)
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    canvas = FigureCanvasTkAgg(plt.gcf(), master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

def run_dijkstra():
    start_node = start_node_entry.get()
    distances, prev_nodes = dijkstra(graph, start_node)
    print_shortest_paths(distances, prev_nodes, start_node)

# Graph representation
graph = {
    'T': {'U': 2, 'V': 4, 'Y': 7},
    'U': {'T': 2, 'V': 3, 'W': 3},
    'V': {'T': 4, 'U': 3, 'W': 4, 'X': 3, 'Y': 8},
    'W': {'V': 4, 'U': 3, 'X': 3},
    'X': {'Z': 8, 'Y': 6, 'V': 3, 'W': 6},
    'Y': {'Z': 12, 'T': 7, 'V': 8, 'X': 6},
    'Z': {'X': 8, 'Y': 12}
}

# Create the main window
window = tk.Tk()
window.title("Dijkstra's Algorithm")

# Create the input field for the start node
start_node_label = ttk.Label(window, text="Start Node:")
start_node_label.pack(pady=5)
start_node_entry = ttk.Entry(window)
start_node_entry.pack(pady=5)

# Create the button to run Dijkstra's algorithm
run_button = ttk.Button(window, text="Run Dijkstra's Algorithm", command=run_dijkstra)
run_button.pack(pady=5)

# Create the output text area
output_text = tk.Text(window, height=10, width=50)
output_text.pack(pady=5)

# Visualize the graph
visualize_graph()

# Start the main event loop
window.mainloop()