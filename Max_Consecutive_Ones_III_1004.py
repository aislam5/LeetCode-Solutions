from collections import defaultdict

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:

        """ 
        left = 0 
        track = defaultdict(int)
        trackable = 0
        max_track = 0 

        for right, num in enumerate(nums):
            track[num] += 1
            if num != 1:
                trackable += 1
            while trackable > k:
                left_num = nums[left]
                if left_num != 1:
                    trackable -= 1
                track[left_num] -= 1
                left += 1
            max_track = max(max_track, (right-left + 1))
        return max_track
        """
    # ok we can make this better if I dont have a dictioanry
        left = 0 
        zeros = 0
        max_ones = 0 

        for right, num in enumerate(nums):
            if num == 0:
                zeros += 1
                
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max_ones = max(max_ones, (right-left + 1))
        return max_ones


