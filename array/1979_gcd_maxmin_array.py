# Daily Challenge: 18/07/26
# Recursion used for gcd and in built method to find min and max of an array

def gcd(a,b): # to define a function make it global and not inside class else we need to use self and other things yk
    if (b==0):
        return a
    return gcd(b,a%b)
class Solution(object):
    def findGCD(self, nums):
        mini=min(nums)
        maxi=max(nums)
        res=gcd(mini,maxi)
        return res

# Time-complexity: O(1)
# Space-complexity: O(1)