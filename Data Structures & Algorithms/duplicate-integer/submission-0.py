class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        flag = False
        for x in nums:
            if x not in hashmap: hashmap[x]=1
            else:
                flag = True
                break
        return flag

            