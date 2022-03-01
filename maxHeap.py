# L is a list, but in our imaginatin it's a contigious tree with a MAX heap property.
# What's a max heap? A contigious tree where parents are bigger than children


#add a node while maintaining the heap property
# delete the root/maximum element while maintainting the heap property
from heap import parent, left_child, right_child

def max_heapify_up(Q, c):
    """when a new element is appended at the end of the list/ contigious tree, this 
    function makes sure that the new element obeys the heap property by sifting it upwards till life is great_

    Args:
        Q (_list_): the list(tree) with the max heap property
        c (_int_): the new element which might be problematic because it could be breaking the 
        max heap property and we wanna sift it up till Q is a max heap
    """
    p = parent(Q, c) #get the new elemet's parent
    if Q[c]>Q[p]: # if the new element is problematic i.e the parent is smaller, swap them
        Q[c], Q[p]= Q[p], Q[c]
        max_heapify_up(Q, p) #continue till the root


def insert(Q, x):
    """inserts a element in a list that we are pretending is a tree while maintaining the max heap property

    Args:
        Q (_list_): the list(tree) we want to insert into
        x (_int_): the value of the element we want to insert into the max heap
    """
    Q.append(x) #append to the array/tree
    max_heapify_up(Q, len(Q)-1) #somehow sift it up if breaks the heap property, if not just chill


def max_heapify_down(Q,p):
    l,r = left_child(Q,p), right_child(Q,p)
    c = l if Q[l]>Q[r] else r
    if Q[p]< Q[c]:
        Q[p],Q[c]=Q[c],Q[p]
        max_heapify_down(Q, c)


def delete_max(Q):
    last = len(Q)-1
    Q[0], Q[last] = Q[last], Q[0]
    out = Q.pop()
    max_heapify_down(Q, 0)
    return out

def build_heap(A):
    for i in range(len(A)//2, -1, -1):
        max_heapify_down(A, i)

def __main__():
    L = [18,12,5,7,10,1,4,6,3,8] # this is already a max heap
    print(L)
    insert(L,13 )
    print(L)
    delete_max(L)
    print(L)
    A = [23,4,7,8,9,43,75,25,0]
    build_heap(A)
    print(A)

__main__()