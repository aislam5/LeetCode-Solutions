#so we need a 2 pointer somewhere but I am not sure how. 
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        possibleCombinations = []
        nums.sort() #helps with a lot of stuff

        for i, num in enumerate(nums):
            #skips duplicate
            if i > 0 and num == nums[i-1]:
                continue #continue skips the current iteration and will be used instead of pass
            if num > 0: #Since the numbers are sorted if the current number is positive no number of 3 will sum to 0
                break
            
            #make 2 pointers one from the left and one from the right
            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    possibleCombinations.append([num, nums[l], nums[r]])
                    l+= 1 #both left and right move close to each other
                    r-= 1

                    while nums[l] == nums[l-1] and l<r:
                        l += 1 # skipping left side duplicates
        return possibleCombinations