"""class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        #so the first ideas I have right now are I need a way to calculate something to determine if the car meets before or at the target 
        # (target-position) / speed - and we see the seconds to reach the target
        #if the time reached of car 1 is less than car 2 and car 2 pos is ahead of car 1 then we can add them to a fleet

        #ok just had an idea to make a dict of pos and speed
        #then we sort the dict and then it becomes a little easier
        stack = []
        fleets = []
        mydict = {}
        for i in range(len(position)):
            mydict[position[i]] = speed[i]
        sortedDict = dict(sorted(mydict.items()))
        print(sortedDict)
        #now that the dictionary is made we loop through the dic and then check if a positioned car in the back takes the same time as a car in the front 
        for pos, spe in sortedDict.items():
            #we calculate the time to reach target and we append that time to the stack if the time to reach target of current is < time to reach target of top of stack then we pop out of the stack and we add a fleet 
            time = (target - pos)/spe
            toAdd=[]
            while stack and time < stack[-1]:
                toAdd.append(stack.pop())
            stack.append(time)
            if toAdd:
                fleets.append(toAdd)
        print("before last call: ")
        print(fleets)

        while stack:
            toAdd.append(stack.pop())
        fleets.append(toAdd)
        print(fleets)
        return len(fleets)


if __name__ == "__main__":
    sol = Solution()
    target = 10
    position = [0,4,2]
    speed = [2,1,3]
    ans = sol.carFleet(target, position, speed)
    print(ans)`

#ok so there is an extra layer to this which I didnt catch at all 
#time is almost over so go pray and then do this later if u find time in the day or postpone it till tomorrow"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack:
                stack.append(dist / vel)
            elif dist / vel > stack[-1]:
                stack.append(dist / vel)
        return len(stack)