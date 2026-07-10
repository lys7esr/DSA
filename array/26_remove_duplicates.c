// brute force approach can be to use set data structures, as set contains unique elements
// two-pointers approach
// first elemet is obviously unique, start from second element
// if a[j]!=a[i], then move a[j] to i++, j always increment

int removeDuplicates(int* nums, int numsSize) {
    int i=0;
    for (int j=1;j<numsSize;j++){
        if (nums[i]!=nums[j]){
            i++;
            nums[i]=nums[j];
        }
    }
    return i+1;   
}

// time complexity: O(n)
// space complexity: O(1)