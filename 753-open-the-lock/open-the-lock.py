class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead_set = set(deadends)
        if "0000" in dead_set:
            return -1
        queue = [("0000",0)]
        visited = set(["0000"])
        while queue:
            combo,steps = queue.pop(0)
            if combo == target:
                return steps
            if combo in dead_set:
                continue
            for i in range(len(combo)):
                val = int(combo[i])
                v1 = val+1 if val!=9 else 0
                v2 = val-1 if val!=0 else 9
                paths = [v1,v2]
                for t in paths:
                    curr = combo[:i]+ str(t) + combo[i+1:]
                    if curr not in visited:
                        queue.append((curr,steps+1))
                        visited.add(curr)
        return -1