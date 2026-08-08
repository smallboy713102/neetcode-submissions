class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]  # Return indices if complement is found
            hashmap[nums[i]] = i  # Store index of current number
        
        return []  # Return empty list if no solution found
