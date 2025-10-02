#INT3086 Assignment 1 Part A Self Study
#Oscar Ng Cheuk Hau 11558129 
#Shunting Yard Algorithm to convert infix expression to postfix expression
class Stack:
    
    """
    A simple stack implementation using a list.
    """
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) ==  0 
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Error: Popping from an empty stack")
    
def precedence(op):
    """
    Return the precedence of the given operator.
    Higher number means higher precedence.
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = Stack()
    postfix = []
    i = 0

    while i < len(expression):
        ch = expression[i]
    
        if ch.isalnum(): 
            postfix.append(ch)
        elif ch == '(':
            stack.push(ch)
        elif ch == ')':
            while not stack.is_empty() and stack.items[-1] != '(':
                postfix.append(stack.pop())
            stack.pop  # Pop the '(' from the stack
        
        else: 
            while (not stack.is_empty() and precedence(stack.items[-1]) >= precedence(ch)):
                postfix.append(stack.pop())
            stack.push(ch) # Push the current operator onto the stack
        i += 1

        while not stack.is_empty():
            postfix.append(stack.pop())
    return ''.join(postfix)

if __name__ == "__main__":
    expression = input("Enter an infix expression: ")
    postfix_expression = infix_to_postfix(expression)
    print("Postfix expression:", postfix_expression)
            