class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[left]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
        return nums[mid]