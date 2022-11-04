class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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