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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def getLength(node):
            if node is None:
                return 0, 0
            l_node_long, l_longest = getLength(node.left)
            r_node_long, r_longest = getLength(node.right)

            new_long = max(l_node_long, r_node_long, l_longest + r_longest)

            return new_long, max(l_longest + 1, r_longest + 1)

        l, ll = getLength(root)
        # gotta deduct one from ll since it is the root
        return max(l, ll - 1)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

