# Given an array arr[]. The task is to find the largest element and return it.
class Solution:
    def largestinarray(self, arr):
        max=0
        for i in arr:
            if max<i: max=i
        return max
obj=Solution()
arr = [1, 8, 7, 56, 90]
res=obj.largestinarray(arr)
print(res)