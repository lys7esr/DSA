# TWO-POINTERS and SORTING used

class Solution(object):
    def intersect(self, nums1, nums2):
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        res=[]
        i=0
        j=0
        while(i<len(nums1) and j<len(nums2)):
            if (nums1[i]==nums2[j]):
                res.append(nums1[i])
                i+=1
                j+=1
            elif(nums1[i]>nums2[j]):
                j+=1
            else:
                i+=1
        return res

# Time-complexity: O(NlogN)+O(MlogM)
# Space-complexity: O(1)

# Use HASHING
# For repetition allowed, keep reducing the freq and if freq>0 then only append in the result else no need

class Solution(object):
    def intersect(self, nums1, nums2):
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        res=[]
        for i in nums2:
            if i in freq.keys() and freq[i]>0:
                res.append(i)
                freq[i]-=1
        return res

# Time-complexity: O(N+M)
# Space-complexity: O(N)