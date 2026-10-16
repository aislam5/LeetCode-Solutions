class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        i, j = 0, len(people) - 1
        boats = 0
        people.sort()
        #right side with most weigth left one with least weight 
        while i <= j:
            if people[i] + people[j] <= limit:
                i+=1
            j-=1
            boats+=1
"""
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit: j -= 1
            i += 1
        return i

    #ok so first we sort the aray and put the pointers at each end 
    
                
"""