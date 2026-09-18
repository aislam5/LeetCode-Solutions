class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setNums = set(nums)
        maxLength = 0
        for num in setNums:
            length = 1
            if num - 1 in setNums:
                pass
            else:
                while nums + length in setNums:
                    length += 1
            if length > maxLength:
                maxLength = length  
        return maxLength

    #ok the solution wasnt that hard im just an idiot who cant think straight