"""class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #basically we have 2 array and we array num1 is a subset of array num2
        #we have to get the index of the number in num1 in num2 and then check if there is a greater element that comes after that number
        ans = []
        for i, num in enumerate(nums1):
            idx = nums2.index(num)
            for j in range(idx, len(nums2)):
                if nums2[j] > nums2[idx]:
                    toAdd = True
                    break
                else:
                    toAdd = False
            if toAdd:
                ans.append(nums2[j])
            else:
                ans.append(-1)
        return ans
"""
    #now we strive to find a solution with a stack

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans = []
        map = {}
        stack = []
        for i, num in enumerate(nums2):
            while stack and num > stack[-1]:
                popped = stack.pop()
                map[popped] = num
            stack.append(num)

        for j, num in enumerate(nums1):
            if num in map:
                ans.append(map[num])
            else:
                ans.append(-1)

        return ans
        #traverse nums2 and push elements on the stack 
        #if the current element is greater than stack[-1]
        #we pop that element and then add them to the map as the key and the current num as the value
        #
