# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# what do we want: max depth
# how should we track it?
# option 1: a set of depths, which we take the max of
# option 2: a variable that we compare to and update as needed - less space
# how do we work with the tree we are given?
# we need to explore every node of the tree
# we can do this using recursion
# the recursion can get the depth of the current node
# then call itself onto the next node with the depth + 1
# what is the base case? when we hit a leaf node (no left or right)
# where are we tracking max_depth:
# as a parameter passed into the recursive method
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthRecursive(root, curr_depth, unexplored):
            if root.right == None and root.left == None:
                return curr_depth
            if root.left != None:
                if root.right != None:
                    unexplored.append((root.right, curr_depth + 1))
                return maxDepthRecursive(root.left, curr_depth + 1, unexplored)
            if root.right != None:
                return maxDepthRecursive(root.right, curr_depth + 1, unexplored)
            return -1
        
        if root == None:
            return 0
       
        max_depths = set()
        unexplored = [(root, 1)]

        while len(unexplored) > 0:
            node, depth = unexplored.pop()
            max_depths.add(maxDepthRecursive(node, depth, unexplored))
        
        print(max_depths)
        return max(max_depths)

            
            

        



        