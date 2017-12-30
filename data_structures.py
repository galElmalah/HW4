
# exceptions classes
class ValueExistsException(Exception):
    def __init__(self, val):
        super().__init__("Same Value Exists: {}".format(val))

class ValueNotExistsException(Exception):
    def __init__(self, val):
        super().__init__("Value Not Exists: {}".format(val))

class EmptyTreeException(Exception):
    def __init__(self):
        super().__init__("The Tree Is Empty")



# node class
class TreeNode:
    def __init__(self,value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    # interface method with the basic logic
    def insert(self, value):
        if self.value == None:
            self.value = value    
        else:
            self.__insert(value,self)

    # private recursive function that handles the insertion
    def __insert(self, value, node):
        if value < node.value:
            if node.left_child == None:
                node.left_child = TreeNode(value)
                node.left_child.parent = node
            else:
                self.__insert(value,node.left_child)
        elif value > node.value:
            if node.right_child == None:
                node.right_child = TreeNode(value)
                node.right_child.parent = node
            else:
                self.__insert(value,node.right_child)        
        else:
            raise ValueExistsException(value)

# BST class
class BSTree:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, values):
        if type(values) == list or type(values) == tuple :
            for val in values:
                self.root.insert(val)
        else:
            self.root.insert(values)
    
    def search(self, value):
        if self.root == None:
            raise EmptyTreeException()
        tmp = self.root
        while(tmp != None):
            if tmp.value == value:
                return tmp
            if value < tmp.value:
                tmp = tmp.left_child
            else:
                tmp = tmp.right_child
        raise ValueNotExistsException(value)
    
    def inOrder(self):
        arr = []

        def traverse(node):
            if node:
                traverse(node.left_child)
                arr.append(node.value)
                traverse(node.right_child)

        if self.root:
            traverse(self.root)
            return arr
        else:
            raise EmptyTreeException()
    
    def height(self):
        def maxDepth(node):
            if  node is None: 
                return 0
            else:
                # getting the height of all the left sub trees
                left_height = maxDepth(node.left_child)
                # getting the height of all the right sub trees
                right_height= maxDepth(node.right_child)

            return max(left_height,right_height)+1

        tmp = self.root
        if tmp:
            return maxDepth(tmp)
        else:
            raise EmptyTreeException()        
            
            

a = BSTree()
a.insert([1,2,3,4,5,6,7])
a.insert(12)
a.insert(10)
print(a.inOrder())
print(a.height())
    

