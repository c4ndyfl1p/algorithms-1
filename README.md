1. Singly Linked Lists
2. Doubly Linked List
3. pqSprt - sorts a list using a priotity queue. 
insert() just appends to the queue. del_max() looks for the biggest element and extracts it.
Sorting algorithm used is selection sort. Bad bad

4. pqSortBetter.py - sorts a list using a priority queue. Sorting algorithm used is insertion sort. Better.
    - insert() inserts stuff into a empty list(we call it a priority queue) in a sorted order. At each insert this sorted order is maintained.
    - del_max() just takes out the last element coz the priority queue is already sorted, and the last element is going to be the maximum.

Conclusion: depending on how the priority queue is implemented we can have different time complexities.
Priority queue is the data structure/ insert() and del_max() are the interface. How we actually implement them is the algorithm.
This separation helps because if in future a new algorithm is developed, we can just replace it and everything will still work just fine.

5. Heaps: # can we represent a contigious tree in an array. And in our head pretend that list/array is a tree.
 Can we then write TREE operations(like: get child, get parent) on the list?

6. MaxHeap: can we now impose a max heap property on the list that we are pretending is actually a tree? 