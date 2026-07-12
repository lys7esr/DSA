# Take two variables, one to store the max count and other to count the max consecutive ones

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxi=0
        count=0
        for i in nums:
            if (i==1):
                count+=1
                maxi=max(count,maxi)
            else:
                count=0
        return maxi

# Time-complexity: O(N)
# Space-complexity: O(1)