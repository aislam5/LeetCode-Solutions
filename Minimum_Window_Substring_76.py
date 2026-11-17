from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #
        left = 0 

        required = defaultdict(int)
        found = defaultdict(int)

        formed = 0 #how many required things are formed 
        ans = (float("inf"),0,0) #tuple with 3 values


        for char in t:
            required[char] += 1
        unique_keys = len(required) #unique keys 



        for right, char in enumerate(s):
            found[char] += 1
            if char in required and found[char] == required[char]:
                formed += 1

            while formed == unique_keys:
                if right-left+1 < ans[0]:
                    ans = (right -left +1, left, right)
                left_char = s[left]
                found[left_char] -= 1
                if left_char in required and found[left_char] < required[left_char]:
                    formed -= 1
                left += 1
            
        if ans[0] == float("inf"):
            return ""

        else: 
            return s[ans[1]: ans[2] + 1] #slicing the string to show the shortest len

