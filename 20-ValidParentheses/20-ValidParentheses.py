# Last updated: 6/16/2026, 9:29:05 PM
class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if(s[i]=="[" or s[i]=="{" or s[i]=="("):
                arr.append(s[i])
            else:
                if(len(arr)==0):
                    return False 
                a = arr.pop()
                if((s[i]=="]" and a!="[") or (s[i]=="}" and a!="{") or (s[i]==")" and a!="(")):
                    return False
               
        if(len(arr)==0):
            return True 
        else:
            return False 


   

        