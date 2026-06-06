# Last updated: 6/6/2026, 10:26:29 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        b = []


        for i in range(len(a) - 1, -1, -1):
            b.append(a[i])

        return ' '.join(b)

