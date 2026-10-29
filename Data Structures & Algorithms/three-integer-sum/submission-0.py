class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, ans = 0, []
        while l < len(nums) - 1:
            r = l + 1
            while r < len(nums):
                if (0 - nums[l] - nums[r]) in nums:
                    ind = nums.index(0 - nums[l] - nums[r])
                    if ind != l and ind != r:
                        answer = [nums[l], nums[r], 0 - nums[l] - nums[r]]
                        answer.sort()
                        if answer not in ans:
                            ans.append(answer)
                r += 1
            l += 1
        return ans