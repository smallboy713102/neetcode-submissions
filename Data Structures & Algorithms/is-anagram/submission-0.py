class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap = {}
        
        for x in range(len(s)):
            if s[x] in hashmap:
                hashmap[s[x]][0] += 1
            else:
                hashmap[s[x]] = [1, 0]
            
            if t[x] in hashmap:
                hashmap[t[x]][1] += 1
            else:
                hashmap[t[x]] = [0, 1] 
        
        for key, counts in hashmap.items():
            if counts[0] != counts[1]:
                return False
        
        return True
