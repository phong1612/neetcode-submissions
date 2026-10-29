from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = dict(Counter(nums))
        print(count_nums)
        count_nums = sorted(count_nums, key=lambda x: count_nums[x], reverse=True)
        return count_nums[:k]