class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(0,len(nums)):
            complement = target - nums[i];
            if nums[i] not in mp:
                mp[complement] = i
            else:
                return [mp[nums[i]], i]