# Last updated: 6/6/2026, 10:25:10 PM
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        j = 0

        while(i<len(pushed) and j<len(popped)):
            stack.append(pushed[i])
            while(len(stack)!=0 and j < len(popped) and popped[j] == stack[-1]):
                stack.pop()
                j = j + 1
            i = i + 1

        return True if len(stack) == 0 else False
        