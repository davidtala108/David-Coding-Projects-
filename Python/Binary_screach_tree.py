class TreeNode:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def find(self,key):
        if self.is_empty():
            return False
        return self.find_helper(self.root,key)
    def find_helper(self,root,key):
        if root == None:
            return False
        elif root.key == key:
            return True
        elif root.key > key:
            return self.find_helper(root.left, key)
        elif root.key < key:
            return self.find_helper(root.right, key)

    def find_min(self):
        if self.is_empty():
            return False
        return self.find_min_helper(self.root)

    def find_min_helper(self,min):
        if min.left == None:
            return min.key
        else:
           return  self.find_min_helper(min.left)

    def find_max(self):
        if self.is_empty():
            return False
        return self.find_max_helper(self.root)
    def find_max_helper(self, max):
        if max.right == None:
            return max.key
        else:
            return self.find_max_helper(max.right)
    def insert(self,key):
        N = TreeNode(key)
        if self.is_empty():
            self.root = N
        else:
            return self.insert_helper(self.root, N)
    def insert_helper(self,root, Node):
        if root == None:
            root = Node
        elif root.key != Node.key:
            if root.key > Node.key:
                if root.left == None:
                    root.left = Node
                else:
                    self.insert_helper(root.left, Node)
            elif root.key < Node.key:
                if root.right == None:
                    root.right = Node
                else:
                    self.insert_helper(root.right, Node)
    def delete(self, key):
        self.delete_helper(self.root,key)
    def delete_helper(self, root, key, prev = None, d = None):
        if root.key == key:
            temp = root
            if root.right != None:
                root = root.right
                while root.left != None:
                    root = root.left
                temp.key = root.key
                temp.right = root.right
                root = temp
            elif root.left!= None:
                root = root.left
                while root.right != None:
                    root = root.right
                temp.key = root.key
                temp.left = root.left
                root = temp
            else:
                if prev != None and d == 1:
                    prev.right = root.right
                elif prev != None and d == 0:
                    prev.left = root.left
                else:
                    self.root = None

        else:
            if root.key > key:
                self.delete_helper(root.left, key, root,0)
            elif root.key < key:
                self.delete_helper(root.right, key, root,1)
    def print_tree(self):
        #indorder
        if self.is_empty():
            return []
        Final_list = []
        self.print_tree_helper(self.root,Final_list)
        return Final_list
    def print_tree_helper(self, root, list):
        if root.left != None:
            self.print_tree_helper(root.left,list)
        list.append(root.key)
        if root.right !=None:
            self.print_tree_helper(root.right,list)
    def is_empty(self):
        return self.root == None
    def inorder_print_tree(self,key):
        if self.find(key) == False:
            return []
        Final_list = []
        root = self.Located(self.root,key)
        self.inorder_print_tree_helper(root,Final_list)
        return Final_list

    def inorder_print_tree_helper(self,root,list):
            if root.left != None:
                self.inorder_print_tree_helper(root.left, list)
            list.append(root.key)
            if root.right != None:
                self.inorder_print_tree_helper(root.right, list)
    def Located(self,root,key):
        if root.key == key:
           return root
        elif root.key > key:
            return self.Located(root.left, key)
        elif root.key < key:
            return self.Located(root.right, key)
    def print_levels(self):
        if self.is_empty():
            return []
        Final_Level =[]
        self. print_levels_helper(self.root, Final_Level)
        return Final_Level
    def print_levels_helper(self, root,Final_Level, count = 0):
        if root.left != None:
            self.print_levels_helper(root.left,Final_Level,count+1)
        Final_Level.append([root.key, count])
        if root.right != None:
            self.print_levels_helper(root.right, Final_Level, count + 1)
