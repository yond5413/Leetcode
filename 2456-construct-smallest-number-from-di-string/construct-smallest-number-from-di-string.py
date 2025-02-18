class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ret = []
        #visited = set()
        stack = []
        for i in range(len(pattern)+1):
            stack.append(str(i+1))
            while stack and(i == len(pattern) or pattern[i] == "I"):
                ret.append(stack.pop(-1))
        return "".join(ret)