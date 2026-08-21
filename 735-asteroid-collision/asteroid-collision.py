class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ret = []
        for ast in asteroids:
            while ret and ret[-1]>0 and ast<0:
                if abs(ast)>ret[-1]:
                    ret.pop(-1)
                elif abs(ast)==ret[-1]:
                    ret.pop(-1)
                    break
                else:
                    break
            else:
                ret.append(ast)
        return ret