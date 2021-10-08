class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        nodes = [root]
        len_nodes = 1
        while nodes[0]:
            for x in range(len_nodes):
                nodes[x].right = nodes[x + 1] if (x + 1 < len_nodes) else None
            nodes = [node for parent in nodes for node in [parent.left, parent.right]]
            len_nodes *= 2
        return root

root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
sol = Solution()
sol.connect(root)