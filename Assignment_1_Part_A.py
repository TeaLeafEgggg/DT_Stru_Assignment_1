#INT3086 Assignment 1 Part A Self Study
#Oscar Ng Cheuk Hau 11558129 
#Shunting Yard Algorithm to convert infix expression to postfix expression
<<<<<<< HEAD
user_input = input("Enter an infix expression: ") # e.g. "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3" For users to input infix expression
infix_expression = [] #List to hold the infix expression that the user inputs
operators = [] 
postfix_expression = []
precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} #Define operator precedence. How "high valued" an operator is
associativity = {'+':'L', '-':'L', '*':'L', '/':'L', '^':'R'} # “+", "-", "*", "/" are left associative while "^" is right associative. Do from left to right or right to left
#Left associative example: 5 - 3 - 2 = (5 - 3) - 2
#Right associative example: 2 ^ 3 ^ 2 = 2 ^ (3 ^ 2) 

def is_operator(c): # Check if the character is an operator
    return c in precedence
def is_higher_precedence(op1, op2): #Check precedence of operators
    return (precedence[op1] > precedence[op2] or \
            #If operator 1 has higher precedence than operator 2 
            (precedence[op1] == precedence[op2] and associativity[op1] == 'L')) 
            #If both operators have the same precedence, check associativity. If left associative ("+", "-", "*", "/", return true. If right associative ("^"), return false. This is for the while loop in the Shunting Yard Algorithm
# Tokenize the input expression. 
# Tokens works as a indicator of the current position in the expression. 
# i.e. only the token needs to be evaluated instead of the whole expression
i = 0 #Index to track the user input
while i < len(user_input): #While loop to go through the user input
    if user_input[i].isspace(): #Skip the spacees in the user input when necessary
        i += 1 #index increment i.e. move to the next character
        continue
    if user_input[i] in precedence or user_input[i] in '()': #
        infix_expression.append(user_input[i])
        i += 1
    else:
        j = i
        while j < len(user_input) and (user_input[j].isalnum() or user_input[j] == '.'):
            j += 1
        infix_expression.append(user_input[i:j])
        i = j
# Shunting Yard Algorithm
for token in infix_expression:
    if token.isalnum() or ('.' in token and token.replace('.','',1).isdigit()):
        postfix_expression.append(token)
    elif token == '(':
        operators.append(token)
    elif token == ')':
        while operators and operators[-1] != '(':
            postfix_expression.append(operators.pop())
        operators.pop()  # Pop the '('
    elif is_operator(token):
        while (operators and operators[-1] != '(' and
               is_higher_precedence(operators[-1], token)):
            postfix_expression.append(operators.pop())
        operators.append(token)
# Pop all the operators from the stack
while operators:
    postfix_expression.append(operators.pop())
# Output the postfix expression
print("Postfix expression:", ' '.join(postfix_expression))

=======
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
>>>>>>> 248bf72250c9f3eae9b35875dfbe1d6af83dc27f
