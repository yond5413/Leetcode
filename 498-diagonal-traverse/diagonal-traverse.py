class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m,n = len(mat),len(mat[0])
        ret = []
        diag = True
        i,j = 0,0
        while(len(ret)<m*n):
            if diag:
                while i>=0 and j<n:
                    ret.append(mat[i][j])
                    i-=1
                    j+=1
                if j == n:
                    j -= 1
                    i +=2
                else:
                    i+=1
                diag = False
            else:
                while i<m and j>=0:
                    ret.append(mat[i][j])
                    i+=1
                    j-=1
                if i == m:
                    i -= 1
                    j+=2
                else:
                    j+=1
                diag = True
        return ret