class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #make a dict out of the array, loop through the dict to see if a - target 
        #is in the dict and if so ruturn the keys of a and the other value
        """
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for key in my_dict:
            find = target - key
            if find in my_dict and my_dict[find] != my_dict[key]:
                return [my_dict[find],my_dict[key]]
        """
        #The way I did it above will not be able to compute if for cases such as case 3 due to the way dictionaries work 

        my_dict = {}
        for i, nums in enumerate(nums):
            find = target - nums

            if find in my_dict:
                return [my_dict[find], i]

            my_dict[nums] = i

        