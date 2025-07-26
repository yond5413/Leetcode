class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        i,j = 0,0
        # closed interval 
        # a<= x<=b
        #while i<len(firstList) and j <len(secondList):
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                a = max(firstList[i][0],secondList[j][0])
                b = min(firstList[i][1],secondList[j][1])
                if a<=b:
                    ret.append([a,b])
                

        return ret