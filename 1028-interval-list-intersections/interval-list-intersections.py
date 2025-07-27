class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        i,j = 0,0
        m,n = len(firstList),len(secondList)
        while i<m and j<n:
            a = max(firstList[i][0],secondList[j][0])
            b = min(firstList[i][1],secondList[j][1])
            if a<= b:
                ret.append([a,b])
            if firstList[i][1] > secondList[j][1]:
                j+=1
            else:
                i+=1
        return ret