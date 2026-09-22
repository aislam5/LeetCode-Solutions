class Solution:
    def maxArea(self, height: list[int]) -> int:
        mostArea = 0
        l = 0
        r = len(height) -1
        while l<r:
            currentArea = 0
            distance = r - l
            if height[l] > height[r]:
                currentArea = height[r] * distance
                r -= 1
            else: #left is smaller or equal to
                currentArea = height[l] * distance
                l += 1
            
            #checks if the currentArea is 
            if currentArea > mostArea:
                mostArea = currentArea
        return mostArea
    #was over complicating the method a lot when it was a lot simpler. This was a fun problem as I knew what had to be done but just couldn't get to it. Might be because I am very sleepy
            

if __name__ == "__main__":
    solution = Solution()
    test1 = [1,3,2,5,25,24,5]
    value = solution.maxArea(test1)
    print(value)