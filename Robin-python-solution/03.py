class Solution:

    def length_of_longest_substring(self, s: str) -> int:
        # hashmap solution
        # 滑动窗口 sliding window
        ans = {}
        start_num = 0
        max_ans = 0
        for i in range((len(s))):
            if s[i] in ans:
                start_num = max(start_num, ans[s[i]] + 1)
            max_ans = max(i + 1 - start_num, max_ans)
            ans[s[i]] = i
        return max_ans

if __name__ == '__main__':
    s = Solution()
    # a = s.length_of_longest_substring("pwwkew")
    a = s.length_of_longest_substring("tmmzuxt")
    a = s.length_of_longest_substring("abcdedfrtyui")
    print(a)
