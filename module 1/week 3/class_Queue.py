class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self._queue = []
    
    def is_empty(self):
        return len(self._queue) == 0
    
    def is_full(self):
        return len(self._queue) == self.capacity
    
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self._queue.append(value)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._queue.pop(0)
    
    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._queue[0]

# Test the Queue class
if __name__ == '__main__':
    queue = Queue(5)
    
    print("Is queue empty?", queue.is_empty())  # True
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    
    print("Is queue full?", queue.is_full())  # True
    print("Front element:", queue.front())  # 1
    
    print("Dequeued element:", queue.dequeue())  # 1
    print("Front element after dequeue:", queue.front())  # 2
    print("Is queue full after dequeue?", queue.is_full())  # False
    
    # Uncommenting the following line will raise an OverflowError
    # queue.enqueue(6)
    
    while not queue.is_empty():
        print("Dequeued element:", queue.dequeue())
    
    print("Is queue empty after dequeuing all elements?", queue.is_empty())  # True
    
    # Uncommenting the following line will raise an IndexError
    # queue.dequeue()