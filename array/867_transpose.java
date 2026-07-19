class Solution {
    public int[][] transpose(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[][] ans = new int[n][m];  // as rows and columns are interchanged so n,m size of ans array
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                ans[j][i] = matrix[i][j]; // swap the indices yk
            }
        }
        return ans;
    }
}

// Time-complexity: O(N^2)
// Space-complexity: O(N^2)