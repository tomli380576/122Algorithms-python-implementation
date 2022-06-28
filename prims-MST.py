from queue import PriorityQueue
import math
import numpy as np

SAMPLE_WEIGHTED_UNDIRECTED_GRAPH = np.array([[0, 9, 75, 0, 0],
                                             [9, 0, 95, 19, 42],
                                             [75, 95, 0, 51, 66],
                                             [0, 19, 51, 0, 31],
                                             [0, 42, 66, 31, 0]])


def getEdges(G: np.ndarray):
    num_vertices = len(G)
    edges = []
    for y in range(num_vertices):
        for x in range(num_vertices):
            if x < y and G[y, x] != 0:
                edges.append((y, x))
    return edges


def isSafeEdge(curr_tree: list[tuple], edge: tuple):
    if len(curr_tree) == 0:
        return True
    x, y = zip(*curr_tree)
    u, v = edge[1]

    # let uv be the edge
    # if neither u or v is in the tree, then it's not connected
    # if both are in, then it's a cycle
    # so the condition is 'not disconnected nor creates a cycle'
    return not ((u not in x + y and v not in x + y) or
                (u in x + y and v in x + y))


def PrimsMST(G: np.ndarray):
    priority_queue = PriorityQueue()
    # Initially, add all edges to PQ
    for edge in getEdges(G):
        # (weight, edge)
        priority_queue.put((G[edge], edge))

    # Take global min
    # if the graph is connected, it definitely has global min
    curr_tree = [priority_queue.get()[1]]
    while not priority_queue.empty():
        min_edge = priority_queue.get()
        if isSafeEdge(curr_tree, min_edge):
            curr_tree.append(min_edge[1])

    return curr_tree


if __name__ == '__main__':
    print(
        f'Edges selected by Prim\'s MST: {PrimsMST(SAMPLE_WEIGHTED_UNDIRECTED_GRAPH)}'
    )