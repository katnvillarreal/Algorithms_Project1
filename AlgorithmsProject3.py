# Algorithms Project 3
# Group Members: Kile Adams, Monique Dashner, Kathryn Villarreal

import sys
import time
import heapq
from itertools import groupby
from collections import defaultdict
import collections

# Question 1 ############################################################################
# Undirected and Unweighted
# Both DFS and BFS

# Reference code for dfs by UTD Xue Kris Yu
def dfs(g):
    def dfs_path(graph, start, goal):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for neighbor in graph[vertex]:
                    stack.append((neighbor, path + [neighbor]))
        
    def main(g):
        path = dfs_path(g, 'A', 'B')
        if path:
            print(path)
        else:
            print('no path found')
    main(g)

''' The modified script for bfs is contributed by Maarten Fabre available at
https://codereview.stackexchange.com/questions/193410/breadth-first-search-implementation-in-python-3-to-find-path-between-two-given-n
'''
def bfs(g):
    def bfs_path(graph, start, goal):
        if start == goal:
            return [start]
        visited = {start}
        queue = [(start, [])]
        while queue:
            current, path = queue.pop(0) 
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor == goal:
                    return path + [current, neighbor]
                if neighbor in visited:
                    continue
                queue.append((neighbor, path + [current]))
                visited.add(neighbor)   
        return None
    def main(g):
        path = bfs_path(g, 'A', 'B')
        if path:
            print(path)
        else:
            print('no path found')
    main(g)

def q1():
    g = {'A': set(['B', 'E', 'F']),
            'B': set(['A','C','F']),
            'C': set(['B','G','D']),
            'D': set(['C','G']),
            'E': set(['A','F','I']),
            'F': set(['A','B','E','I']),
            'G': set(['C','D']),
            'H': set(['K','L']),
            'I': set(['E','F','J','M']),
            'J': set(['I']),
            'K': set(['H','L','O']),
            'L': set(['H','K','P']),
            'M': set(['I','N']),
            'N': set(['M']),
            'O': set(['K']),
            'P': set(['L'])}
    dfs(g)
    bfs(g)

# Question 2 ############################################################################################################
# Directed and unweighted
# Find the strongly connected components

# modified script for strongly connected components from original script
#https://github.com/ChuntaoLu/Algorithms-Design-and-
#Analysis/blob/master/week4%20Graph%20search%20and%20SCC/scc.py#L107

#set rescursion limit and stack size limit
sys.setrecursionlimit(10 ** 6)
#resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


class Tracker(object):
    """Keeps track of the current time, current source, component leader,
    finish time of each node and the explored nodes.
    
    'self.leader' is informs of {node: leader, ...}."""

    def __init__(self):
        self.current_time = 0
        self.current_source = None
        self.leader = {}
        self.finish_time = {}
        self.explored = set()


def dfs_scc(graph_dict, node, tracker):
    """Inner loop explores all nodes in a SCC. Graph represented as a dict,
    {tail: [head_list], ...}. Depth first search runs recursively and keeps
    track of the parameters"""

    tracker.explored.add(node)
    tracker.leader[node] = tracker.current_source
    for head in graph_dict[node]:
        if head not in tracker.explored:
            dfs_scc(graph_dict, head, tracker)
    tracker.current_time += 1
    tracker.finish_time[node] = tracker.current_time


def dfs_loop(graph_dict, nodes, tracker):
    """Outer loop checks out all SCCs. Current source node changes when one
    SCC inner loop finishes."""

    for node in nodes:
        if node not in tracker.explored:
            tracker.current_source = node
            dfs_scc(graph_dict, node, tracker)


def graph_reverse(graph):
    """Given a directed graph in forms of {tail:[head_list], ...}, compute
    a reversed directed graph, in which every edge changes direction."""

    reversed_graph = defaultdict(list)
    for tail, head_list in graph.items():
        for head in head_list:
            reversed_graph[head].append(tail)
    return reversed_graph


def scc(graph):
    """First runs dfs_loop on reversed graph with nodes in decreasing order,
    then runs dfs_loop on original graph with nodes in decreasing finish
    time order(obtained from first run). Return a dict of {leader: SCC}."""

    out = defaultdict(list)
    tracker1 = Tracker()
    tracker2 = Tracker()
    nodes = set()
    reversed_graph = graph_reverse(graph)
    for tail, head_list in graph.items():
        nodes |= set(head_list)
        nodes.add(tail)
    nodes = sorted(list(nodes), reverse=True)
    dfs_loop(reversed_graph, nodes, tracker1)
    sorted_nodes = sorted(tracker1.finish_time,
                          key=tracker1.finish_time.get, reverse=True)
    dfs_loop(graph, sorted_nodes, tracker2)
    for lead, vertex in groupby(sorted(tracker2.leader, key=tracker2.leader.get),
                                key=tracker2.leader.get):
        out[lead] = list(vertex)
    return out

def q2():
    start = time.time()
    g = {'1': set(['3']),
        '2': set(['1']),
        '3': set(['2','5']),
        '4': set(['1','2','12']),
        '5': set(['6','8']),
        '6': set(['7','8','10']),
        '7': set(['10']),
        '8': set(['9','10']),
        '9': set(['5','11']),
        '10': set(['9','11']),
        '11': set(['12']),
        '12': set()}
    t1 = time.time() - start
    groups = scc(g)
    t2 = time.time() - start
    top_5 = heapq.nlargest(5, groups, key=lambda x: len(groups[x]))
    result = []
    for i in range(5):
        try:
            result.append(len(groups[top_5[i]]))
        except:
            result.append(0)
    return result, groups
##################################################################################################################

# Question 3
# Undirected and weighted
# Dijkstra's

def q3():
    # Python implementation of Dijkstra's algorithm
    #https://gist.github.com/econchick/4666413
    class Graph:
        def __init__(self):
            self.nodes = set()
            self.edges = collections.defaultdict(list)
            self.distances = {}

        def add_node(self, value):
            self.nodes.add(value)

        def add_edge(self, from_node, to_node, distance):
            self.edges[from_node].append(to_node)
            self.edges[to_node].append(from_node)
            self.distances[(from_node, to_node)] = distance
                                        
    def dijkstra(graph, initial):
        visited = {initial: 0}
        path = {}

        nodes = set(graph.nodes)

        while nodes: 
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in graph.edges[min_node]:
                weight = current_weight + graph.distance[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path

    def main():
        graph = Graph()
        graph.nodes = {'A','B','C','D','E','F','G','H','I'}
        graph.edges = {'A': ['B', 'C', 'D'], 'B':['A','C', 'F', 'H'], \
                'C':['A', 'B', 'D', 'F', 'E'], 'D':['A', 'C', 'E', 'I'],\
                'E': ['C', 'D', 'F', 'G'], 'F':['B', 'C', 'E', 'G', 'H'],\
                'F':['B', 'C', 'E', 'G', 'H'], 'G':['E', 'F', 'H', 'I'], \
                'H':['B', 'F', 'G', 'I'], 'I':['D', 'G', 'H']}
        graph.distance = {('A', 'B'):22, ('A', 'C'):9, ('A', 'D'):12,\
                    ('B', 'A'):22, ('B', 'C'):35, ('B', 'F'):36, ('B', 'H'):34,\
                    ('C', 'A'):9, ('C', 'B'):35, ('C', 'D'):4, ('C', 'E'):65, ('C', 'F'):42,\
                    ('D', 'A'):12, ('D', 'C'):4, ('D', 'E'):33, ('D', 'I'):30,\
                    ('E', 'C'):65, ('E', 'D'):33, ('E', 'F'):18, ('E', 'G'):23, \
                    ('F', 'B'):36, ('F', 'C'):42, ('F', 'E'):18, ('F', 'G'):39, ('F', 'H'):24,\
                    ('G', 'E'):23, ('G', 'F'):39, ('G', 'H'):25, ('G', 'I'):21,\
                    ('H', 'B'):34, ('H', 'F'):24, ('H', 'G'):25, ('H', 'I'):21,\
                    ('I', 'D'):30, ('I', 'G'):21, ('I', 'H'):19,
                   }

        v, path = dijkstra(graph, 'A')
        print('Visited: ', v)
        print('Path :', path)

    main()

if __name__ == "__main__":
    q1()
    count, components = q2()
    print('Strongly connected components are:')
    for key in components:
        print(components[key])
    q3()