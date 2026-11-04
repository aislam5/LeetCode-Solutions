class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        #so basically we need a rate of eating bananas so that all the bananas get eaten
        #now we basically need a binary search for this and I dont know where I am supposed
        #to implement the binary search
        #So basically we have to calculate the speed and the suggested hours, if the suggested hours are less than the actual hour than it is a valid speed

        low = 1 #lowest speed
        high = max(piles) #highest speed
        viableRate = []

        while low <= high :
            mid = (low + high) // 2 #middle speed
            totalHours = 0
            for i, pile in enumerate(piles):
                totalHours += ((pile+mid-1)//mid) #this way of divising ensures if there is remainder it is rounded up instead of being truncated
            if totalHours <= h:
                viableRate.append(mid)
                high = mid - 1
            else:
                low = mid + 1
        return min(viableRate)