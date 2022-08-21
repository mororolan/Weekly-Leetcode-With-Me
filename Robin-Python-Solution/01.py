from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        #   hash map solution
        ans = {}
        for i in range(len(nums)):
            ans[target - nums[i]] = i
        for i in range(len(nums)):
            # if ans[nums[i]] != None  and ans[nums[i]] != i : 这个只能判断value是不是 None
            if nums[i] in ans and ans[nums[i]] != i:
                return [ans[nums[i]], i]
        return []


if __name__ == '__main__':
    s = Solution()
    a = s.two_sum([22, 3, 3], 6)
    print(a)

