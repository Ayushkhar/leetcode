# Last updated: 6/6/2026, 10:27:26 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs)==0:
        #     return ""
        # strs=sorted(strs,key=len)
        prfx =strs[0]
        # a=[]
        for i in range(1,len(strs)):
            while prfx not in strs[i][:len(prfx)]:
                prfx=prfx[0:len(prfx)-1]
                
            # if prfx in strs[i][:len(prfx)]:
            #     a.append(prfx)
        return prfx

