class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i1, i2 = 0, 0
        all_num = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                all_num.append(nums1[i1])
                i1 += 1
            else:
                all_num.append(nums2[i2])
                i2 += 1
        while i1 < len(nums1):
            all_num.append(nums1[i1])
            i1 += 1
        while i2 < len(nums2):
            all_num.append(nums2[i2])
            i2 += 1
        n = len(all_num)
        if n % 2 == 1:
            return float(all_num[(n - 1) // 2])
        else:
            a = all_num[(n // 2) - 1]
            b = all_num[n // 2]
            return float((a + b) / 2)