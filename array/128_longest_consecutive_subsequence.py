# Same as C++, set is unordered so indexing can't be used
# Same approach, in brute force the only difference was that for every element in array
# We used to check if next consecutive exists using Linear Search, which used to take O(N^3) time complexity

class Solution(object):
    def longestConsecutive(self, nums):
        if (len(nums)==0):
            return 0
        longest=1
        st=set(nums)
        for i in st:
            if (i-1 not in st):
                cnt=1
                x=i
                while(x+1 in st):
                    cnt+=1
                    x+=1
                longest=max(longest,cnt)
        return longest

# Time-complexity: O(3N)
# Space-complexity: O(N)