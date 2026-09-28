class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #loop array and count 0s then remove all instances of 0 in the list and then append them in the end
        """
        count = 0
        for i, num in enumerate(nums):
            if num == 0:
                count+=1
            else:
                pass
        while count != 0:
            nums.remove(0)
            count -= 1
            nums.append(0)
        return nums

        Not Ideal for a Two Pointer Solution
        """

        #two pointer one to track zero position on to track real numbers
        #if normal number

        j = 0 # Pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at index j 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # Move j to the next index for placing non-zero