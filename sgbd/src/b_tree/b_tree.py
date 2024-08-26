# /src/b_tree/b_tree.py

from .node import BTreeNode

class BTree:
    def __init__(self, t):
        self.t = t
        self.root = BTreeNode(t, leaf=True)

    def traverse(self, node):
        i = 0
        for i in range(len(node.keys)):
            if not node.is_leaf():
                self.traverse(node.children[i])
            print(node.keys[i], end=' ')
        if not node.is_leaf():
            self.traverse(node.children[i + 1])

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and k == node.keys[i]:
            return node
        elif node.is_leaf():
            return None
        else:
            return self.search(k, node.children[i])

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode(self.t)
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.is_leaf():
            node.keys.append(None)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], k)

    def split_child(self, node, i):
        t = self.t
        y = node.children[i]
        z = BTreeNode(t, y.leaf)
        node.children.insert(i + 1, z)
        node.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]

        if not y.is_leaf():
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t - 1]
