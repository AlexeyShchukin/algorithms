"""
You are given a network of n directed nodes, labeled from 1 to n. You are also given times,
a list of directed edges where times[i] = (ui, vi, ti).

ui is the source node (an integer from 1 to n)
vi is the target node (an integer from 1 to n)
ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
You are also given an integer k, representing the node that we will send a signal from.

Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes
to receive the signal, return -1 instead.
"""

import collections
import heapq


class Solution:
    def network_delayTime(self, times: list[list[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            max_time = time

            for neighbor, weight in edges[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (time + weight, neighbor))
        return max_time if len(visited) == n else -1
