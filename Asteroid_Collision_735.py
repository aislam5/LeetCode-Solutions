class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for i, asteroid in enumerate(asteroids):
            toAdd = True
            while stack and asteroid < 0:
                if stack[-1] < 0:
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                    toAdd = True
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    toAdd = False
                    break
                else:
                    toAdd = False
                    break
            if toAdd:
                stack.append(asteroid)
        return stack
