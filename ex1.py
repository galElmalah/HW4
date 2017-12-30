############# part 1 ###############
# part a

inches_to_meters=lambda inches: inches * 0.0254
inches_to_feets= lambda inches: inches * (1 / 12)
miles_to_feets=lambda miles: miles * 5280

# part b
# b.1 composition
def composition(f, g): return lambda x: f(g(x))
# b.2 opposite
def opposite(f): return lambda x: x / f(1)


# part c
meters_to_inches = opposite(inches_to_meters)
miles_to_inches = composition(miles_to_feets, opposite(inches_to_feets))
feets_to_inches = opposite(inches_to_feets)
miles_to_meters = composition(miles_to_inches, opposite(meters_to_inches))
feets_to_miles = opposite(miles_to_feets)
feets_to_meters = composition(feets_to_inches,inches_to_meters)
meters_to_miles = opposite(miles_to_meters)
inches_to_miles = opposite(miles_to_inches)
meters_to_feets = opposite(feets_to_meters)
# Examples
# print(inches_to_meters(10))
# print(feets_to_inches(10))
# print(miles_to_inches(10))

############################### part 2 ################################
from make_class import make_class as cls


def isFloat(string):
    """
    helper function thats try to convert a string to a floating point number
    string:  str
    return value: true/false
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


class Meters(object):

    def __init__(self, meters):
        if type(meters) is int or type(meters) is float:
            self.value = float(meters)
        elif type(meters) is str:
            tmp = meters.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "m"):
                self.value = float(tmp[0])
            else:
                raise Exception("Format error: {}".format(meters))
        else:
            raise Exception("Type error: {}".format(type(meters)))

    def __str__(self):
        return '{} m'.format(self.value)

    def __repr__(self):
        return 'Meters({})'.format(self.value)

    def __type__(self):
        return 'Meters'

class Inches(object):

    def __init__(self, inches):
        if type(inches) is int or type(inches) is float:
            self.value = float(inches)
        elif type(inches) is str:
            tmp = inches.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "in"):
                self.value = float(tmp[0])
            else:
                raise Exception("Format error: {}".format(inches))
        else:
            raise Exception("Type error: {}".format(type(inches)))

    def __str__(self):
        return '{} in'.format(self.value)

    def __repr__(self):
        return 'Inches({})'.format(self.value)


def make_feets_class():
    def __init__(self, feets):
        if type(feets) is int or type(feets) is float:
            self['set']('value', float(feets))
        elif type(feets) is str:
            tmp = feets.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "ft"):
                self['set']('value', float(tmp[0]))
            else:
                raise Exception("Format error: {}".format(feets))
        else:
            raise Exception("Type error: {}".format(type(feets)))

    def __str__(self):
        return '{} ft'.format(self['get']('value'))

    def __repr__(self):
        return 'Feets[\'new\']({})'.format(self['get']('value'))

    return cls(locals())


def make_miles_class():
    def __init__(self, miles):
        if type(miles) is int or type(miles) is float:
            self['set']('value', float(miles))
        elif type(miles) is str:
            tmp = miles.split(" ")
            if(isFloat(tmp[0]) and tmp[1] == "mi"):
                self['set']('value', float(tmp[0]))
            else:
                raise Exception("Format error: {}".format(miles))
        else:
            raise Exception("Type error: {}".format(type(miles)))

    def __str__(self):
        return '{} mi'.format(self['get']('value'))

    def __repr__(self):
        return 'miles[\'new\']({})'.format(self['get']('value'))

    return cls(locals())

############## helper functions ################


def to_str(obj):
    if isinstance(obj, dict):
        return obj['get']('__str__')()
    return str(obj)

def to_repr(obj):
    if isinstance(obj, dict):
        return obj['get']('__repr__')()
    return repr(obj)

def type_of(obj):
    if isinstance(obj, dict):
        return obj['get']('__type__')
    return type(obj)


#################### Part 3 Generic functions ########################


def apply(operator, obj1, obj2):
    if operator == 'add':  
        if isinstance(obj1, Meters):
            if not isinstance(obj2, dict):
                return Meters(obj1.value + inches_to_meters(obj2.value)) if isinstance(obj2, Inches) else Meters(obj1.value + obj2.value)
            if type_of(obj2)=='Miles':
                return Meters(obj1.value + miles_to_meters(obj2['get']('value')))
            if type_of(obj2)=='Feets':
                return Meters(obj1.value + feets_to_meters(obj2['get']('value')))
        # Inches is obj1
        elif isinstance(obj1, Inches):
            if not isinstance(obj2, dict):
                return Inches(obj1.value + meters_to_inches(obj2.value)) if isinstance(obj2, Meters) else Inches(obj1.value + obj2.value)
            if type_of(obj2)=='Miles':
                return Inches(obj1.value + miles_to_inches(obj2['get']('value')))
            if type_of(obj2)=='Feets':
                return Inches(obj1.value + feets_to_inches(obj2['get']('value')))
        # Miles is obj1
        elif type_of(obj1) == 'Miles':
            if isinstance(obj2, dict):
                return Miles['new'](obj1['get']('value') + feets_to_miles(obj2['get']('value'))) if type_of(obj2)=='Feets' else Miles['new'](obj1['get']('value') + obj2['get']('value'))
            if isinstance(obj2, Meters):
                return Miles['new'](obj1['get']('value') + meters_to_miles(obj2.value))
            if isinstance(obj2, Inches):
                return Miles['new'](obj1['get']('value') + inches_to_miles(obj2.value))
        # Feets is obj1
        elif type_of(obj1) == 'Feets':
            if isinstance(obj2, dict):
                return Feets['new'](obj1['get']('value') + miles_to_feets(obj2['get']('value'))) if type_of(obj2)=='Miles' else Feets['new'](obj1['get']('value') + obj2['get']('value'))
            if isinstance(obj2, Meters):
                return Feets['new'](obj1['get']('value') + meters_to_feets(obj2.value))
            if isinstance(obj2, Inches):
                return Feets['new'](obj1['get']('value') + inches_to_feets(obj2.value))
    elif operator=='sub':
        if isinstance(obj1, Meters):
            if not isinstance(obj2, dict):
                return Meters(obj1.value - inches_to_meters(obj2.value)) if isinstance(obj2, Inches) else Meters(obj1.value - obj2.value)
            if type_of(obj2)=='Miles':
                return Meters(obj1.value - miles_to_meters(obj2['get']('value')))
            if type_of(obj2)=='Feets':
                return Meters(obj1.value - feets_to_meters(obj2['get']('value')))
        # Inches is obj1
        elif isinstance(obj1, Inches):
            if not isinstance(obj2, dict):
                return Inches(obj1.value - meters_to_inches(obj2.value)) if isinstance(obj2, Meters) else Inches(obj1.value - obj2.value)
            if type_of(obj2)=='Miles':
                return Inches(obj1.value - miles_to_inches(obj2['get']('value')))
            if type_of(obj2)=='Feets':
                return Inches(obj1.value - feets_to_inches(obj2['get']('value')))
        # Miles is obj1
        elif type_of(obj1) == 'Miles':
            if isinstance(obj2, dict):
                return Miles['new'](obj1['get']('value') - feets_to_miles(obj2['get']('value'))) if type_of(obj2)=='Feets' else Miles['new'](obj1['get']('value') - obj2['get']('value'))
            if isinstance(obj2, Meters):
                return Miles['new'](obj1['get']('value') - meters_to_miles(obj2.value))
            if isinstance(obj2, Inches):
                return Miles['new'](obj1['get']('value') - inches_to_miles(obj2.value))
        # Feets is obj1
        elif type_of(obj1) == 'Feets':
            if isinstance(obj2, dict):
                return Feets['new'](obj1['get']('value') - miles_to_feets(obj2['get']('value'))) if type_of(obj2)=='Miles' else Feets['new'](obj1['get']('value') - obj2['get']('value'))
            if isinstance(obj2, Meters):
                return Feets['new'](obj1['get']('value') - meters_to_feets(obj2.value))
            if isinstance(obj2, Inches):
                return Feets['new'](obj1['get']('value') - inches_to_feets(obj2.value))
    elif operator == '>' or operator == 'gt' or operator == '==' or operator == 'eq':
        if operator =='>' or operator=='gt':
            # Meters is obj1
            if isinstance(obj1, Meters):
                if not isinstance(obj2, dict):
                    return obj1.value > inches_to_meters(obj2.value) if isinstance(obj2, Inches) else obj1.value > obj2.value
                if type_of(obj2)=='Miles':
                    return obj1.value > miles_to_meters(obj2['get']('value'))
                if type_of(obj2)=='Feets':
                    return obj1.value > feets_to_meters(obj2['get']('value'))
            # Inches is obj1
            elif isinstance(obj1, Inches):
                if not isinstance(obj2, dict):
                    return obj1.value > meters_to_inches(obj2.value) if isinstance(obj2, Meters) else obj1.value > obj2.value
                if type_of(obj2)=='Miles':
                    return obj1.value > miles_to_inches(obj2['get']('value'))
                if type_of(obj2)=='Feets':
                    return obj1.value > feets_to_inches(obj2['get']('value'))
            # Miles is obj1
            elif type_of(obj1) == 'Miles':
                if isinstance(obj2, dict):
                    return obj1['get']('value') > feets_to_miles(obj2['get']('value')) if type_of(obj2)=='Feets' else obj1['get']('value') > obj2['get']('value')
                if isinstance(obj2, Meters):
                    return obj1['get']('value') > meters_to_miles(obj2.value)
                if isinstance(obj2, Inches):
                    return obj1['get']('value') > inches_to_miles(obj2.value)
            # Feets is obj1
            elif type_of(obj1) == 'Feets':
                if isinstance(obj2, dict):
                    return obj1['get']('value') > miles_to_feets(obj2['get']('value')) if type_of(obj2)=='Miles' else obj1['get']('value') > obj2['get']('value')
                if isinstance(obj2, Meters):
                    return obj1['get']('value') > meters_to_feets(obj2.value)
                if isinstance(obj2, Inches):
                    return obj1['get']('value') > inches_to_feets(obj2.value)
        ## equality operator ##
        elif operator =='==' or operator=='eq':
            # Meters is obj1
            if isinstance(obj1, Meters):
                if not isinstance(obj2, dict):
                    return obj1.value == inches_to_meters(obj2.value) if isinstance(obj2, Inches) else obj1.value == obj2.value
                if type_of(obj2)=='Miles':
                    return obj1.value == miles_to_meters(obj2['get']('value'))
                if type_of(obj2)=='Feets':
                    return obj1.value == feets_to_meters(obj2['get']('value'))
            # Inches is obj1
            elif isinstance(obj1, Inches):
                if not isinstance(obj2, dict):
                    return obj1.value == meters_to_inches(obj2.value) if isinstance(obj2, Meters) else obj1.value == obj2.value
                if type_of(obj2)=='Miles':
                    return obj1.value == miles_to_inches(obj2['get']('value'))
                if type_of(obj2)=='Feets':
                    return obj1.value == feets_to_inches(obj2['get']('value'))
            # Miles is obj1
            elif type_of(obj1) == 'Miles':
                if isinstance(obj2, dict):
                    return obj1['get']('value') == feets_to_miles(obj2['get']('value')) if type_of(obj2)=='Feets' else obj1['get']('value') == obj2['get']('value')
                if isinstance(obj2, Meters):
                    return obj1['get']('value') == meters_to_miles(obj2.value)
                if isinstance(obj2, Inches):
                    return obj1['get']('value') == inches_to_miles(obj2.value)
            # Feets is obj1
            elif type_of(obj1) == 'Feets':
                if isinstance(obj2, dict):
                    return obj1['get']('value') == miles_to_feets(obj2['get']('value')) if type_of(obj2)=='Miles' else obj1['get']('value') == obj2['get']('value')
                if isinstance(obj2, Meters):
                    return obj1['get']('value') == meters_to_feets(obj2.value)
                if isinstance(obj2, Inches):
                    return obj1['get']('value') == inches_to_feets(obj2.value)

def coerce_apply(operator, obj1, obj2):
    if operator =='add':
        obj3 = apply('add', obj1, obj2)
        return apply('add', Meters(0), obj3)     
    elif operator =='sub':
        obj3 = apply('sub', obj1, obj2)
        return apply('sub', Meters(0), obj3)   

print(coerce_apply('add',Meters(1.5), Inches(1)))
print(coerce_apply('add', Inches(1) ,Meters(1.5)))
print(coerce_apply('sub',Meters(1), Inches(1.5)))
print(coerce_apply('sub', Inches(1.5) ,Meters(1)))
################### Part 4 Recursiv Data Structures and Exceptions #################


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
    def insert(self, obj):
        if self.value == None:
            self.value = obj   
        else:
            self.__insert(obj,self)

    # private recursive function that handles the insertion
    def __insert(self, obj, node):
        if apply('==', obj, node.value):
            raise ValueExistsException(obj)
        elif not apply('>', obj, node.value):
            if node.left_child == None:
                node.left_child = TreeNode(obj)
                node.left_child.parent = node
            else:
                self.__insert(obj,node.left_child)
        elif apply('>', obj, node.value):
            if node.right_child == None:
                node.right_child = TreeNode(obj)
                node.right_child.parent = node
            else:
                self.__insert(obj,node.right_child)        
      

    def delete(self, obj):
        pass
    def __delete(self, obj):
        tmp = search(obj)
        if tmp:
            # Case 1: the node we are trying to delete is a leaf
            if tmp.left_child == None  and tmp.right_child == None:
                if tmp.parent.left_child == tmp:
                    tmp.parent.left_child = None
                else:
                    tmp.parent.right_child = None
            # Case 2: the node we are trying to delete have a single child
            if tmp.left_child == None or tmp.right_child == None:
                # if he is a left child
                if tmp.parent.left_child == tmp:
                    # the parent node will now point to the child of the node we are deleting 
                    if tmp.left_child is not None:
                        tmp.parent.left_child = tmp.left_child
                    else:
                        tmp.parent.left_child = tmp.right_child
                # else he is a right child
                else:
                    if tmp.left_child is not None:
                        tmp.parent.right_child = tmp.left_child
                    else:
                        tmp.parent.right_child = tmp.right_child                    


                
                

# BST class
class BSTree:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, objects):
        if type(objects) == list or type(objects) == tuple :
            for obj in objects:
                self.root.insert(obj)
        else:
            self.root.insert(objects)
    
    def search(self, value):
        if self.root == None:
            raise EmptyTreeException()
        tmp = self.root
        while(tmp != None):
            if apply('==', tmp.value, value):
                return tmp
            if not apply('>', tmp.value, value):
                tmp = tmp.left_child
            else:
                tmp = tmp.right_child
        raise ValueNotExistsException(value)
    
    def in_order(self):
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
            

Feets = make_feets_class()
Feets['set']('__type__', 'Feets')

Miles = make_miles_class()
Miles['set']('__type__', 'Miles')
print(apply('add',Meters(1), Feets['new'](1)))            
print(feets_to_meters(1))            


tree =  BSTree()
print(tree)
tree.insert(Meters(10))
try:
    tree.insert(Meters(10))
except Exception as e:
    print(e)
tree.insert(Inches(10))
tree.insert(Feets['new'](10))
tree.insert(Miles['new'](10))
print(tree)
print(tree.in_order())
print('-- in order print after insert ------------------------------')
for v in tree.in_order():
    if (isinstance(v, dict)):
        print(v['get']('__str__')(), end=" = ")
    else:
        print(v, end=" = ")
    print(apply('add', Meters(0), v))
print(tree.search(Meters(10)))

## Driver ##

# l = Meters(20)
# l2 = Inches(20)
# print(l)

# for v in ["25.8 in", "25.8 ft", [], 4]:
#     try:
#         print(str(Inches(v)))
#     except Exception as e:
#         print(e)

# f = Feets['new']('25.8 ft')
# print(f['get']('__str__')())
# print(f['get']('__repr__')())

# m = Miles['new']('25.8 mi')
# print(m['get']('__str__')())
# print(m['get']('__repr__')())
# print(to_repr(apply('add', Feets['new'](1.5),Miles['new'](1))))
# print("########### operators ############")
# print(to_repr(apply('gt',Miles['new'](1),Inches(1.5))))

# print(to_repr(apply('gt',Inches(1.5), Miles['new'](1))))

# print(to_repr(apply('>',Miles['new'](1),Inches(1.5))))

# print(to_repr(apply('>',Inches(1.5), Miles['new'](1))))

# print(to_repr(apply('eq',Feets['new'](1),Inches(feets_to_inches(1)))))

# print(to_repr(apply('eq',Inches(1.5),Feets['new'](inches_to_feets(1.5)))))

# print(to_repr(apply('==', Feets['new'](1), Inches(1.5))))

# print(to_repr(apply('==', Inches(1.5), Feets['new'](1))))


