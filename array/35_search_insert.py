# Binary Search used
# Return low to return the index for the edge cases, trace it yourself for different values

class Solution(object):
    def searchInsert(self, nums, target):
        low=0
        high=len(nums)-1
        while(low<=high):
            mid=(low+high)/2
            if (target==nums[mid]):
                return mid
            elif (target<nums[mid]):
                high=mid-1
            else:
                low=mid+1
        return low

# Time-complexity: O(logn)
# Space-complexity: O(1)