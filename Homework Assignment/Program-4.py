#  Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array. 
class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k-1]
obj=Solution()
arr=[1,3,6,2,7,9,4,2]
k=5
result=obj.kthSmallest(arr,k)
print(result)