#INT3086 Assignment 1 Part A Self Study
#Oscar Ng Cheuk Hau 11558129 
#Shunting Yard Algorithm to convert infix expression to postfix expression
class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self): # Return the top item without removing it (for dealing with the precedence of operators)
        if not self.isEmpty():
            return self.items[-1]
        return None

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def topostfixinExp(infixExpr):
    Stack = stack()
    postfix = []
    for char in infixExpr:
        if char.isalnum():  # If operand, add to postfix expression
            postfix.append(char)
        elif char == '(': # If '(', push to stack
            stack.push(char) 
        elif char == ')': # If ')', pop from stack to postfix until '(' is found
            while not stack.isEmpty() and stack.peek() != '(': 
                postfix.append(stack.pop()) # Append popped operators to postfix
            stack.pop()  # Pop '('
        else:
            while (not stack.isEmpty() and precedence(stack.peek()) >= precedence(char)): # If operator, pop from stack to postfix until stack is empty or top of stack has less precedence
                postfix.append(stack.pop()) # Append popped operators to postfix
            stack.push(char) # Push current operator to stack

    while not stack.isEmpty(): # Pop all remaining operators from stack to postfix
        postfix.append(stack.pop()) # Append popped operators to postfix

    return ''.join(postfix) # Convert list to string

def evalpostfixpostExp(postfixExpr): # Evaluate postfix expression
    Stack = stack() # Create a stack for evaluation
    for char in postfixExpr: # Iterate through each character in postfix expression
        if char.isdigit(): # If operand, push to stack
            stack.push(int(char)) # Convert char to int before pushing
        else:
            val2 = stack.pop() # Pop two operands from stack
            val1 = stack.pop()
            if char == '+': # Perform operation and push result back to stack
                stack.push(val1 + val2) # Addition
            elif char == '-':
                stack.push(val1 - val2) # Subtraction
            elif char == '*':
                stack.push(val1 * val2) # Multiplication
            elif char == '/':
                stack.push(val1 // val2)  # Integer division
            elif char == '^':
                stack.push(val1 ** val2) # Exponentiation

    return stack.pop() # The final result is the only item left in the stack

def main(): # Main function to run the program
    print("Welcome to the Infix to Postfix Converter and Evaluator")
    print("Note: Use single-digit operands and operators +, -, *, /, ^")
    while True: # Loop to allow multiple conversions and evaluations
        infix = input("Enter infix expression (or 'exit' to quit): ").replace(" ", "") # Remove spaces from input
        if infix.lower() == 'exit': # Exit condition
            break # Break the loop if user wants to exit
        postfix = topostfixinExp(infix) # Convert infix to postfix
        print(f"Postfix expression: {postfix}") # Display postfix expression
        result = evalpostfixpostExp(postfix) # Evaluate postfix expression
        print(f"Evaluation result: {result}\n") # Display evaluation result

if __name__ == "__main__": # Run the main function
    main()
