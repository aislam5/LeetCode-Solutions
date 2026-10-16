class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        #ok for 4Sum
        result = []
        nums.sort()
        for a in nums:
            for b in range(a+1,len(nums)):
                l = b+1
                r = len(nums) - 1
                while l < r:
                    fourSum = nums[a] + nums[b] + nums [l] + nums[r]
                    if fourSum > target:
                        r -= 1
                    elif fourSum < target:
                        l += 1
                    else:
                        result.append([nums[a], nums[b], nums[l], nums[r]])
                        l+=1
                        r-=1

        return result