In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Input: root = [1,2,3,4], x = 4, y = 3
Output: false

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true

Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def TreeNodeX(self,root,x,depth,parent):
        tree=root
        if tree ==None:
            return
        if tree.val==x:
            return (parent,depth)
        l=None
        r=None
        if tree.left:
            l= self.TreeNodeX(tree.left,x,depth+1,tree)
        if tree.right:
            r = self.TreeNodeX(tree.right,x,depth+1,tree)
        return l if l!=None else r
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        xparent,xdepth=self.TreeNodeX(root,x,0,None)
        yparent,ydepth=self.TreeNodeX(root,y,0,None)
        if xdepth==ydepth:
            if xparent!=yparent:
                return True
        else:
            return False
