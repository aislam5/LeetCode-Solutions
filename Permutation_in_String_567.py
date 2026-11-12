import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #ok so bascially if we has a string of 2 ab then the given things could be ab or ba 
        #what I think I am doing is maybe making combinations of the string and then checking if the other string one of those combinations in it
        left = 0 
        app = dict.fromkeys(string.ascii_lowercase, 0)
        for i, char in enumerate(s1):
            app[char] += 1
        windowSize = len(s1)

        currApp = dict.fromkeys(string.ascii_lowercase, 0)
        for right, char in enumerate(s2):
            while (right - left + 1) > windowSize:
                currApp[s2[left]] -= 1
                left += 1
            currApp[char] += 1
            if currApp == app:
                return True
        return False
