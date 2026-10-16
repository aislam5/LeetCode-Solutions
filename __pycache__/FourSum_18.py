class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = []
        nums.sort()
        for a in range (len(nums)):
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
                        toAdd = [nums[a], nums[b], nums[l], nums[r]]
                        if toAdd not in result:
                            result.append(toAdd)
                        l+=1
                        r-=1

        return result