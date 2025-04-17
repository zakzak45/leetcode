class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # \U0001f32aï¸ Prepare the battlefield

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue  # \U0001f6ab Skip duplicate blades

            l, r = i + 1, len(nums) - 1  # \U0001f5e1ï¸ Left and right flankers

            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1  # âï¸ Too heavy â retreat right
                elif threesum < 0:
                    l += 1  # âï¸ Too light â advance left
                else:
                    res.append([a, nums[l], nums[r]])  # \U0001f3af Perfect combo!
                    l += 1

                    # \U0001f300 Skip duplicates on the left
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res  # \U0001f525 Return all the successful triple strikes!