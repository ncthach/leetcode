from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        def area(l: int, r: int) -> int:
            return min(height[l], height[r]) * (r - l)

        n = len(height)
        if n <= 1:
            return 0

        l = 0
        r = n - 1
        max_area = area(l, r)

        while l < r:
            if height[l] < height[r]:
                cur = height[l]
                while height[l] <= cur:
                    l += 1
                max_area = max(max_area, area(l, r))
            else: # height[l] >= height[r]
                cur = height[r]
                while r > l and height[r] <= cur:
                    r -= 1
                max_area = max(max_area, area(l, r))

        return max_area


cases = [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([], 0),
    ([1], 0),
    ([1, 1], 1),
    ([1, 5], 1),
    ([1, 1, 1, 1], 3),
    ([1, 1, 1, 2], 3),
    ([2, 1, 1, 1], 3),
    ([2, 1, 1, 2], 6),
    ([1, 2, 2, 1], 3),
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 1], 4),
    ([1, 2, 3, 4, 3, 2, 1], 8)
]

for input, expected in cases:
    sol = Solution()
    output = sol.maxArea(input)
    result = 'P' if output == expected else 'F'
    print(f"{result} output: {output} expected: {expected}")
