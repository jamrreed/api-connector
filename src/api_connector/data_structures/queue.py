from collections import deque

class Queue:
    def __init__(self, items: list = []):
        self.items_queue = deque(items)

    # adds to the end of the collection
    def enqueue(self, item: any) -> None:
        self.items_queue.append(item)

    # pops from the beginning of the collection
    def dequeue(self) -> any:
        if self.isEmpty():
            return None
        
        return self.items_queue.popleft()

    def isEmpty(self) -> bool:
        return len(self.items_queue) > 0