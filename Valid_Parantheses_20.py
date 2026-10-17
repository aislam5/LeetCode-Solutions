class Solution:
    def isValid(self, s: str) -> bool:
        """
        ok for this problem what I have in mind is we traverse the string and if we see a open bracket ( { [ we will add it to the stack if we see a closing bracket we shall pop the open bracket from the stack to see if the open and closing brackets match
        """
        hashmap = {')':'(' , ']':'[' , '}':'{'} # so with this hasmap it will make it easier to write the code we have the closing brackets as the key and the values as the opening brackets 
        stack = []

        for char in s:  #looping trhough the string 
            if char not in hashmap:
                stack.append(char)
            else:
                if not stack: #if our stack is Empty
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[char]:
                        return False 
        return not stack #this checks if the stack is empty by the end meaning there are not open brackets left behind
1