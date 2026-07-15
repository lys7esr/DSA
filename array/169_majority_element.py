# MOORE'S VOTING ALGO
# Imagine the flow, you are takig first element considering it as majority, but if someone else comes you subtract count
# Else, you add count
# If count becomes zero, it means that particular element is not majority
# So, you take the next element in array as major
# In this question, it was given that always exist majority, but if not
# Then you need a loop to check if it exists, can use a variable to count its occurence
# If cnt1>n/2, then thats the major element else the major element doesnt exist

class Solution(object):
    def majorityElement(self, nums):
        count=0
        for i in range (0,len(nums)):
            if (count==0):
                ele=nums[i]
                count=1
            elif (ele==nums[i]):
                count+=1
            else:
                count-=1
        return ele

# Time-complexity: O(N)
# Space-complexity: O(1)