"""
Question statement
===========================================
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

MyCircularDeque(int k) Initializes the deque with a maximum size of k.
boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
boolean isEmpty() Returns true if the deque is empty, or false otherwise.
boolean isFull() Returns true if the deque is full, or false otherwise.
===========================================================================
Time complexity
===========================================================================
__init__ has time complexity of O(n)

Any other functions(methods) has time complexity of O(1)
===========================================================================
Space complexity
============================================================================
O(n)
============================================================================
Approach
=============================================================================
Deque using Python3
"""
class MyCircularDeque:
    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = k
        self.q = [0] * k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.capacity
        self.q[self.head] = value
        self.size += 1
        return True
    
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        return True
    
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
    
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.capacity
        self.size -= 1
        return True
    
    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[self.head]
    
    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.tail - 1) % self.capacity]
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def isFull(self) -> bool:
        return self.size == self.capacity
