class Solution:
    def two_to_thirty_one(self) -> int:
        ret = 2
        for i in range(30):
            ret += ret
        return ret

    def clamp(self, val: int) -> int:
        lower = -self.two_to_thirty_one()
        upper = self.two_to_thirty_one() - 1
        if val < lower:
            return lower
        if val > upper:
            return upper
        return val

    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        powers = []
        quot_powers = []
        val = divisor
        quot = 1
        while val <= dividend:
            powers.append(val)
            quot_powers.append(quot)
            val += val
            quot += quot
        quotent = 0
        remainder = dividend
        for i in range(len(powers) - 1, -1, -1):
            if powers[i] <= remainder:
                quotent += quot_powers[i]
                remainder = remainder - powers[i]

        if neg:
            quotent = -quotent

        return self.clamp(quotent)

lower = -2 ** 31
upper = 2 ** 31 - 1
cases = [
    (10, 2, 5),
    (10, 3, 3),
    (10, 12, 0),
    (-10, 2, -5),
    (-10, 3, -3),
    (-10, 12, 0),
    (lower, 1, lower),
    (lower, -1, upper),
    (upper, 1, upper),
    (upper, -1, -upper),
    (lower, upper, -1),
    (upper, lower, 0),
    (lower, lower, 1),
    (upper, upper, 1),
    (lower, -lower, -1),
    (upper, -upper, -1),
]

sol = Solution()
print(sol.two_to_thirty_one())
for dividend, divisor, expected in cases:
    ret = sol.divide(dividend, divisor)
    check = "P" if ret == expected else "F"
    print(check, dividend, divisor, expected, ret)