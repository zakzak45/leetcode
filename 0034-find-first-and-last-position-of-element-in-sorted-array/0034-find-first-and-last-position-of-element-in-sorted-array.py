class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
            
        result = [-1, -1]
        left = 0
        right = len(nums) - 1
        
        # First occurrence
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result[0] = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        left = 0
        right = len(nums) - 1
        
        # Last occurrence
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                result[1] = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return result
  