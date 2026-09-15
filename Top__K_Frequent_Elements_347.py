import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        #loop through array and make a hashmap with the key = number in array and the value being the amount of times we see it
        #then using heapq.nlargest we find the kth most frequent elements
        my_dict = {}
        for key in nums:    
            my_dict[key] = my_dict.get(key, 0) + 1
        kMostFreq = heapq.nlargest(k, my_dict, key = my_dict.get)
        return kMostFreq
    #Alternate Solutions and making a hashmap and then sorting it by the value and then returning the kth most frequent
    #Another Solution is that you make a hashmap and then based on that you make a list in a list [[],[],[],...] making it so
    #that the most frequent element is at the bottom of the list and then just output the bottom of the list
    def topKFrequentSecond(self, nums: list[int], k: int) -> list[int]:
        my_dict= {}
        answer = []
        frequency = [[] for _ in range(len(nums)+1)]
        for key in nums:
            my_dict[key] = my_dict.get(key,0) + 1

        for key, val in my_dict.items():
            frequency[val].append(key)

        for i in range(len(frequency)-1, 0, -1):    #this goes in reverse for frequency
            for j in frequency[i]:                  # this loops through the each element at index i 
                answer.append(j)                  
                if k == len(answer):                # if the answer list is as long as k
                    return answer                   #just return the answer
        return []


