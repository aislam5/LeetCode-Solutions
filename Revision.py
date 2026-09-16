#16th September 2026 - Revised Contains Duplicate, Two Sum, Valid Anagrams, Group Anagrams

from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        my__dict = {}
        for i, nums in enumerate(nums):
            if nums in my__dict.values():
                return False
            else:
                my__dict[i] = nums
        return True
        """
        setNums = set(nums)
        if len(nums) == len(setNums):
            return False
        else:
            return True

    def isAnagram(self, s: str, t:str) -> bool:
        dict_s = {}
        dict_t= {}

        for char in s:
            dict_s[char] = dict_s.get(char,0) +1

        for char in t:
            dict_t[char] = dict_t.get(char, 0) +1

        if dict_t == dict_s:
            return True
        return False

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict ={}

        for i, num in enumerate(nums):
            find = target - num
            if find in my_dict:
                return [i, my_dict[find]]
            else:
                my_dict[find] = i

    def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
        my_dict = defaultdict(list)
        for word in strs:
            wordKey = [0] * 26
            for char in word:
                wordKey[ord(char) - ord('a')] += 1
            my_dict[tuple(wordKey)].append(word)
        return list(my_dict)

    
            
