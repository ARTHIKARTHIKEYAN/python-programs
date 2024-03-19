class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def top(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")
            return None

def is_palindrome(string):
    stack = Stack()
    for char in string:
        stack.push(char)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return string == reversed_string

# Example usage:
string1 = "racecar"
string2 = "hello"

print(f"Is '{string1}' a palindrome:", is_palindrome(string1))
print(f"Is '{string2}' a palindrome:", is_palindrome(string2))
