from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        maxFreq = 0
        maxLength = 0
        counts = defaultdict(int)

        for right, char in enumerate(s):
            counts[char] += 1
            maxFreq = max(maxFreq, counts[char])

            # Shrink window if replacements needed exceed k
            while (right - left + 1) - maxFreq > k:
                counts[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength

#default dict allows us to have defaul values so no Key Errors are thrown 