# Last updated: 6/6/2026, 10:25:39 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap=defaultdict(int)

        i=0
        res=0
        for j in range(len(s)):
            count_len =j-i+1
            hashmap[s[j]]+=1
            max_freq=max(hashmap.values())
            # shrinking condition
            if count_len-max_freq>k:
                hashmap[s[i]]-=1
                i+=1
                count_len=j-i+1

            res=max(res,count_len)
        return res


