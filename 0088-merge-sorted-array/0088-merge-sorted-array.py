class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Start merging from the end of both arrays
        while n > 0:  # We will keep merging until all elements of nums2 are placed
            if m <= 0 or nums2[n-1] >= nums1[m-1]:  
                nums1[m + n - 1] = nums2[n-1]  # Place the larger element from nums2
                n -= 1  # Decrease the index for nums2
            else:
                nums1[m + n - 1] = nums1[m-1]  # Place the larger element from nums1
                m -= 1  # Decrease the index for nums1
