// brute force used, using 3 loops
// optimal solution would be to use reverse function, will try later
// rotate right means first take k elements in temp array
// then shift the arr elements in reverse order i.e. go from back
// then copy the temp elements to the beginning of the array

void rotate(int* nums, int numsSize, int k) {
    k=k%numsSize;
    if (k>0){
        int temp[k];
        for (int i=numsSize-k;i<numsSize;i++){
            temp[i-(numsSize-k)]=nums[i];
        }
        for (int i=numsSize-k-1;i>=0;i--){
            nums[i+k]=nums[i];
        }
        for(int i=0;i<k;i++){
            nums[i]=temp[i];
        }
    }
}

// time complexity: O(n+d)
// space complexity: O(d)