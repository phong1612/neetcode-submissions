class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        precompute_left , precompute_right = [0] * n, [0]*n
        precompute_left[0] = height[0]
        for i in range(1, len(height)):
            precompute_left[i] = max(precompute_left[i - 1], height[i])
        precompute_right[n - 1] = height[n - 1]
        for i in range(len(height) - 2, 0, -1):
            precompute_right[i] = max(precompute_right[i + 1], height[i])
        sum = 0
        for i in range(1, n - 1):
            sum += min(precompute_left[i], precompute_right[i]) - height[i]
        return sum