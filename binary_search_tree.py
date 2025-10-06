from queue_array import Queue


class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:

    def __init__(self):
        # Returns empty BST
        self.root = None

    def is_empty(self):
        # returns True if tree is empty, else False
        return self.root is None

    def search_helper(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self.search_helper(node.left, key)
        else:
            return self.search_helper(node.right, key)

    def search(self, key):
        # returns True if key is in a node of the tree, else False
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.search_helper(self.root, key)


    def insert_helper(self, node, key, data):
        if node is None:
            return TreeNode(key, data)
        if key == node.key:
            node.data = data
        elif key < node.key:
            node.left = self.insert_helper(node.left, key, data)
        else:
            node.right = self.insert_helper(node.right, key, data)
        return node

    def insert(self, key, data=None):
        # inserts new node w/ key and data
        # If an item with the given key is already in the BST,
        # the data in the tree will be replaced with the new data
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        self.root = self.insert_helper(self.root, key, data)

    def find_min_helper(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node.key, node.data
        else:
            return self.find_min_helper(node.left)

    def find_min(self):
        # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.find_min_helper(self.root)

    def find_max_helper(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node.key, node.data
        else:
            return self.find_max_helper(node.right)

    def find_max(self):
        # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        return self.find_max_helper(self.root)

    def tree_height_helper(self, node):
        if node is None:
            return -1
        else:
            left_height = self.tree_height_helper(node.left)
            right_height = self.tree_height_helper(node.right)
            return max(left_height, right_height) + 1

    def tree_height(self):  # return the height of the tree
        # returns None if tree is empty
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        if self.root is None:
            return None
        return self.tree_height_helper(self.root)

    def inorder_helper(self, node, result):
        if node:
            self.inorder_helper(node.left, result)
            result.append(node.key)
            self.inorder_helper(node.right, result)

    def inorder_list(self):
        # return Python list of BST keys representing in-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        result = []
        self.inorder_helper(self.root, result)
        return result

    def preorder_helper(self, node, result):
        if node:
            result.append(node.key)
            self.preorder_helper(node.left, result)
            self.preorder_helper(node.right, result)

    def preorder_list(self):
        # return Python list of BST keys representing pre-order traversal of BST
        # DON'T use a default list parameter
        # This method MUST BE RECURSIVE. Hint: add a recursive helper method
        result = []
        self.preorder_helper(self.root, result)
        return result

    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        # DON'T attempt to use recursion
        if self.root is None:
            return []

        result = []
        q = Queue(25000)
        q.enqueue(self.root)

        while not q.is_empty():
            node = q.dequeue()
            result.append(node.key)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return result

        

