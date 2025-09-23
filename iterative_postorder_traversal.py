from typing import Optional, List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        #cur = root
        
        #extra visited for postorder compared to inorder and preorder traversals, and also no cur variable this time supposedly simpler
        visit = [False]

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val) #visited twice
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right) #right child first because want to go left first, so left has to be last one added, so first one popped
                    stack.append(cur.left)
                    
                    visit.append(False)
                    visit.append(False)
                    


        return res