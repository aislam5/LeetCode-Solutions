class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        #ok binary search maybe we can reuse the code 
        left = 0 
        right = len(nums)-1
        targetFound = False
        while left <= right:
            mid = (left+right)//2 #gets the middle
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: #if target == mid
                #we have to check the left and the right and if they are equal to target we should add it to the range
                targetFound = True
                point = mid
                start = mid
                end = mid 
                while nums[mid-1] == target:
                    start = mid-1
                    mid-=1
                mid = point
                while nums[mid+1] == target:
                    end = mid + 1
                    mid += 1
                return [start,end]
        return [-1,-1]
        """
        #ok we can implement searching for the first and last instance of the a specific element

        left = 0
        right = len(nums)-1
        start = -1
        end = -1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                #once we have found the target we search the left side for the start
                start = mid
                right = mid - 1
        
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                #once we have found the target we search the right side for the start
                end = mid
                left = mid + 1

        return [start,end]