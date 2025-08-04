"""
Stack Implementation
"""
from typing import Any


class Stack:
    """
    A simple stack implementation using a list.
    """
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        """
        self._items = []

    def push(self, item) -> None:
        """
        Push an item onto the stack.
        """
        self._items.append(item)

    def is_empty(self) -> bool:
        """
        Check if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0
    
    def pop(self) -> Any:
        """
        Pop an item from the stack.
        """
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("[DS-STACK ERROR] Pop from an empty stack")

    def peek(self) -> Any:
        """
        Peek at the top item of the stack without removing it.
        """
        if not self.is_empty():
            return self._items[len(self._items) - 1]
        raise IndexError("[DS-STACK ERROR] Peek from an empty stack")

    def size(self) -> int:
        """
        Get the number of items in the stack.
        """
        return len(self._items)

    def clear(self) -> None:
        """
        Clear the stack.
        """
        self._items.clear()

if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())  # Should print: True

    stack.push("hello")
    stack.push("world") 
    print(stack.is_empty())  # Should print: False

    item = stack.pop()
    print(item)  # Should print: world    
    item = stack.peek()
    print(item)  # Should print: hello
    print(stack.size())  # Should print: 1
    stack.clear()
    print(stack.is_empty())  # Should print: True