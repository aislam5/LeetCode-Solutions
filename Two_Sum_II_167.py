class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        #Pretty Simple Idea 2 pointers at each end if sum > target move right pointer down
        #If sum < target move left pointer up
        left = 0
        right = len(numbers) - 1

        while left < right:
            adder = numbers[left] + numbers[right]
            if adder < target:
                left += 1
            elif adder > target:
                right -= 1
            else:
                return [left+1, right+1]
        
            