class Solution:
    signs = {"+", "-"}
    digits = {str(i) for i in range(10)}
    boundary = 2 ** 31

    def clamp(self, num: int) -> int:
        if num < -self.boundary:
            return -self.boundary
        elif num >= self.boundary:
            return self.boundary - 1
        return num
    
    def myAtoi(self, s:str) -> int:
        index = 0
        l = len(s)
        val = 0
        neg = False
        while index < l and s[index] == " ":
            index += 1
        if index >= l or s[index] not in self.signs.union(self.digits):
            return 0
        if s[index] == "-":
            neg = True
        elif s[index] in self.digits:
            val = int(s[index])
        index += 1
        while index < l and s[index] in self.digits:
            val = val * 10 + int(s[index])
            index += 1
        if neg:
            val = -val
        return self.clamp(val)

prefixes = ["", "  ", "a", "a  ", "  a", "  a "]
numbers = [123, -123, 0, ""]
suffices = ["", "  ", "a", "a  ", "  a", "  a ", " 456", "a456", " a456"]
sol = Solution()
for prefix in prefixes:
    for number in numbers:
        for suffix in suffices:
            case = prefix + str(number) + suffix
            print(case, sol.myAtoi(case))

