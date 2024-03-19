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

def is_correctly_parenthesized(expression):
    stack = Stack()
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            if (char == ")" and stack.top() != "(") or \
               (char == "]" and stack.top() != "[") or \
               (char == "}" and stack.top() != "{"):
                return False
            stack.pop()
    return stack.is_empty()

# Example usage:
expression1 = "{[()()]}"
expression2 = "{[()]}("
expression3 = "([]{}"

print(f"Is '{expression1}' correctly parenthesized:", is_correctly_parenthesized(expression1))
print(f"Is '{expression2}' correctly parenthesized:", is_correctly_parenthesized(expression2))
print(f"Is '{expression3}' correctly parenthesized:", is_correctly_parenthesized(expression3))
