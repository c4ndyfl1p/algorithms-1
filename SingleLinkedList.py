class Node:
    """
    A node takes in the value and the next node(optional).
    Default for next is None(removed this)
    """
    def __init__(self, value):
        self.value = value
        self.next = None
               
    def __str__(self):
        
        return str(self.value)

class LinkedList:
    """
    1. YOu can declare a linked list with a list of nodes


    Contains nodes and operations to make stay true to a linked list property
    """
    def __init__(self,nodes=None):
        # self.head will point to a Node() object
        self.head = None           
            

        if nodes:            
            self.head = Node(value=nodes.pop(0))
            currNode = self.head                
            for element in nodes:                
                currNode.next = Node(value=element)
                currNode = currNode.next       

    def __str__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(str(node.value))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        # iterate using built in dunerstring to make this mroe pythonic
        #we could have user a traverse() as well
        node = self.head
        while node:
            yield node
            node = node.next
        

node1 = Node(42)
list1 = LinkedList()
list1.head = node1

node3 = Node("Wed")

node2 = Node("Tue")

node1.next = node2  #we are giving the address of the next node object




print(list1)
print(list1.head)

#the __iter__ to iterate over the node
#we are tring to make LinkedList() be the actual list. indead of holding
#individulaa Node() objects in an array. So instead of list = [array1,array2],
#we want to replicate this behaviour
for node in list1:
    print(node)

list2 = LinkedList(nodes=["Mon","Tue", "Wed"])
print(list2)

# for node in list2:
#     print(node)