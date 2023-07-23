'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ret = False
        # ,rows in increasing order
        ## last element of row i is < first element of row i+1
        ## we can try to use this information to modify binary search
        ### idea before looking at neetcode
        ### use rows to iterate with binary srach but use edges od each row to decide whether to go up or down!!!!!
        ### binary search for rows then binary search for one that fits whar were looking for 
        l, r = 0, len(matrix)-1
        #### this is for the rows
        while(r>=l):
            mid =(r+l)//2
            curr_l,curr_r = l,r
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                print('found the right row')
                break    
            elif matrix[mid][0] >= target:
                print('go lower')
                r = mid-1
            elif  matrix[mid][-1] <= target:
                print('go higher')
                l = mid+1
           
        if target not in matrix[mid]:
            return ret
        
        new_l, new_r = 0,len(matrix[mid])-1
        while(new_l<= new_r):
            mid2 =(new_r+new_l)//2
            print(f"new_l: {new_l},new_r: {new_r}, mid2: {mid2}")
            if matrix[mid][mid2] == target:
                print('found the exact value')
                ret = True
                break    
            elif matrix[mid][mid2] > target:
                print('go lower in row')
                new_r = mid2-1
            elif  matrix[mid][mid2] < target:
                print('go higher in row')
                new_l = mid2+1
        return ret
        