class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            a = nums[i]

            # skip duplicate a
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if a > 0:
                break

            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # skip duplicate values
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif threeSum > 0:
                    r -= 1

                else:
                    l += 1

        return res