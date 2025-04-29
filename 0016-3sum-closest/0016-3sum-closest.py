class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2] # initialize closest sum
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right: # two-pointer approach
                sum = nums[i] + nums[left] + nums[right]
                if sum == target: # sum equals target, return immediately
                    return sum
                elif sum < target:
                    left += 1
                else:
                    right -= 1
                if abs(sum - target) < abs(closest_sum - target): # update closest sum
                    closest_sum = sum
        return closest_sum
