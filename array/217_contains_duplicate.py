# Hashing i.e. dictionary is used in map
# Can also use set
# Idea is to basically enter the numbers in dict, if it exists i.e. appears atleast twice, return true
# If not add in dictionary, in the end return False

class Solution(object):
    def containsDuplicate(self, nums):
        dict={}
        for i in nums:
            if i in dict:
                return True
            dict[i]=1
        return False

# Time-complexity: O(n)
# Space-complexity: O(1)