"""
1514. Path with Maximum Probability

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list
where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of
success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start
to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer
by at most 1e-5.
"""
import collections
import heapq


class Solution:
    def max_probability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int,
                        end_node: int) -> float:
        graph = collections.defaultdict(list)

        for (src, target), p in zip(edges, succProb):
            graph[src].append((p, target))
            graph[target].append((p, src))

        visited = set()
        heap = [(-1, start_node)]

        while heap:
            prob, node = heapq.heappop(heap)

            if node == end_node:
                return -prob

            if node in visited:
                continue

            visited.add(node)

            for p, neighbor in graph[node]:
                heapq.heappush(heap, (p * prob, neighbor))

        return 0
