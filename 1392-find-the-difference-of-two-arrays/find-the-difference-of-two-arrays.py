class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        visit1,visit2 = set(nums1),set(nums2)
        ret = []
        curr = []
        for i in nums1:
            if i not in visit2:
                visit2.add(i)
                curr.append(i)
        ret.append(curr)
        curr = []
        for i in nums2:
            if i not in visit1:
                visit1.add(i)
                curr.append(i)
        ret.append(curr)
        return ret