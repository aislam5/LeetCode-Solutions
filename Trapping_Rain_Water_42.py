class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) -1 
        max_right = height[len(height)-1]
        max_left = height[0]
        water = 0
        while left <= right: #basic traversal 
            if max_left < max_right:
                max_left = max(max_left, height[left])
                water += max_left - height[left]
                left += 1
            else:
                max_right = max(max_right, height[right])
                water += max_right - height[right]
                right -= 1
        return water

#ok the understanding itself wasnt that bad.
#we keep track of the left most, right most, and the current position of the left and right counters
#the rest is pretty self explanatory

