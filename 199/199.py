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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Go to the right and if there is no right, go to the left node.
        #  terminate at a leaf node.

        #         if not root:
        #             return []

        #         FIFO = list()
        #         FIFO.append((0, root))

        #         vals = list()
        #         temp_list = list()
        #         l = list()
        #         lvl = 0
        #         while len(FIFO) > 0:
        #             cur_lvl, n = FIFO.pop(0)

        #             if n.left:
        #                 FIFO.append((cur_lvl+1, n.left))
        #             if n.right:
        #                 FIFO.append((cur_lvl+1, n.right))

        #             if cur_lvl > lvl:
        #                 l.append(temp_list)
        #                 temp_list = list()
        #                 temp_list.append(n.val)
        #                 lvl += 1
        #             else:
        #                 temp_list.append(n.val)
        #         l.append(temp_list)
        #         ans = [x[-1] for x in l]

        #         return ans

        # Inspiration:
        # https://leetcode.com/problems/binary-tree-right-side-view/discuss/56003/My-C++-solution-modified-preorder-traversal

        ans = list()

        def traverse(node, lvl):
            if not node:
                return
            if lvl > len(ans):
                ans.append(node.val)
            traverse(node.right, lvl + 1)
            traverse(node.left, lvl + 1)

        traverse(root, 1)
        return ans


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    return
