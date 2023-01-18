from math import max
from typing import List

class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        l = len(nums)
        if l == 0:
            return -1
        if l == 1:
            return -1 if k % 2 == 1 else nums[0]
        # l >= 2
        if k == 0:
            return nums[0]
        if k == 1:
            return nums[1]
        
        # k > 1, l >= 2
        if k <= l - 1:
            # either take k - 1 elements out and put the max back in
            # or take k elements out and leave nums[k] as the new top
            return max(max(nums[:k-1]), nums[k])
        if k <= l + 1:
            # k = l: take k - 1 elements out and put the max in
            # k = l + 1: take all elements out and put the max back in
            return max(nums[:k-1])
        # k >= l + 2 and l >= 2
        # take all elements out and put aside the max,
        # keep putting one other element in and take it out until we have 1 or 2 moves left,
        # put either the max, or another element and the max in depending on how many moves left
        return max(nums)