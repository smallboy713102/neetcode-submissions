class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            mp = [0]*26
            for ch in s:
                mp[ord(ch)-ord('a')]+=1
            groups[tuple(mp)].append(s)
        res = []
        for key,value in groups.items():
            res.append(value)
        return res