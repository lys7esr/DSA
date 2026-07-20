// GOOGLE ASKED, Optimal solution
// The trick is to only check the consecutive elements if the sequence starts from it
// Like if 102, and 101 exists then dont start checking from 102, later when 101 comes check from there
// But for that also if 100 exists then dont start from 101, start when 100 appears

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int n=nums.size();
        if (n==0){
            return 0;
        }
        int longest=1;
        unordered_set<int> st;
        for (int i=0;i<n;i++){
            st.insert(nums[i]);
        }
        for (auto it:st){
            if (st.find(it-1)==st.end()){
                int cnt=1;
                int x=it;
                while(st.find(x+1)!=st.end()){
                    cnt++;
                    x++;
                }
                longest=max(longest,cnt);
            }
        }
    return longest;    
    }
};

// Time-complexity: O(3N) so basically O(N)
// Space-complexity: O(N)