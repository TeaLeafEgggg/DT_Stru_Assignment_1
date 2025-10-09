# INT3086 Assignment 1 Part B
# Oscar Ng Cheuk Hau 11558129 
# Infix to Postfix Converter and Postfix Evaluator using Custom Stack ADT

from prettytable import PrettyTable  # Import PrettyTable module to create a table for better visualization of the output 
# ("pip install prettytable" is needed in the terminal when running the program for the first time)

class Stack: # Custom Stack ADT implementation
    """
    Custom Stack ADT implementation using a list.
    Includes basic operations: push, pop, is_empty, and peek (necessary for precedence checking).
    """
    
    def __init__(self): 
        """Initialize an empty stack."""
        self.items = []  # Internal list to hold stack elements

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item) # Append item to the end of the list

    def pop(self):
        """Remove and return the top item from the stack if not empty."""
        if not self.is_empty(): # Check if the stack is not empty
            return self.items.pop() # Pop the last item from the list
        else: 
            raise IndexError("Error: Popping from an empty stack")  # Error handling for empty stack

    def is_empty(self): 
        """Check if the stack is empty."""
        return len(self.items) == 0 # Return True if the list is empty, else False

    def peek(self): 
        """Return the top item without removing it if not empty."""
        if not self.is_empty(): # Check if the stack is not empty
            return self.items[-1] # Return the last item in the list
        else:
            raise IndexError("Error: Peeking from an empty stack")  # Error handling for empty stack

def to_postfix(inExp): # Convert infix to postfix
    """
    Convert infix expression to postfix using the custom Stack ADT.
    Handles numbers, alphabets, operators (+, -, *, /, ^), and parentheses.
    Returns space-separated postfix string.
    """
    stack = Stack()  # Create custom stack for operators
    postfix = []  # List to build postfix expression
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}  # Define operator precedence
    associativity = {'+':'L', '-':'L', '*':'L', '/':'L', '^':'R'}  # Define associativity rules
    steps = []  # List to hold steps for visualization

    def is_operator(c):  # Check if the character is an operator
        return c in precedence # Return True if c is in precedence keys

    def is_higher_precedence(op1, op2):  # Check precedence of operators
        return (precedence[op1] > precedence[op2] or # Higher precedence
                (precedence[op1] == precedence[op2] and associativity[op1] == 'L')) # Equal precedence and left associative

    # Tokenize the input expression
    i = 0  # Index to track the user input
    current_token = ''  # Variable to hold the current token
    while i < len(inExp):  # While loop to go through the input. Dealing with one character at a time
        if inExp[i].isspace():  # Skip spaces
            i += 1 # Increment index to skip space
            continue # Continue to the next iteration

        if inExp[i] in precedence or inExp[i] in '()':  # Detect operators or parentheses
            if current_token:  # If there is a current token
                postfix.append(current_token)  # Append operand to postfix
                current_token = '' # Reset current token
            postfix.append(inExp[i])  # Append operator or parenthesis
            i += 1
        else:  # Handle operands (numbers, alphabets, decimals)
            current_token += inExp[i]
            i += 1 # Increment index to continue building the token
    
    if current_token: # If there's a token left at the end
        postfix.append(current_token)  # Append the last operand

    # Shunting Yard Algorithm with step tracking
    postfix_tokens = []  # Reset postfix for correct building
    for token in postfix:  # Process each token
        step = {'Token': token, 'Postfix Expression': ' '.join(postfix_tokens), 'Stack': ' '.join(stack.items) if not stack.is_empty() else ''}  # Step dictionary for table
        if token.isalnum() or ('.' in token and token.replace('.', '', 1).isdigit()) or token.lstrip('-').isdigit():  # Operand (number or alphabet)
            postfix_tokens.append(token) # Append operand to postfix
        
        elif token == '(':  # Dealing with Opening parenthesis
            stack.push(token) # Push '(' onto stack

        elif token == ')':  # Dealing with Closing parenthesis
            while not stack.is_empty() and stack.peek() != '(':  # Pop until '('
                postfix_tokens.append(stack.pop()) # Pop and append to postfix
            
            if not stack.is_empty(): # If stack is not empty
                stack.pop()  # Pop the '('
        
        elif is_operator(token): # If the token is an operator
            while (not stack.is_empty() and stack.peek() != '(' and 
                   is_higher_precedence(stack.peek(), token)):  # Pop higher precedence operators
                postfix_tokens.append(stack.pop()) # Pop and append to postfix
            stack.push(token) # Push current operator onto stack
        step['Postfix Expression'] = ' '.join(postfix_tokens)  # Update postfix in step
        step['Stack'] = ' '.join(stack.items) if not stack.is_empty() else ''  # Update stack in step
        steps.append(step)  # Append step for visualization

    # Pop remaining operators
    while not stack.is_empty():  # While there are still operators on the stack
        postfix_tokens.append(stack.pop())  # Pop and append to postfix
        steps.append({'Token': 'Pop', 'Postfix Expression': ' '.join(postfix_tokens), 'Stack': ' '.join(stack.items) if not stack.is_empty() else ''}) # Append step for visualization


    # Visualize conversion steps
    table = PrettyTable() # Create a PrettyTable instance
    table.field_names = ['Token', 'Postfix Expression', 'Stack'] # Define table headers
    for step in steps: # Add each step to the table
        table.add_row([step['Token'], step['Postfix Expression'], step['Stack']]) # Add row to the table
    print('\nStep-by-Step Infix to Postfix Conversion Process:') # Print header
    print(table) # Print the table

    return ' '.join(postfix_tokens)  # Return space-separated postfix

def eval_postfix(postExp): # Evaluate postfix expression
    """
    Evaluate postfix expression using the custom Stack ADT.
    Handles numeric operations; returns the result as float.
    Assumes valid postfix input with numbers and operators.
    """
    stack = Stack()  # Create custom stack for operands
    tokens = postExp.split()  # Split into tokens
    steps = []  # List to hold steps for visualization

    for token in tokens:  # Process each token
        step = {'Token': token, 'Stack': ' '.join(str(x) for x in stack.items) if not stack.is_empty() else ''}  # Step dictionary for table
        if token.lstrip('-').isdigit() or token.replace('.', '', 1).replace('-', '', 1).isdigit():  # Operand (number)
            stack.push(float(token))  # Push as float
        elif token in '+-*/^':  # Operator
            if stack.is_empty():
                raise ValueError("Invalid postfix expression") # Check for sufficient operands
            b = stack.pop()  # Second operand
            if stack.is_empty(): 
                raise ValueError("Invalid postfix expression") # Check for sufficient operands
            a = stack.pop()  # First operand
            if token == '+':
                result = a + b # Perform addition
            elif token == '-':  
                result = a - b # Perform subtraction
            elif token == '*':
                result = a * b # Perform multiplication
            elif token == '/': 
                result = a / b # Perform division
            elif token == '^':
                result = a ** b # Perform exponentiation
            stack.push(result)  # Push result
        step['Stack'] = ' '.join(str(x) for x in stack.items) if not stack.is_empty() else ''  # Update stack in step
        steps.append(step)  # Append step for visualization

    if stack.is_empty():
        raise ValueError("Invalid postfix expression") # Final check for valid expression
    result = stack.pop()  # Final result

    # Visualize evaluation steps
    table = PrettyTable() # Create a PrettyTable instance
    table.field_names = ['Token', 'Stack'] # Define table headers
    for step in steps: # Add each step to the table
        table.add_row([step['Token'], step['Stack']]) # Add row to the table
    print('\nStep-by-Step Postfix Evaluation Process:') # Print header
    print(table) # Print the table

    return result  # Return the computed result

def main(): # Main user interface
    """
    Main user interface to test the Stack ADT with infix expressions.
    Provides a loop for input, converts to postfix, evaluates, and visualizes steps.
    Includes welcome message, examples, and exit option.
    """
    print("\n" + "=" * 50) # Print a separator line
    print("Welcome to Oscar's Infix to Postfix Converter & Evaluator!") # Welcome message
    print("This program converts infix expressions to postfix and evaluates them using a custom Stack.") # Description
    print("Supported operators: +, -, *, /, ^ (with parentheses for grouping).") # Supported operators
    print("Supports numbers (integers, decimals, negative) and alphabets as variables (but evaluation only for numbers).") # Supported operands
    print("Examples:") # Examples
    print("  - (4+5)*(2-3)    [Expected postfix: 4 5 + 2 3 - * , Result: -9]") # Example 1
    print("  - 10+20*30       [Expected postfix: 10 20 30 * + , Result: 610]") # Example 2
    print("  - A+B*C          [Expected postfix: A B C * + , No evaluation since variables]") # Example 3
    print("Enter 'end' or 'End' to exit.") # Exit instruction
    print("=" * 50 + "\n") # Print a separator line
    
    while True: # Loop for user input
        inExp = input("Enter infix expression: ").strip() # Get user input and strip whitespace
        if inExp.lower() == 'end': # Exit condition
            print("\nThanks for using the program! Goodbye.") # Exit message
            break # Exit the loop and program
        
        try: # Try block for error handling
            postExp = to_postfix(inExp) # Convert to postfix
            print(f"\nConverted Postfix: {postExp}") # Display postfix expression
            
            # Check if evaluable (only numbers)
            all_numbers = all(t.lstrip('-').replace('.', '', 1).isdigit() for t in postExp.split() if t not in '+-*/^()') # Check if all tokens are numbers
            if all_numbers: # If all tokens are numbers
                result = eval_postfix(postExp) # Evaluate postfix
                print(f"Evaluation Result: {result}\n") # Display result
            else: # If there are variables
                print("Expression contains variables; evaluation skipped.\n") # Skip evaluation message
        except Exception as e: # Catch exceptions
            print(f"Error: {e}. Please enter a valid infix expression.\n") # Display error message

if __name__ == "__main__": # Run the main function if this script is executed
    main() # Call the main function