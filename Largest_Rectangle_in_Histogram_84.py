class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        #Solution works but the time complexity is a lot
        """
        maxHeight = 0
        for i, height in enumerate(heights):
           stack = []
           if stack and heights[i] < stack[-1]:
                continue
           stack.append(height)
           if height > maxHeight:
               maxHeight = height
           for j in range(i+1, len(heights)):
                print(stack)
                stack.append(heights[j])
                leastHeight = min(stack)
                stackLen = len(stack)
                currHeight = leastHeight * stackLen
                if currHeight > maxHeight:
                    maxHeight = currHeight
                print(maxHeight)
        return maxHeight
        """
        #Lets try a monotonic stack approach - Greg Hogg Video
        """n = len(heights)
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j 
                a = w*h
                maxArea = max(maxArea, a)
                start = j
            stack.append((height,start))
        while stack:
            h, j = stack.pop()
            w = n-j
            maxArea = max(maxArea, w*h)
        return maxArea"""

    #ok basically loop through the array and then make a stack.
    #In the loop while the current height is less than the top height in the stack we pop the height and we calculate the area using different techs
    
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                index = stack.pop() #gives us the higher ones index
                h = height[index]
                right = i 
                left = stack[-1] if stack else -1
                w = right - left
                a = w*h
                maxArea = max(maxArea, a)
            stack.append(i)

            while stack:
                height.append(-1)

    
if __name__ == "__main__":
    sol = Solution()
    heights = [2,0,2]
    print(sol.largestRectangleArea(heights))

