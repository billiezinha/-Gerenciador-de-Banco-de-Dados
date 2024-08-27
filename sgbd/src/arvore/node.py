# /src/b_tree/node.py

class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grau mínimo (t)
        self.leaf = leaf  # Verdadeiro se o nó é uma folha
        self.keys = []  # Lista de chaves
        self.children = []  # Lista de filhos

    def is_leaf(self):
        return self.leaf
