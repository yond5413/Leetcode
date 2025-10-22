class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = n
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[0] ==0:
                if (len(flowerbed)>1 and flowerbed[i+1]!=1) or len(flowerbed) ==1:
                    count-=1
                    flowerbed[i] = 1
            elif i == len(flowerbed)-1 and flowerbed[i] == 0:
                if len(flowerbed)>1 and flowerbed[i-1]!=1:
                    count-=1
                    flowerbed[i] = 1
            elif flowerbed[i] == 0 and len(flowerbed)>3:
                if flowerbed[i-1] != 1 and flowerbed[i+1]!=1:
                    flowerbed[i] = 1
                    count-=1
        print(f"count:{count},flower:{flowerbed}")
        return count<= 0