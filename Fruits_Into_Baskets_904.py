from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        maxFruit = 0
        fruity = defaultdict(int)

        for right, fruit in enumerate(fruits):
            fruity[fruit] += 1
            while len(fruity) > 2:
                left_fruit = fruits[left]
                fruity[left_fruit] -= 1
                if fruity[left_fruit] == 0:
                    del fruity[left_fruit]
                left += 1
            maxFruit = max(maxFruit, right - left + 1)
        return maxFruit