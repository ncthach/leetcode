from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n == 0:
            return 0

        last_one_count = 1
        last_two_count = 1
        current_set = [fruits[0]]

        max_count = 0
        for i in range(1, n):
            current_fruit = fruits[i]
            previous_fruit = fruits[i - 1]
            if current_fruit == previous_fruit:
                last_one_count += 1
                last_two_count += 1
                continue

            if len(current_set) < 2:
                current_set.append(current_fruit)
                last_one_count = 1
                last_two_count += 1
                continue

            if current_fruit in current_set:
                last_two_count += 1
                last_one_count = 1
                continue

            max_count = max(last_two_count, max_count)
            last_two_count = last_one_count + 1
            last_one_count = 1
            current_set = [previous_fruit, current_fruit]

        max_count = max(last_two_count, max_count)
        return max_count







cases = [
    ([1,2,1], 3),
    ([0,1,2,2], 3),
    ([1,2,3,2,2], 4),
    ([], 0),
    ([1], 1),
    ([1, 1], 2),
    ([1, 1, 1, 2, 2], 5),
    ([3,3,3,1,2,1,1,2,3,3,4], 5),
    ([1, 1, 2, 2, 1, 1, 2, 2, 1, 1], 10)
]

sol = Solution()
for fruits, expt in cases:
    print(sol.totalFruit(fruits), " expected ", expt)