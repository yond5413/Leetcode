class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # start -> "0000"
        if "0000" in deadends:
            return -1
        queue = [("0000",0)]
        visited = set(["0000"])
        while queue:
            combo,steps = queue.pop(0)
            if combo == target:
                #probably
                return steps 
            if combo in deadends:
                continue
            for i in range(len(combo)):
                val = int(combo[i])
                v1 = val+1 if val!=9 else 0
                v2 = val-1 if val!=0 else 9
                turns = [v1,v2]
                for t in turns:
                    path = combo[:i]+str(t)+combo[i+1:]
                    if path not in visited:
                        queue.append((path,steps+1))
                        visited.add(path)
        return -1