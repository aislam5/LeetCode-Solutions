class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        #basically its just searching an array but it has multiple layers to unpack now 
        #ok first we identify which one we are going to search in. 
        #then we use the basic binary search to see which we are seaeching in 
        list_left = 0
        list_right = len(matrix) - 1
        chosen = None
        while list_left <= list_right: #while loop will identify which one we will work in 
            list_mid = (list_left + list_right)//2
            test = matrix[list_mid]
            #check if the target value is within the test list
            if  test[0] <= target and target <= test[len(test)-1]: 
                chosen = matrix[list_mid]
                break
            elif test[0] < target:
                list_left = list_mid + 1
            else:
                list_right = list_mid - 1

        if chosen ==  None:
            return False

        left = 0
        right = len(chosen) - 1
        while left <= right:
            mid = (left+right)//2
            if chosen[mid] < target:
                left = mid + 1
            elif chosen[mid] > target:
                right = mid - 1
            else:
                return True
        
        return False