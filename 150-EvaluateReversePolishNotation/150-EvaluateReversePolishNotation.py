# Last updated: 6/16/2026, 9:28:27 PM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        self.stack = []
        res=0
        if len(tokens)<=2:
            return int(tokens[0])

        for i in range(len(tokens)):
            if(tokens[i]=="*" or tokens[i]=="/" or tokens[i]=="+" or tokens[i]=="-"):
                b=self.stack.pop()
                a=self.stack.pop()
                l=tokens[i]
                match l:
                    case "*":
                        res = int(a) * int(b)
                        self.stack.append(res)

                    case "/":
                        res = int(a) / int(b)
                        self.stack.append(res)
                    case "+":
                        res = int(a) + int(b)
                        self.stack.append(res)
                    case "-":
                        res = int(a) - int(b)
                        self.stack.append(res)
            else:
                self.stack.append(tokens[i])
        return int(res)


















