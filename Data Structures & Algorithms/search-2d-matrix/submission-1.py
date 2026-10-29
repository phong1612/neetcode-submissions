class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            x = mid // n
            y = mid % n
            print(mid, x, y, matrix[x][y])
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                left = mid + 1
            elif matrix[x][y] > target:
                right = mid - 1
        return False