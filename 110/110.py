from typing import Optional, Union


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNodes:
    def __init__(self, node_list):
        FIFO = list()
        l = node_list.copy()
        self.root = TreeNode(val=l.pop(0))
        FIFO.append(self.root)

        while len(FIFO) > 0:
            cur_node = FIFO.pop(0)
            try:
                v = l.pop(0)
                if v is not None:
                    cur_node.left = TreeNode(val=v)
                    FIFO.append(cur_node.left)
                v = l.pop(0)
                if v is not None:
                    cur_node.right = TreeNode(val=v)
                    FIFO.append(cur_node.right)
            except IndexError:
                break


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        if (root.left is None) and (root.right is None):
            return True

        def check(node):

            if node is None:
                return 0, True

            l_height, l_bal = check(node.left)
            r_height, r_bal = check(node.right)

            if (l_bal == False) or (r_bal == False):
                balanced = False
            else:
                balanced = abs(l_height - r_height) < 2

            return max(l_height, r_height) + 1, balanced

        h, bal = check(root)
        return bal
        


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    t = TreeNodes([1,2,2,3,3,None,None,4,4])
    sol = Solution()
    print(sol.isBalanced(t.root))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
