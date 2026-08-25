class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for x in nums:
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] += 1

        arr = []

        for key in hashmap:
            arr.append((hashmap[key], key))

        arr.sort(reverse=True)

        res = []

        for i in range(k):
            res.append(arr[i][1])

        return res