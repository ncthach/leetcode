from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        first, last, num_jumps = 0, 0, 0
        while last < n - 1:
            num_jumps += 1
            next_last = last
            for i in range(first, last + 1):
                next_last = max(next_last, i + nums[i])
            first = last + 1
            last = next_last
        return num_jumps
cases = [
    ([2,3,1,1,4], 2),
    ([2,3,0,1,4], 2),
    ([1,1,1,1], 1),
    ([1,1,1,2], 2),
    ([1,2,0,1,4], 3),
    ([1], 0)
]

sol = Solution()
for input, expected in cases:
    print(sol.jump(input), " expected ", expected)
