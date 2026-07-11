# TWO POINTERS USED
# brute force approach would be to search for all the elements val in nums and store it somewhere else ig
# optimal is to first assign j with the index of first occurence of val
# if no val present in nums, simply return len(nums)
# assign i as the right of j
# if a[i]==val then pass or smt
# if not then swap a[i] and a[j] then increase j
# return j, which represents the number of elements in nums after removing val

class Solution(object):
    def removeElement(self, nums, val):
        j=-1
        for i in range (0, len(nums)):
            if (nums[i]==val):
                j=i
                break
        if (j==-1):
            return len(nums)
        for i in range (j+1,len(nums)):
            if (nums[i]==val):
                i+=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        return j

# Time-complexity: O(n)
# Space-complexity: O(1)
