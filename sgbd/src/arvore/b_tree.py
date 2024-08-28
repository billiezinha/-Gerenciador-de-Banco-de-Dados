import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grau mínimo
        self.leaf = leaf
        self.keys = []
        self.children = []

    def is_leaf(self):
        return self.leaf

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t, True)
        self.t = t

    def is_leaf(self, node):
        return node.is_leaf()

    def traverse(self, node):
        if node is not None:
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
            temp.children.append(root)
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
        z = BTreeNode(t, y.is_leaf())
        node.children.insert(i + 1, z)
        node.keys.insert(i, y.keys[t - 1])

        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]

        if not y.is_leaf():
            z.children = y.children[t:(2 * t)]
            y.children = y.children[0:t]

    def delete(self, k, node=None):
        if node is None:
            node = self.root

        idx = self._find_key(node, k)

        if idx < len(node.keys) and node.keys[idx] == k:
            if node.is_leaf():
                node.keys.pop(idx)
            else:
                self._delete_internal_node(node, k, idx)
        else:
            if node.is_leaf():
                return  # O k não está presente na árvore
            flag = (idx == len(node.keys))

            if len(node.children[idx].keys) < self.t:
                self._fill(node, idx)

            if flag and idx > len(node.keys):
                self.delete(k, node.children[idx - 1])
            else:
                self.delete(k, node.children[idx])

    def _find_key(self, node, k):
        idx = 0
        while idx < len(node.keys) and node.keys[idx] < k:
            idx += 1
        return idx

    def _delete_internal_node(self, node, k, idx):
        if len(node.children[idx].keys) >= self.t:
            pred = self._get_predecessor(node, idx)
            node.keys[idx] = pred
            self.delete(pred, node.children[idx])
        elif len(node.children[idx + 1].keys) >= self.t:
            succ = self._get_successor(node, idx)
            node.keys[idx] = succ
            self.delete(succ, node.children[idx + 1])
        else:
            self._merge(node, idx)
            self.delete(k, node.children[idx])

    def _get_predecessor(self, node, idx):
        current = node.children[idx]
        while not current.is_leaf():
            current = current.children[-1]
        return current.keys[-1]

    def _get_successor(self, node, idx):
        current = node.children[idx + 1]
        while not current.is_leaf():
            current = current.children[0]
        return current.keys[0]

    def _fill(self, node, idx):
        if idx != 0 and len(node.children[idx - 1].keys) >= self.t:
            self._borrow_from_prev(node, idx)
        elif idx != len(node.keys) and len(node.children[idx + 1].keys) >= self.t:
            self._borrow_from_next(node, idx)
        else:
            if idx != len(node.keys):
                self._merge(node, idx)
            else:
                self._merge(node, idx - 1)

    def _borrow_from_prev(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx - 1]

        child.keys.insert(0, node.keys[idx - 1])
        if not child.is_leaf():
            child.children.insert(0, sibling.children.pop())

        node.keys[idx - 1] = sibling.keys.pop()

    def _borrow_from_next(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])
        if not child.is_leaf():
            child.children.append(sibling.children.pop(0))

        node.keys[idx] = sibling.keys.pop(0)

    def _merge(self, node, idx):
        child = node.children[idx]
        sibling = node.children[idx + 1]

        child.keys.append(node.keys[idx])

        child.keys.extend(sibling.keys)
        if not child.is_leaf():
            child.children.extend(sibling.children)

        node.keys.pop(idx)
        node.children.pop(idx + 1)

        if node == self.root and len(node.keys) == 0:
            self.root = child
