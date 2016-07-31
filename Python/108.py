class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        len_nums = len(nums)
        root_position = len_nums / 2
        root = TreeNode(nums[root_position])
        if root_position == 0:
            left = None
        else:
            left = self.sortedArrayToBST(nums[:root_position])
        if root_position == (len_nums - 1):
            right = None
        else:
            right = self.sortedArrayToBST(nums[(root_position + 1):])
        root.left = left
        root.right = right
        return root
