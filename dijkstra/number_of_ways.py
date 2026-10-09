"""
1976. Number of Ways to Arrive at Destination

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads
between some intersections. The inputs are generated such that you can reach any intersection from any
other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means
that there is a road between intersections ui and vi that takes timei minutes to travel.
You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the
shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time.
Since the answer may be large, return it modulo 109 + 7.
"""
import collections
import heapq


class Solution:
    def count_paths(self, n: int, roads: list[list[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        heap = [(0, 0)]
        min_time = [float('inf')] * n
        min_time[0] = 0
        ways = [0] * n
        ways[0] = 1
        mod = 10 ** 9 + 7

        while heap:
            time, node = heapq.heappop(heap)
            if time > min_time[node]:
                continue

            for neighbor, t in graph[node]:
                new_time = t + time
                if new_time < min_time[neighbor]:
                    min_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (new_time, neighbor))
                elif new_time == min_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod

        return ways[n - 1]
