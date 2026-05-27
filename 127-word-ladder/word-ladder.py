from collections import defaultdict 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        
        if endWord not in wordList:
            return 0
        hashmap = defaultdict(list)
        queue = [(beginWord,1)]
        visited = set([beginWord])

        for i in range(len(wordList)):
            for j in range(len(wordList[i])):
                new = wordList[i][:j]+"*"+ wordList[i][j+1:]
                hashmap[new].append(wordList[i])
        
        while (queue):
            word,steps = queue.pop(0)
            if word == endWord:
                return steps
            for i in range(len(word)):
                curr = word[:i] +"*"+word[i+1:]
                if curr in hashmap and curr not in visited:
                    visited.add(curr)
                    for neigh in hashmap[curr]:
                        queue.append((neigh,steps+1))
        return 0