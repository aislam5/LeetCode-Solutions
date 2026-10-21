class Solution:
    def generateParenthesis(self, n:int) -> list[str]:
        ans, sol = [], []
        #ans will be the final thing we return 
        #sol will be each solution

        def backtrack(open, close):
            #check if solution has been reached
            if len(sol) == 2*n: 
                ans.append(''.join(sol))
                return

            if open < n:
                sol.append('(')
                backtrack(open+1, close)
                sol.pop()

            if open > close:
                sol.append(')')
                backtrack(open, close+1)
                sol.pop()

        backtrack(0,0)
        return ans

if __name__ == "__main__":
    sol = Solution()
    answer = sol.generateParenthesis(3)
    print(answer)