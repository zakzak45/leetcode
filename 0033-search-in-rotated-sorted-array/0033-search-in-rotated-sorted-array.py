class Solution:
    def pivotIndex(self, arr, l, r):
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            else:
                r = mid
        return r

    def binarySearch(self, arr, l, r, target):
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    def search(self, arr, target):
        n = len(arr)
        pivot_index = self.pivotIndex(arr, 0, n - 1)
        idx = self.binarySearch(arr, 0, pivot_index - 1, target)
        if idx != -1:
            return idx
        return self.binarySearch(arr, pivot_index, n - 1, target)