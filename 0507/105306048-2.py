class bst:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    def insert(self,data):
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left = bst(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = bst(data)
                else: 
                    self.right.insert(data)
        else:
            self.data = data

    def printTreeInorder(self):
        if self.left:
            self.left.printTreeInorder()
        print(self.data,end=" ")
        if self.right:
            self.right.printTreeInorder()

    def printTreePostorder(self):
        if self.left:
            self.left.printTreePostorder()
        if self.right:
            self.right.printTreePostorder()
        print(self.data,end=" ")


class Solution_H04_P01:
    root = bst(4)
    for i in [2,1,3,6,5]:
        root.insert(i)
    root.printTreeInorder()
    print()
class Solution_H04_P02:
    root = bst(4)
    for i in [2,1,3,6,5]:
        root.insert(i)
    root.printTreePostorder()
class Solution_H04_P03:



class Solution_H04_P04:

    def minDiffInBST(self,root):
        '''
            :type root :Tree Node
            :rtype: int
        '''
        ans = 0
        diff = 0
        tree = []
        def traversal(root):
            if root:
                traversal(root.left)
                tree.append(root.val)
                traversal(root.right)
        traversal(root)
        for i in range(len(tree)-1):
            diff = abs(tree[i] - tree[i+1])
            if ans == 0:
                ans = diff
            else:
                ans = min(ans,diff)
        return ans

