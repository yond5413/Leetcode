class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = list(senate)
        #ret = ''
        r_count=d_count=r_ban=d_ban = 0
        ##################
        for s in senate:
            if s =="R":
                r_count+=1
            else:
                d_count+=1
        while(queue):
            curr = queue.pop(0)
            if curr == "R":
                if r_ban>0:
                    r_ban-=1
                else:
                    d_ban+=1
                    queue.append(curr)
            else:
                if d_ban>0:
                    d_ban-=1
                else:
                    r_ban+=1
                    queue.append(curr)
            if r_count<=r_ban:
                return "Dire"
            elif d_count<=d_ban:
                return "Radiant"
        #########################
