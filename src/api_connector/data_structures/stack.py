class Stack:
    def __init__(self, items: list = []):
        self.items = items

    def isEmpty(self) -> bool:
        return len(self.items) < 1
    
    def size(self) -> int:
        return len(self.items)
    
    def push(self, item: any) -> None:
        self.items.append(item)

    def pop(self) -> any:
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
        
    def peek(self) -> any:
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def peek_all(self) -> list:
        return self.items.copy()
    
    def clear(self) -> None:
        self.items.clear()