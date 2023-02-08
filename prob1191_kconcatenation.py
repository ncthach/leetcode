from typing import List

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        modulo = 10 ** 9 + 7
        def sumUpto(a: List[int]) -> List[int]:
            s = 0
            ret = []
            for i in range(len(a)):
                s += a[i]
                ret.append(s)
            return ret

        if not arr or k == 0:
            return 0

        sums = sumUpto(arr)
        total = sums[-1]
        max_left = max(max(sums), 0)
        max_right = max(total - min(sums), 0, total)

        max_middle = 0
        max_seen = sums[-1]
        for i in range(len(sums) - 1, -1, -1):
            max_middle = max(
                max_middle,
                max_seen - sums[i]
            )
            max_seen = max(max_seen, sums[i])
        max_middle = max(max_middle, max_seen)

        return (
            max_middle if k == 1
            else max(
                max_middle,
                max_left + max_right + max(0, (k - 2) * total)
            )
        ) % modulo

cases = [
    ([1, 2], 3, 9),
    ([1, -2, 1], 5, 2),
    ([-1, -2], 7, 0),

    # empty
    ([], 0, 0),
    ([], 1, 0),
    ([], 2, 0),
    ([], 5, 0),

    # one element positive
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([1], 5, 5),

    # one element negative
    ([-1], 0, 0),
    ([-1], 1, 0),
    ([-1], 2, 0),
    ([-1], 5, 0),

    # left = right = middle
    ([3, -2, 3], 0, 0),
    ([3, -2, 3], 1, 4),
    ([3, -2, 3], 2, 8),
    ([3, -2, 3], 3, 12),

    # left != right
    ([3, -2, - 2, 2, -1, 1], 0, 0),
    ([3, -2, - 2, 2, -1, 1], 1, 3),
    ([3, -2, - 2, 2, -1, 1], 2, 5),
    ([3, -2, - 2, 2, -1, 1], 5, 8),

    # middle only
    ([-5, 1, -4], 0, 0),
    ([-5, 1, -4], 1, 1),
    ([-5, 1, -4], 2, 1),
    ([-5, 1, -4], 5, 1),

    # huge number
    ([10000,10000,10000,10000,10000,10000,10000,10000,10000,10000], 100000, 999999937)
]

for arr, k, expected in cases:
    sol = Solution()
    output = sol.kConcatenationMaxSum(arr, k)
    print(f"{str(output == expected)} case: {arr}, {k}, output: {output}, expected: {expected}")
