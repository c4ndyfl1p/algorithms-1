# can we represent a contigious tree in an array. And in our head pretend that list/array is a tree.
# Can we then write TREE operations(like: get child, get parent) on the list?

# all return and imput arguments are indices in this file, and not their values.

def root(A):
    """returns the root node index of a list that we are pretending is a contigious tree

    Args:
        A (__list__): list that we are pretending is a tree

    Returns:
        __index__: index of the root node
    """
    return 0

def left_child(A, i):
    l = 2*i + 1
    return l if l<len(A) else i

def right_child(A, i):
    r = 2*i + 2
    return r if r<len(A) else i

def parent(L, i):
    """returns the index of the parent in a list that we are pretending is a tree

    Args:
        L (_list_): _description_
        i (_int_): index of the elemment whos's parent we want

    Returns:
        _int_: index of the parent if parent exists. if root node was the input, returns the root itself
    """
    p = (i - 1)//2
    return p if i>0 else i

#driver code
def __main__():

    L = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"] 
    print(root(L))
    print(left_child(L, 3))
    print(right_child(L, 3))
    print(parent(L, 7))
    print(parent(L, 8))

# __main__()