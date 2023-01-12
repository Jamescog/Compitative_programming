"""
Question Statement
===================================
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
====================================
Time complexity
====================================
Push and empty --> O(1)
Pop and Peek ---> O(n)
Overall ---> O(n)
====================================
Space complexity
====================================
O(n)
====================================
Approach
===================================
Queue using two stacks
"""
class MyQueue:
    def __init__(self):
        # stack to implement push
        self.stack1 = []
        # stack to implement pop and peek
        self.stack2 = []

    def push(self, x: int) -> None:
        # add element to stack1
        self.stack1.append(x)

    def pop(self) -> int:
        # Implement pop
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
        # Implement peek
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        # Check if the queue is empty
        return not self.stack1 and not self.stack2



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
