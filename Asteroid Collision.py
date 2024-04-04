class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for each in asteroids:
            while(stack and each<0 and stack[-1]>0):
                if stack[-1]==-each:
                    stack.pop()
                    break
                elif stack[-1]>-each:
                    break
                else:
                    stack.pop()
            else:
                stack.append(each)
            
        return stack
