# 이진 탐색 트리 구현
# http://ejklike.github.io/2018/01/09/traversing-a-binary-tree-1.html

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node


    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

def binary_tree(nodes):
    import collections
    bt = BinarySearchTree()

    for node in nodes:
        if node:
            bt.insert(node)


    queue = collections.deque([bt.root])
    depth = 0

    while queue:
        depth += 1
        print([x.data for x in queue])
        for _ in range(len(queue)):
            v = queue.popleft()
            if v.left and v.left.data:
                queue.append(v.left)
            if v.right and v.right.data:
                queue.append(v.right)

    return depth

print(binary_tree([3, 9, 20, None, None, 15, 7]))