class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.capacity
    
    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.stack.append(value)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()
    
    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

# Test the Stack class
if __name__ == '__main__':
    stack = Stack(5)
    
    print("Is stack empty?", stack.is_empty())  # True
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    
    print("Is stack full?", stack.is_full())  # True
    print("Top element:", stack.top())  # 5
    
    print("Popped element:", stack.pop())  # 5
    print("Top element after pop:", stack.top())  # 4
    print("Is stack full after pop?", stack.is_full())  # False
    
    # Uncommenting the following line will raise an OverflowError
    # stack.push(6)
    
    while not stack.is_empty():
        print("Popped element:", stack.pop())
    
    print("Is stack empty after popping all elements?", stack.is_empty())  # True
    
    # Uncommenting the following line will raise an IndexError
    # stack.pop()