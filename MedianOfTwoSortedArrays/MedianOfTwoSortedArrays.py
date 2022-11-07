'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 
'''
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        ret = 0.0
        merged = list()
        ####################
        for i in nums1:
            merged.append(i)
        for i in nums2:
            merged.append(i)
        ####################
        merged.sort()
        '''built in but there many sorting algorithims just my apporach '''
        ####################
        if len(merged) %2 != 0:
            midpoint = int(len(merged)/2 )
            ret = merged[midpoint]
        else:
            mid1= int((len(merged)/2)-1)
            mid2 = mid1 + 1
            ret = float((merged[mid1] + merged[mid2])/2)
            print("else statement mid1 and mid2 are " +str(mid1) +" "+str(mid2) )

        return ret