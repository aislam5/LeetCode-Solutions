class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """#new approach
        stringDict = {}
        maxSubString = 0

        for i, char in enumerate(s):
            j = i
            tempChar = char
            while tempChar not in stringDict:
                stringDict[tempChar] = j
                j += 1
                if j <= len(s) - 1:
                    tempChar = s[j]
            subString = j - i
            if subString > maxSubString:
                maxSubString = subString
            stringDict.clear()
        return maxSubString"""

    #Problem with my Solution is that it has too many moving pieces and therefore takes a lot of time to run

        left = 0 
        stringDict = {}
        result = 0

        for right, char in enumerate(s):
            while char in stringDict:
                del stringDict[s[left]]
                left += 1
            stringDict[char] = right
            result = max(result, right-left + 1)
        return result


