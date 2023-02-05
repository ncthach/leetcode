from typing import List
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        steps = [0] * n
        max_steps_before = 0
        last_larger_index = 0
        for i in range(1, n):
            if (nums[i] < nums[i-1]):
                last_larger_index = i - 1
                max_steps_before = 0
            else:
                while last_larger_index >= 0 and nums[i] >= nums[last_larger_index]:
                    max_steps_before = max(max_steps_before, steps[last_larger_index])
                    last_larger_index -= 1
                if last_larger_index > -1:
                    steps[i] = max_steps_before + 1
                    max_steps_before = steps[i]
                else: # no larger element before
                    steps[i] = 0
                    max_steps_before = 0 # for completeness
        return max(steps)

sol = Solution()
print(sol.totalSteps([5,3,4,4,7,3,6,11,8,5,11]))
print(sol.totalSteps([4,5,7,7,13]))