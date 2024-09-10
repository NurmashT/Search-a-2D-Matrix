class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            mid = top + (bot - top) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break

        if top > bot:
            return False
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            midpoint = l + (r - l) // 2
            if target == matrix[mid][midpoint]:
                return True
            elif target > matrix[mid][midpoint]:
                l = midpoint + 1
            else:
                r = midpoint - 1
        return False
