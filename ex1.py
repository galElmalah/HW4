############# part 1 ###############
# part a

inches_to_meters = lambda inches: inches * 0.0254
inches_to_feets = lambda inches: inches * (1 / 12)
miles_to_feets = lambda miles: miles * 5280

# part b
# b.1 composition
composition = lambda f,g: lambda x: f(g(x))
# b.2 opposite
opposite = lambda f: lambda x: x / f(1)


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
from make_class import make_class 


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

class Meters:
    def __init__(self, meters):
        if type(meters) is int or type(meters) is float:
            self.value = float(meters)
        elif type(meters) is str:
            tmp = meters.split(" ")
            if isFloat(tmp[0]) and tmp[1] == "m":
                self.value = float(tmp[0])
            else:
                raise Exception("Format error: {}".format(meters))
        else:
            raise Exception("Type error: {}".format(type(meters)))

    def __str__(self):
        return '{} m'.format(self.value)

    def __repr__(self):
        return 'Meters({})'.format(self.value)

class Inches:
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
  
    __type__ = "Feets"
    return make_class(locals())


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

    __type__ = 'Miles'
    return make_class(locals())

Feets = make_feets_class()
Miles = make_miles_class()
############## helper functions ################

def to_str(obj):
    if isinstance(obj, dict) and 'get' in obj:
        if obj['get']('__type__') in ('Miles','Feets'):
            return obj['get']('__str__')()
    return str(obj)

def to_repr(obj):
    if isinstance(obj, dict) and 'get' in obj:
        if obj['get']('__type__') in ('Miles','Feets'):
            return obj['get']('__repr__')()
    return repr(obj)

def type_of(obj):
    if isinstance(obj, dict) and 'get' in obj:
        if obj['get']('__type__') in ('Miles','Feets'):
            return obj['get']('__type__')
    return type(obj)

#################### Part 3 Generic functions ########################

def type_tag(x):
    return type_tag.tags[type_of(x)]

type_tag.tags = {type_of(Meters(0)):'m',type_of(Inches(0)):'i',type_of(Feets):'ft', type_of(Miles):'mi'}


def apply(operator, obj1, obj2):
    types = (type_tag(obj1), type_tag(obj2))
    if operator == '>' or operator == 'gt':
        operator=('gt', '>')
    if operator == '==' or operator == 'eq':
        operator=('eq', '==')
    key = (operator, types)
    return apply.implementation[key](obj1, obj2)

def greater_classes_shmaython(obj1, obj2):
    #obj1 is the the class 
    if isinstance(obj1, Meters):
        if type_of(obj2)=='Miles':
            return obj1.value > miles_to_meters(obj2['get']('value'))
        if type_of(obj2)=='Feets':
            return obj1.value > feets_to_meters(obj2['get']('value'))
    # Inches is obj1
    elif isinstance(obj1, Inches):
        if type_of(obj2)=='Miles':
            return obj1.value > miles_to_inches(obj2['get']('value'))
        if type_of(obj2)=='Feets':
            return obj1.value > feets_to_inches(obj2['get']('value'))

def equal_classes_shmaython(obj1, obj2):
    #obj1 is the the class 
    if isinstance(obj1, Meters):
        if type_of(obj2)=='Miles':
            return obj1.value == miles_to_meters(obj2['get']('value'))
        if type_of(obj2)=='Feets':
            return obj1.value == feets_to_meters(obj2['get']('value'))
    # Inches is obj1
    elif isinstance(obj1, Inches):
        if type_of(obj2)=='Miles':
            return obj1.value == miles_to_inches(obj2['get']('value'))
        if type_of(obj2)=='Feets':
            return obj1.value == feets_to_inches(obj2['get']('value'))

apply.implementation =  {
    # Meters
    ('add',('m','i')):lambda x,y:Meters(x.value + inches_to_meters(y.value)),
    ('add',('m','m')):lambda x,y:Meters(x.value + y.value),
    ('sub',('m','i')):lambda x,y:Meters(x.value - inches_to_meters(y.value)),
    ('sub',('m','m')):lambda x,y:Meters(x.value - y.value),
    # Inches
    ('add',('i','m')):lambda x,y:Inches(x.value + meters_to_inches(y.value)),
    ('add',('i','in')):lambda x,y:Inches(x.value + y.value),
    ('sub',('i','m')):lambda x,y:Inches(x.value - meters_to_inches(y.value)),
    ('sub',('i','i')):lambda x,y:Inches(x.value - y.value),
    # Miles
    ('add',('mi','ft')):lambda x,y:Miles['new'](x['get']('value') + feets_to_miles(y['get']('value'))),
    ('add',('mi','mi')):lambda x,y:Miles['new'](x['get']('value') + y['get']('value')),
    ('sub',('mi','ft')):lambda x,y:Miles['new'](x['get']('value') - feets_to_miles(y['get']('value'))),
    ('sub',('mi','mi')):lambda x,y:Miles['new'](x['get']('value') - y['get']('value')),
    # Miles
    ('add',('ft','mi')):lambda x,y:Feets['new'](x['get']('value') + miles_to_feets(y['get']('value'))),
    ('add',('ft','ft')):lambda x,y:Feets['new'](x['get']('value') + y['get']('value')),
    ('sub',('ft','mi')):lambda x,y:Feets['new'](x['get']('value') - miles_to_feets(y['get']('value'))),
    ('sub',('ft','ft')):lambda x,y:Feets['new'](x['get']('value') - y['get']('value')),
    # eq == ,gt > operators
    # gt > 
    (('gt','>'),('m','m')):lambda x,y: x.value > y.value,
    (('gt','>'),('m','i')):lambda x,y: x.value > inches_to_meters(y.value),
    (('gt','>'),('i','m')):lambda x,y: inches_to_meters(x.value) > y.value,  
    (('gt','>'),('i','i')):lambda x,y: x.value > y.value,
    (('gt','>'),('mi','mi')):lambda x,y: x['get']('value') > y['get']('value'),
    (('gt','>'),('mi','ft')):lambda x,y: x['get']('value') > feets_to_miles(y['get']('value')),
    (('gt','>'),('ft','mi')):lambda x,y: feets_to_miles(x['get']('value')) > y['get']('value'),
    (('gt','>'),('ft','ft')):lambda x,y: feets_to_miles(x['get']('value')) > feets_to_miles(y['get']('value')), 
    # Mixed      
    (('gt','>'),('m','ft')):greater_classes_shmaython,     
    (('gt','>'),('i','ft')):greater_classes_shmaython, 
    (('gt','>'),('ft','m')):lambda x,y: not greater_classes_shmaython(y,x),     
    (('gt','>'),('ft','i')):lambda x,y: not greater_classes_shmaython(y,x),     
    (('gt','>'),('m','mi')):greater_classes_shmaython,     
    (('gt','>'),('i','mi')):greater_classes_shmaython,      
    (('gt','>'),('mi','m')):lambda x,y: not greater_classes_shmaython(y,x),     
    (('gt','>'),('mi','i')):lambda x,y: not greater_classes_shmaython(y,x),     
    # eq ==
    (('eq','=='),('m','m')):lambda x,y: x.value == y.value,
    (('eq','=='),('m','i')):lambda x,y: x.value == inches_to_meters(y.value),
    (('eq','=='),('i','m')):lambda x,y: inches_to_meters(x.value) == y.value,  
    (('eq','=='),('i','i')):lambda x,y: x.value == y.value,
    (('eq','=='),('mi','mi')):lambda x,y: x['get']('value') == y['get']('value'),
    (('eq','=='),('mi','ft')):lambda x,y: x['get']('value') == feets_to_miles(y['get']('value')),
    (('eq','=='),('ft','mi')):lambda x,y: feets_to_miles(x['get']('value')) == y['get']('value'),
    (('eq','=='),('ft','ft')):lambda x,y: feets_to_miles(x['get']('value')) == feets_to_miles(y['get']('value')), 
      # Mixed  
    (('eq' ,'=='),('m','ft')):equal_classes_shmaython,     
    (('eq','=='),('i','ft')):equal_classes_shmaython,     
    (('eq','=='),('ft','m')):lambda x,y: equal_classes_shmaython(y,x),     
    (('eq','=='),('ft','i')):lambda x,y: equal_classes_shmaython(y,x),     
    (('eq','=='),('m','mi')):equal_classes_shmaython,     
    (('eq','=='),('i','mi')):equal_classes_shmaython,     
    (('eq','=='),('mi','m')):lambda x,y: equal_classes_shmaython(y,x),     
    (('eq','=='),('mi','i')):lambda x,y: equal_classes_shmaython(y,x)  
     
  
    }


def coerce_apply(operator, obj1, obj2):
    if operator =='add':
        obj3 = apply('add', obj1, obj2)
        return apply('add', Meters(0), obj3)     
    elif operator =='sub':
        obj3 = apply('sub', obj1, obj2)
        return apply('sub', Meters(0), obj3)   


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

    def insert(self, obj, node):
        # if the node is empty (root)
        if node == None: node = TreeNode(obj)
        elif apply('==', obj, node.value): raise ValueExistsException(obj)
        # obj.val is bigger meaning -> go to the right
        elif apply('>', obj, node.value): node.right_child = self.insert(obj, node.right_child)
        # obj.val is smaller meaning -> go to the left
        elif not apply('>', obj, node.value): node.left_child = self.insert(obj, node.left_child) 
        return node       

    def height(self, node):
        if node is None:
            return 0
        # getting the height of all the left sub trees
        left_height =self.height(node.left_child)
        # getting the height of all the right sub trees
        right_height=self.height(node.right_child)
        # return the max height plus the current node addition to that height ( +1 )
        return max(left_height,right_height)+1

    def delete(self, obj):
        try:
            node = self.search(self, obj)
        except ValueNotExistsException as e:
            print(e)
            return
        if node:
            # the node have two childrens
            [parent, successor] = node.__Successor(node.right_child)
            if node.left_child and node.right_child:
            
                if parent.left_child == successor:
                    parent.left_child = successor.right_child
                else:
                    parent.right_child = successor.left_child
                
                successor.left_child = node.left_child
                successor.right_child = node.right_child
                
                node = successor
            else:
                # The node have only a left child
                if parent != node:
                    parent.left_child = successor.right_child
                else:
                    parent.right_child = successor.right_child
                




    def search(self,node, obj):
        if node is None:
            raise ValueNotExistsException(obj)  
        if apply('==', node.value, obj): return node
        if apply('>', node.value, obj): return node.search(node.left_child,obj)
        if not apply('>', node.value, obj): return node.search(node.right_child,obj)

    def __Successor(self, parent):
        if self.left_child==None:
            return [parent, self]
        else:
            return self.left_child.__Successor(self)

    def in_order(self, arr):
        if self:
            if self.left_child:
                self.left_child.in_order(arr)
            arr.append(self.value)
            if self.right_child:
                self.right_child.in_order(arr)
            return arr


                
# BST class
class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self, objects):
        if self.root == None:
            self.root = TreeNode(objects[0]) if type(objects) == list or type(objects) == tuple else TreeNode(objects)
            return
        if type(objects) == list or type(objects) == tuple :
            for obj in objects:
                self.root.insert(obj, self.root)
        else:
            self.root.insert(objects, self.root)
    
    def search(self, value):
        if self.root == None:
            raise EmptyTreeException()
        else:
            return self.root.search(self.root,value)
    
    def in_order(self):
        arr = []
        if self.root and self.root.value != None:
            return self.root.in_order(arr)
        else:
            raise EmptyTreeException()
    
    def height(self):
        if self.root.value:
            return self.root.height(self.root)
        else:
            raise EmptyTreeException()     

    def delete(self, obj):
        self.root.delete(obj)   
            


print(apply('add',Meters(1), Inches(1)))            
print(feets_to_meters(1))            



# Driver ##

l = Meters(20)
l2 = Inches(20)


for v in ["25.8 in", "25.8 ft", [], 2555555555555]:
    try:
        print(str(Inches(v)))
    except Exception as e:
        print(e)

f = Feets['new']('25.8 ft')
print(f['get']('__str__')())
print(f['get']('__repr__')())
m = Miles['new']('25.8 mi')
print(m['get']('__str__')())
print(m['get']('__repr__')())
print(to_repr(apply('add', Feets['new'](1.5),Miles['new'](1))))
print("########### operators ############")
print(to_repr(apply('gt',Miles['new'](1),Inches(1.5))))

print(to_repr(apply('gt',Inches(1.5), Miles['new'](1))))

print(to_repr(apply('>',Miles['new'](1),Inches(1.5))))

print(to_repr(apply('>',Inches(1.5), Miles['new'](1))))

print(to_repr(apply('eq',Feets['new'](1),Inches(feets_to_inches(1)))))

print(to_repr(apply('eq',Inches(1.5),Feets['new'](inches_to_feets(1.5)))))

print(to_repr(apply('==', Feets['new'](1), Inches(1.5))))

print(to_repr(apply('==', Inches(1.5), Feets['new'](1))))

print('############ coerce_apply ##########')
print(to_repr(coerce_apply('add',Meters(1.5), Inches(1))))
print(to_repr(coerce_apply('add', Inches(1) ,Meters(1.5))))
print(to_repr(coerce_apply('sub',Meters(1), Inches(1.5))))
print(to_repr(coerce_apply('sub', Inches(1.5) ,Meters(1))))

tree =  BSTree()
print(tree)
tree.insert(Meters(10))
try:
    tree.insert(Meters(10))
except Exception as e:
    print(e)
tree.insert(Meters(11))
tree.insert(Meters(miles_to_meters(1.1)))
tree.insert(Meters(9))
tree.insert(Inches(10))
tree.insert(Feets['new'](10))
tree.insert(Miles['new'](10))
tree.insert(Inches(12))
tree.insert(Feets['new'](15))
tree.insert(Miles['new'](1))
tree.insert(Inches(5))
tree.insert(Feets['new'](0.1))
## testing search function
print("#### search function ####")
print(tree.search(Meters(11)).value)
print(tree.search(Inches(12)).value)
print(tree.search(Meters(11)).value)
print(tree.search(Meters(miles_to_meters(1.1))).value)
print(tree.search(Meters(9)).value)
print(tree.search(Inches(10)).value)
print(tree.search(Feets['new'](10)).value['get']('__str__')())
print(tree.search(Miles['new'](10)).value['get']('__str__')())
print(tree.search(Inches(12)).value)
print(tree.search(Feets['new'](15)).value['get']('__str__')())
print(tree.search(Miles['new'](1)).value['get']('__str__')())
print(tree.search(Inches(5)).value)
print(tree.search(Feets['new'](0.1)).value['get']('__str__')())
print('-- in order print after insert ------------------------------')
for v in tree.in_order():
    if (isinstance(v, dict)):
        print(v['get']('__str__')())
    else:
        print(v)

print('-- in order print after delete ------------------------------')
# tree.delete(Meters(11))
# tree.delete(Meters(miles_to_meters(1.1)))
# tree.delete(Meters(9))
# tree.delete(Inches(10))
# tree.delete(Feets['new'](10))
# tree.delete(Miles['new'](10))
# tree.delete(Inches(12))
# tree.delete(Feets['new'](15))
# tree.delete(Miles['new'](1))
# tree.delete(Inches(5))
# tree.delete(Feets['new'](0.1))
# print(tree.height())

try:
    for v in tree.in_order():
        if (isinstance(v, dict)):
            print(v['get']('__str__')())
        else:
            print(v)
except Exception as e:
    print(e)
print(tree.height())