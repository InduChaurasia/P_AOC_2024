"""AOC day 23: https://adventofcode.com/2024/day/23"""
import networkx as nx
from utilities import read_file,Year

def read_input():
    graph = nx.Graph()
    for line in read_file(Year.y2024, 'day23.txt'):
        a,b= line.split('-')
        graph.add_edge(a,b)
    return graph

def find_three_system_lan(graph, node):
    neighbors = list(graph.neighbors(node))
    connected={",".join(sorted([node, neighbors[i], neighbors[j]]))
               for i in range(len(neighbors)-1)
                    for j in range(i+1, len(neighbors))
                        if graph.has_edge(neighbors[i], neighbors[j])}
    return connected

def count_three_system_lan(graph):
    connected=set()
    for node in list(graph.nodes):
        if node.startswith('t'):
            connected.update(find_three_system_lan(graph, node))
    print(f"sets of three inter-connected computers having at least one computer with a name that starts with t: {len(connected)}")

def find_max_length_grpah(graph):
    max_click= max(nx.find_cliques(graph), key=len)
    print(f"max length Lan: {",".join(sorted(max_click))}")

def main():
    graph = read_input()
    count_three_system_lan(graph)
    find_max_length_grpah(graph)

if __name__ == "__main__":
    main()
