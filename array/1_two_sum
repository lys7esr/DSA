# HASHING is used, for only telling yes or no, one can sort and use two pointers i.e. iterate
# Here, the approach is to subtract the element with the target, if the remaining is in dict or map
# Then you found the solution else add the element in the dict along with its index

class Solution(object):
    def twoSum(self, nums, target):
        dict={}
        for i in range (0,len(nums)):
            a=nums[i]
            more=target-a
            if more in dict:  # if (mpp.find(more)!=mpp.end()) for C++
                return [dict[more],i]
            dict[a]=i

# Time-complexity: O(N)
# Space-complexity: O(N), worst case