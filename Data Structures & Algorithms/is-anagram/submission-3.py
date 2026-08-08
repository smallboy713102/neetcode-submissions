class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1,hashmap2={},{}
        for x in s:
            if x not in hashmap1: hashmap1[x] = 1

            else : hashmap1[x] +=1

        for y in t:
            if y not in hashmap2: hashmap2[y] = 1
            else : hashmap2[y] +=1

        return hashmap1 == hashmap2