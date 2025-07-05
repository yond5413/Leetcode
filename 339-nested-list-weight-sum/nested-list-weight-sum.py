# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        The result is undefined if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        The result is undefined if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        ret = 0
        

        for i in range(len(nestedList)):
            print(nestedList[i])
            if nestedList[i].isInteger():
                ret+=nestedList[i].getInteger()
            else:
                new = nestedList[i].getList()
                queue = []
                for n in new:
                    queue.append((n,2))
                #queue = [(nestedList[i].getList(),2)]
                while(queue):
                    curr,depth = queue.pop(0)
                    if curr.isInteger():
                        ret+= curr.getInteger()*depth
                    else:
                        #queue.append((curr.getList(),depth+1)) 
                        new = curr.getList()
                        for n in new:
                            queue.append((n,depth+1))
            
        return ret