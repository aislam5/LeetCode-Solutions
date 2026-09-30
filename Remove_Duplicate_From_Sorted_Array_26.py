class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #ok so it has to be in place, so loop through
        #cannot use for loop as it calculates the len of the list once, while loop will keep updating the len of the list
        """
        k = 0 #unique elements
        i=0
        j=1
        while j < len(nums):
            if nums[i] == nums[j]:
                del nums[j]
            else:
                i+=1
                j+=1
        #since I am deleting the elements the time complexity is too much therefore I need to find another solution
        """

        i = 0
        k = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j] and j != i+1:
                nums[i+1] = nums[j]
                i+=1
            else:
                pass
                k += 1
        toDel = len(nums) - k
        while toDel > 0: #this is always deleting one
            nums.pop()
            toDel -= 1


            

            

