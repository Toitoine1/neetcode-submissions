# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def aux(root: Optional[TreeNode]) -> tuple[int,int] :
            if root == None :
                return (-1001,-1001)
            lmax, lbranch = aux(root.left)
            rmax, rbranch = aux(root.right)
            sum_max_path_rooted_here = max(lbranch + rbranch,lbranch, rbranch, 0) + root.val
            sum_max_branch_rooted_here = max(lbranch, rbranch, 0) + root.val
            return(max(sum_max_path_rooted_here, rmax, lmax), sum_max_branch_rooted_here)
        return aux(root)[0]
