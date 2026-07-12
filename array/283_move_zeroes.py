# TWO-POINTER APPROACH
# similar to one already did before, point j to first occurence
# if doesnt exist simply return nums, else check i from j+1
# swap numbers and increase j

class Solution(object):
    def moveZeroes(self, nums):
        j=-1
        for i in range(0,len(nums)):
            if (nums[i]==0):
                j=i
                break #need to break, else last 0 index will be assigned to j
        if (j==-1):
            return nums
        for i in range (j+1,len(nums)):
            #if (nums[i]==0): #don't need this as i will obviously increase on its own through loop
                #i+=1
            if (nums[i]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                j+=1

# Time-complexity: O(n)
# Space-complexity: O(1)