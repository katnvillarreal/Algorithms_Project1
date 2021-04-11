# Algorithms Project 3
# Group Members: Kile Adams, Monique Dashner, Kathryn Villarreal

import sys
import time
import heapq
from itertools import groupby
from collections import defaultdict

# Question 1 ############################################################################
# Undirected and Unweighted
# Both DFS and BFS
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
# A: (B,22), (C,9), (D,12)
# B: (A,22), (C,35), (F,36), (H,34)
# C: (A,9), (B,35), (F,42), (E,65), (D,4)
# D: (A,12), (C,4), (E,33), (I,30)
# E: (C,65), (D,33), (F,18), (G,23)
# F: (B,36), (C,42), (E,18), (G,39), (H,24)
# G: (E,23), (F,39), (H,25), (I,21)
# H: (B,34), (F,24), (G,25), (I,19)
# I: (D,30), (G,21), (H,19)

if __name__ == "__main__":
    q1()
    count, components = q2()
    print('Strongly connected components are:')
    for key in components:
        print(components[key])