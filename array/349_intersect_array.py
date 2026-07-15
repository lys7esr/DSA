# Two-pointers, sorting and last variable used, easy only

class Solution(object):
    def intersection(self, nums1, nums2):
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        last=None
        res=[]
        i,j=0,0
        while(i<len(nums1) and j<len(nums2)):
            if (nums1[i]<nums2[j]):
                i+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                if (nums1[i]!=last):
                    res.append(nums1[i])
                    last=nums1[i]
                i+=1
                j+=1
        return res

# Time-complexity: O(NlogN+MlogM)
# Space-complexity: O(1)

# HASHING used
# If present in map, then add to result and remove from dictionary else nothing 
class Solution(object):
    def intersection(self, nums1, nums2):
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in nums2:
            if i in freq:
                res.append(i)
                freq.pop(i)  # return value as pop is used but not required
                # can also use del freq(i), doesnt return value:)
        return res

# Time-complexity: O(N+M)
# Space-complexity: O(N)