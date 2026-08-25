class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1={}
        mp2={}
        if len(s) != len(t):
            return False
        for x in s:
            if x not in mp1: mp1[x] = 1
            else : mp1[x]+=1
        for x in t:
            if x not in mp2: mp2[x] = 1
            else : mp2[x]+=1
        return mp1 == mp2