# Last updated: 6/6/2026, 10:25:47 PM
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        m, n = len(nums1), len(nums2)
        min_heap = []
        visited = set()

        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))

        result = []

        while min_heap and len(result) < k:
            total, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < n and (i, j + 1) not in visited:
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))

            if i + 1 < m and (i + 1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))

        return result
