class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        answer = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if j == i:
                    pass
                else:
                    result = result * nums[j]
            answer.append(result)
        return answer
        """
        #Answer above is O(n^2) so therefore not fulfilling the requirements of the question

        ans = [1] * len(nums)
        pre = 1
        for i in range(len(nums)):
            ans[i] = pre
            pre = pre *nums[i] 

        post = 1
        for i in range(len(nums)-1, -1, -1): 
            ans[i] = ans[i] * post
            post = post * nums[i]

        return ans



