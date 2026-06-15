# Last updated: 6/15/2026, 12:45:04 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        arr=[]
4        for i in range(len(s)):
5            if(s[i]=="[" or s[i]=="{" or s[i]=="("):
6                arr.append(s[i])
7            else:
8                if(len(arr)==0):
9                    return False 
10                a = arr.pop()
11                if((s[i]=="]" and a!="[") or (s[i]=="}" and a!="{") or (s[i]==")" and a!="(")):
12                    return False
13               
14        if(len(arr)==0):
15            return True 
16        else:
17            return False 
18
19
20   
21
22        