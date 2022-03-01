# Given a list A of n numbers, sort it using a priority queue.
L = [1,5,3,4,2,8,9,10,6,7]

#A queue is a structure with a first in first out policy.
# A priority queue is a structure with a max element gets out first policy


def insert(Q, x):
    """Function to insert just 1 element into a priority que, in a sorted order.
        This is essentially insertion sort. this function has a complexity of log(n).
        Called n times in the mian function it will be n log (n)

    Args:
        Q (_list_): _the priority queu itself_
        x (_int_): _the value of the element that has to be inseted_
    """
    Q.append(x) #add the element
    i = len(Q)-1 #get the last element, that we just inserted, and not sure if it is in order
    while i>0 and Q[i]<Q[i-1]: #check if it is in order, if it is not in order:
        Q[i], Q[i-1]= Q[i-1], Q[i] # swap to put in order
        i = i-1 #keep going back till the entire queue is in order

def del_max(Q):
    """deletes the max valur from the queu and gives it

    Args:
        Q (the priority queue): _description_

    Returns:
        int: max val
    """
    return Q.pop()
    

# print(L.pop(0))

def pqsort(A):
    Q = []
    for x in A:
        insert(Q,x)
    print(f"priority queue: {Q}")    
    for i in range(len(A)):
        A[len(A)-1-i]= del_max(Q) 
        

pqsort(L)
print(L)