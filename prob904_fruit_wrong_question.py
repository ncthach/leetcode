from heapq import *
from collections import defaultdict
from typing import List

class Solution:
    def toCounts(self, fruits: List[int]) -> List[List[int]]:
        if not fruits:
            return []

        counts = []
        current = fruits[0]
        current_count = 1
        for i in range(1, len(fruits)):
            if fruits[i] == current:
                current_count += 1
            else:
                counts.append((current, current_count))
                current = fruits[i]
                current_count = 1
        counts.append((current, current_count))
        return counts

    def oneMoreFruit(self, counts: List[List[int]], start: int) -> int:
        first = counts[start][0]
        max_count = 0
        for i in range(start + 1, len(counts)):
            count_i = counts[i][1]
            if i > start + 1 and counts[i - 1][0] == first:
                # shouldn't count the first one as wild card
                count_i += counts[i - 1][1]
            if i + 1 < len(counts) and counts[i + 1][0] == first:
                count_i += counts[i + 1][1]
            if count_i > max_count:
                max_count = count_i

        return max_count

    def pickFirst(self, counts: List[List[int]], start: int) -> int:
        return counts[start][1] + self.oneMoreFruit(counts, start)

    def totalFruitRecurse(self, counts: List[List[int]], start: int) -> int:
        if start == len(counts) - 1:
            return counts[start][1]

        # print("pick ", start, " ", self.pickFirst(counts, start))

        return max(counts[start][1] + self.oneMoreFruit(counts, start), self.totalFruitRecurse(counts, start + 1))

    def totalFruit(self, fruits: List[int]) -> int:
        if not fruits:
            return 0
        counts = self.toCounts(fruits)
        # print(counts)
        return self.totalFruitRecurse(counts, 0)

cases = [
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
    [],
    [1],
    [1, 1],
    [1, 1, 1, 2, 2],
    [3,3,3,1,2,1,1,2,3,3,4]
]

sol = Solution()
for fruits in cases:
    print(sol.totalFruit(fruits))