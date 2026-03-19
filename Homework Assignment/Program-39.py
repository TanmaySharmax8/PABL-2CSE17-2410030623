class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        m = len(matrix)     # Number of rows
        n = len(matrix[0])  # Number of columns
        
        left = 0
        right = (m * n) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Map the 1D 'mid' index back to 2D coordinates
            # mid // n gives the row, mid % n gives the column
            row = mid // n
            col = mid % n
            
            mid_value = matrix[row][col]
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False