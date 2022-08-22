class Solution:
    def roman_to_int(self, s: str) -> int:
        # forced solution
        hash_mp = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ans_num = 0
        i = 0
        while i < len(s) - 1:
            if hash_mp[s[i]] >= hash_mp[s[i + 1]]:
                ans_num += hash_mp[s[i]]
            else:
                ans_num -= hash_mp[s[i]]
            i += 1
        ans_num += hash_mp[s[-1]]
        return ans_num


if __name__ == '__main__':
    s = Solution()
    a = s.roman_to_int("IV")
    print(a)
