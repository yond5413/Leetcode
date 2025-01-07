class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        

        '''
        - may have to sort both slots1 and slots2
        '''
        slots1.sort(key= lambda x: x[0])
        slots2.sort(key= lambda x: x[0])
        i,j = 0,0
        n,m = len(slots1),len(slots2)

        while(i<n and j<m):
            start = max(slots1[i][0],slots2[j][0])
            end = min(slots1[i][1],slots2[j][1])
            if end-start>=duration:
                return [start,start+duration]
            if end ==slots1[i][1]:
                i+=1
            else:
                j+=1 

        return []