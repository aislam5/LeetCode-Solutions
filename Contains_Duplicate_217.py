class Solution:
    """
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums [j]:
                    return True
        return False 
    """

    def containsDuplicate(self, nums: list[int]) -> bool:
        setNums = set(nums)
        if len(nums) == len(setNums):
            return False
        else:
            return True