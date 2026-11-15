from collections import deque

class Solution:
    def maxSlidingWindow(self, nums:list[int], k:int) -> list[int]:
        dq = deque()
        ans = []

        for right, num in enumerate(nums):

            #if the incoming next number is greater than or equal to the number at the top of the deque then we pop 
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(right)

            #remove the front if outside window value 
            if dq[0] < right - k + 1:
                dq.popleft()

            #Recording the maximum once the first window of size k is formed 
            if right >= k - 1:
                ans.append(nums[dq[0]])

