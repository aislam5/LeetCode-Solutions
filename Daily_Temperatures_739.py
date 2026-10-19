from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        result = [0] * len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[-1]] < temp[i]:
                index = stack.pop()
                daysWait = i - index
                result[index] = daysWait
            stack.append(i)
        return result

        """
        res = [0] * len(temp)
        stack = []
            for i in len(temp):
                while stack and temp[i] > temp[stack[-1]]:
                    index = stack.pop()
                    add = i - index
                    res[index] = add
                stack.append(i)
            return res 
        """
