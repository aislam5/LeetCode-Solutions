#my logic for this is that the end and the front pointer should be the same

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        left = 0
        right = len(filtered_s) - 1
        print(filtered_s)
        while left < right:
            if filtered_s[left] != filtered_s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    test = "A man, a plan, a canal: Panama"
    ans = solution.isPalindrome(test)
    print(ans)
