class Solution(object):
    def transpose(self, matrix):     
        m=len(matrix)
        n=len(matrix[0])
        A=[[0]*m for _ in range(n)]  #to assign nested listed to A and assign each row element as 0
        for i in range (0,m):
            for j in range(0,n):
                A[j][i]=matrix[i][j] #cause in logic we are using assignment operator, to use it need to have initial value
        return A
    
# Time-complexity: O(N^2)
# Space-complexity: O(N^2)