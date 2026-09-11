class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #loop through both and make 2 separate dictionaries
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in s:
            if s_dict.get(i) == None:
                s_dict[i] = 1
            else:
                currentNum = s_dict.get(i)
                s_dict[i] = currentNum+1
        for j in t:
            if t_dict.get(j) == None:
                t_dict[j] = 1
            else:
                currentNum = t_dict.get(j)
                t_dict[j] = currentNum +1

        #check if the dictionaries are equal
        if s_dict != t_dict:
            return False
        return True

    """
        better way of looping is 
        for i in s:
            s_dict[i] = s_dict.get(i, 0) + 1 - this basically checks if the key value pair exists or not and
            based on that it either gets the value and adds 1 or it makes a new pair with a value of 0 and adds 1
        
    """
        
            