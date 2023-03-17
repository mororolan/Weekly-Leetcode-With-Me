class Solution:
    def int_to_roman(self, num: int) -> str:
        # forced solution
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans_str = ""
        for i in range(len(values)):
            while num // values[i] != 0:
                ans_str += numerals[i]
                num -= values[i]
        return ans_str


if __name__ == '__main__':
    s = Solution()
    a = s.int_to_roman(8)
    print(a)
