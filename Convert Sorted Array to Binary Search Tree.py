# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        def buildBST(nums, start, end):
            if(start==end):
                return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = buildBST(nums, start, mid)
            node.right = buildBST(nums, mid+1, end)
            return node
            
        return buildBST(nums, 0, len(nums))
            
