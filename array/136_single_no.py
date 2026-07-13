# XOR- Bitwise Manipulation
# find the number that only appears once in the array, rest appears twice
# XOR of two same number is 0 and 0^n is n

class Solution(object):
    def singleNumber(self, nums):
        XOR=0
        for i in nums:
            XOR=XOR^i
        return XOR

# Time-complexity: O(N)
# Space-complexity: O(1)