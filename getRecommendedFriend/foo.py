''''
Essentially we are given a integer n representing the subset of individuals 
on a social media application and the goal is provide a simple recommendation system.
We are also given an array friends that provides us with the friends an individual may have. 
Using the friends of each user recommend the most commonly seen between the mutuals
if there is one new to reccomend put -1 in the respecive index instead of reccommending a new one 

return type list/array
-> modified bfs to stop after first level level was done
--> could potenitally have just brute forced with double for loop
'''
def main(n,friends):
    ret = []
    for i in range(n):
        ret.append(bfs(i,friends))
    return ret

def bfs(root,connections):
    ret = -1
    queue = [root]
    visited = set()
    visited.add(root)
    frequency = {}
    ##
    # Goal BFS 
    # root
    # find friends
    # return with highest frequency
    level = 0
    cuttoff = len(connections[root])
    while(len(queue)>0):
        curr = queue.pop(0)
        visited.add(curr)
        for vert in connections[curr]:
            if vert not in visited:
                queue.append(vert)
                #visited.add(vert)
        if level ==cuttoff:
            # empty queue and count frequencies
            print(queue)
            for q in queue:
                    if q not in visited and q not in frequency:
                        frequency[q] = 1
                    elif q not in visited and q in frequency:
                        frequency[q] += 1
            queue = []
        level+=1
    #############
    print(f"visited:{visited}, fre:{frequency}")
    maxi = 0
    for k in frequency.keys():
        curr = frequency[k] 
        if curr>maxi or (curr == maxi and ret>k): 
            ret = k
            maxi = curr
        #elif (curr == maxi and ret>k):
        #    ret = k
    print(ret)
    return ret

if __name__ == '__main__':
    '''
    Person A: [B, C]
    Person B: [A, D, E]
    Person C: [A, D, F]
    Person D: [B, C, E]
    Person E: [B, D, F]
    Person F: [C, E]
    '''
    n = 6 ## number of vertices
    friends = [[1,2],[0,3,4],[0,3,5],[1,2,4],[1,3,5],[2,4]] ### adjacency list 
    correct = [3,2,1,0,2,3]
    ret = main(n,friends)
    if ret == correct:
        print("Correct")
    else:
        print("Incorrect")
        print(correct)
        print(ret)
    ### check if correct 