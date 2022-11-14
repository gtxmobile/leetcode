from typing import Optional
from . import TreeNode


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    cnt_l = countTree(root.left)
    if cnt_l == k -1:
        return root.val
    elif cnt_l < k-1:
        return kthSmallest(root.right,k-cnt_l-1)
    else:
        return kthSmallest(root.left,k)


def countTree(root):
    if root is None:
        return 0
    else:
        return countTree(root.left)+countTree(root.right)+1