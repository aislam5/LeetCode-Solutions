from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        #make all hashamps and then compare 
        my_dict = defaultdict(list)
        for word in strs:
            count = [0]*26 #make a array every word 
            for char in word:
                count[ord(char)-ord('a')] += 1 #the stuff inside the square brackets gives us the index for the letter using ASCII values
            my_dict[tuple(count)].append(word) #we make count a tuple since a lsit is not a hashable object
        return list(my_dict.values())

    #Second Solution we will sort all the words in the list and then make entries of them in the dict
    def groupAnagramsSecond(self, strs: list[str]) -> list[list[str]]:
        for word in strs:
            return 


if __name__ == "__main__" :
    solution = Solution()
    test = ["eat","tea","tan","ate","nat","bat"]
    hi = solution.groupAnagrams(test)
    print(hi)


