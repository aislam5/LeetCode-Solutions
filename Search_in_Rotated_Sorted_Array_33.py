class Solution:
    def search(self, nums:list[int], target:int) -> int:
        #setting up left and right of the array
        left = 0 
        right = len(nums)-1

        while left <= right:
            #calculate mid 
            #this forumal might cause an integer overflow 
            mid = (left + right)//2

            #check if mid == target
            if nums[mid] == target:
                return mid

            #check if left half is sorted 
            if nums[left] < nums[mid]:

                #check if target it between if yes then make the right side to the mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                else:
                    left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


            