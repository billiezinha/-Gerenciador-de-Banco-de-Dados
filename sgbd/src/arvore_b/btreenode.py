class BTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Grau mínimo
        self.leaf = leaf
        self.keys = []
        self.children = []

    def is_leaf(self):
        return self.leaf
