class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mp = (low + high) // 2
                if arr[mp] == target:
                    return mp
                elif arr[mp] < target:
                    low = mp + 1
                else:
                    high = mp - 1
            
            return -1

        low = 0
        high = len(matrix) - 1
        target_row_idx = -1
        while low <= high:
            mp = (low + high) // 2
            if matrix[mp][0] <= target and matrix[mp][len(matrix[mp]) - 1] >= target:
                target_row_idx = mp
                break
            elif matrix[mp][0] > target:
                high = mp - 1
            else:
                low = mp + 1
      
        target_row = matrix[target_row_idx]
        if binary_search(target_row, target) != -1:
            return True

        return False
            





