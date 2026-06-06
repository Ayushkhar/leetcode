# Last updated: 6/6/2026, 10:24:52 PM
class ProductOfNumbers:
    arr = []
    def __init__(self):
        self.prod = [1]
    def add(self, num: int) -> None:
        if(num == 0):
            self.prod = [1]
        else:
            self.prod.append(self.prod[-1] * num)
 
    def getProduct(self, k: int) -> int:
        return 0 if  k >= len(self.prod) else self.prod[-1] // self.prod[-k-1] 
        