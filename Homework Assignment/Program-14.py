class Solution:
    def findDuplicate(self, arr):
        low, high = 1, len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            count = 0

            for x in arr:
                if x <= mid:
                    count += 1

            if count > mid:
                high = mid
            else:
                low = mid + 1

        return low



arr=[3,1,4,4,2]
obj=Solution()
res=obj.findDuplicate(arr)
print(res)