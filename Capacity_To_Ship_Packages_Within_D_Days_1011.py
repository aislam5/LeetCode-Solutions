class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        totalWeight = sum(weights)
        ans =[]
        while left <= right:
            mid = (left+right)//2 #this is our current capacity we need to test
            testWeight = 0
            testDays = 1
            for i, weight in enumerate(weights):
                if testWeight + weight <= mid:
                    testWeight += weight
                else:
                    testWeight = 0
                    testWeight += weight
                    testDays+=1
            if testDays <= days:
                ans.append(mid)
                right = mid - 1
            else:
                left = mid + 1
        return min(ans)

