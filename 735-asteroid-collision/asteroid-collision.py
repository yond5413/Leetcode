class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []

        for ast in asteroids:
            while ret and ast<0 and ret[-1]>0:
                if abs(ret[-1])<abs(ast):
                    ret.pop(-1)
                elif abs(ret[-1])==abs(ast):
                    ret.pop(-1) 
                    break
                else:
                    break    
            else:
                ret.append(ast)
        return ret