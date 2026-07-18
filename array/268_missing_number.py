# XOR used as xor of same number is zero

class Solution(object):
    def missingNumber(self, nums):
        XOR1=len(nums) #as loop will run from 0 to n-1, and we need to include n
        for i in range(0,len(nums)):
            XOR1=i^nums[i]^XOR1  #do xor with the previous result too
        return XOR1

# Time-complexity: O(N)
# Space-complexity: O(1)