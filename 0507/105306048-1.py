class Solution_H04_P01:

class Solution_H04_P02:

class Solution_H04_P03:
    def insert_new(self,k):


class Solution_H04_P04:

    def minDiddInBST(self,root):
        '''
            :type root :Tree Node
            :rtype: int
        '''
        main = [0,leftNode,rightNode]
        leftNode = [main]
        rightMode = [main]
        for i in root:
             if null:
                pass
             else:
                if i>main[0]:
                    main[0] = i
                else:                  
                    
class BinMinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self,i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

t = BinMinHeap()
t.insert(1)
