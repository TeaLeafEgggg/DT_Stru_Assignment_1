# INT3086 Assignment 1 Part A Self Study
# Oscar Ng Cheuk Hau 11558129 
# Shunting Yard Algorithm to convert infix expression to postfix expression

from prettytable import PrettyTable  # Import PrettyTable module to create a table for better visualization of the output 
# ("pip install prettytable" is needed in the terminal when running the program for the first time)

def evaluate_postfix(postfix): # Function to evaluate the postfix expression if all tokens are numbers
    stack = [] # Stack to hold the operands
    for token in postfix.split(): # Split the postfix expression into tokens
        if token.lstrip('-').isdigit() or token.replace('.', '', 1).replace('-', '', 1).isdigit(): # Check if the token is a number (including negative and decimal numbers)
            stack.append(float(token)) # If true, convert the token to float and push it onto the stack
        else: # The token is an operator
            b = stack.pop() # Pop the top two operands from the stack
            a = stack.pop() # Pop the top two operands from the stack
            if token == '+': stack.append(a + b) # Perform the operation and push the result back onto the stack
            elif token == '-': stack.append(a - b) # Perform the operation and push the result back onto the stack
            elif token == '*': stack.append(a * b) # Perform the operation and push the result back onto the stack
            elif token == '/': stack.append(a / b) #1 Perform the operation and push the result back onto the stack
            elif token == '^': stack.append(a ** b) # Perform the operation and push the result back onto the stack
    return stack[0] # The final result is the only element left in the stack

while True:  # Loop to ensure valid input from user
    print('Welcome to the Infix to Postfix Converter!') # Welcome message
    print("Type 'end' or 'End' to stop the program.") # Instructions to end the program
    print('Please enter a valid infix expression with or without spaces between each input.') # Instructions for user input
    print('For example: "3 + 4 * 2 / ( 1 - 5 ) ^ 2" or "A+B*C"') # Example of valid input
    user_input = input('Enter an infix expression: ') # Prompt user for input
    if user_input.lower() == 'end':  # If the user inputs 'end' or 'End', the program will terminate
        print('Thanks for using the program. Goodbye!') # Goodbye message
        break  # Break the loop and terminate the program
    
    # Prepare for the Shunting Yard Algorithm / tokenize input
    infix_expression = []  # List to hold the infix expression that the user inputs
    operators = [] # Stack to hold operators and parentheses during the conversion process
    postfix_expression = [] # List to hold the resulting postfix expression
    steps = []  # List to hold the steps for PrettyTable output

    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}  # Define operator precedence. How "high valued" an operator is
    associativity = {'+':'L', '-':'L', '*':'L', '/':'L', '^': 'R'}  # “+", "-", "*", "/" are left associative while "^" is right associative. Do from left to right or right to left
    # Left associative example: 5 - 3 - 2 = (5 - 3) - 2
    # Right associative example: 2 ^ 3 ^ 2 = 2 ^ (3 ^ 2) 

    def is_operator(c):  # Check if the character is an operator
        return c in precedence # If the character is in the precedence dictionary, it is an operator

    def is_higher_precedence(op1, op2):  # Check precedence of operators
        return (precedence[op1] > precedence[op2] or \
                # If operator 1 has higher precedence than operator 2 
                (precedence[op1] == precedence[op2] and associativity[op1] == 'L')) 
                # If both operators have the same precedence, check associativity. If left associative ("+", "-", "*", "/", return true. If right associative ("^"), return false. This is for the while loop in the Shunting Yard Algorithm

    # Tokenize the input expression. 
    # Tokens work as an indicator of the current position in the expression. 
    i = 0  # Index to track the user input
    current_token = ''  # Variable to hold the current token
    while i < len(user_input):  # While loop to go through the user input. Dealing with one character at a time for tokenization and further processing
        if user_input[i].isspace():  # Skip the spaces in the user input when necessary
            i += 1  # Index increment i.e. move to the next character
            continue  # This will not stop the loop, just skip the space and continue
        if user_input[i] in precedence or user_input[i] in '()':  # This detects if the user input is an operator which is in the precedence dictionary or if the user input is within a parentheses
            if current_token:  # If there is a current token (i.e. if the current token is not an empty string)
                infix_expression.append(current_token)  # Append the current token to the infix expression list
                current_token = ''  # Reset the current token to an empty string
            infix_expression.append(user_input[i])  # If true, append the operator or parentheses to the infix expression list
            i += 1  # Index increment i.e. move to the next character
        else:  # This else statement is for when the user input is an operand (number or variable) 
            current_token += user_input[i]  # Append the character at index i to the current token
            i += 1  # Corrected from i += i to i += 1
    if current_token: 
        infix_expression.append(current_token)  # Append the final token if exists

    # Shunting Yard Algorithm with step tracking for all tokens
    for token in infix_expression:  # Process each token in the infix expression list
        step = {'Token': token, 'Postfix Expression': ' '.join(postfix_expression), 'Stack': ' '.join(operators)}  # Create a dictionary to hold the current token, postfix expression and operators stack for PrettyTable output
        if token.lstrip('-').isdigit() or token.replace('.', '', 1).replace('-', '', 1).isdigit() or token.isalpha():  # Check if the token is a number or alphabet
            postfix_expression.append(token)  # If true, append the token to the postfix expression list
            steps.append(step)  # Add step before processing to show token entry
        elif token == '(':  # If the token is a left parenthesis
            operators.append(token)  # Push the left parenthesis onto the operators stack
            step['Stack'] = ' '.join(operators)  # Update the operators stack in the step dictionary
            steps.append(step)  # Append the step dictionary to the steps list for PrettyTable output
        elif token == ')':  # If the token is a right parenthesis
            while operators and operators[-1] != '(':  # Pop operators from the stack to the output list until a left parenthesis is encountered
                postfix_expression.append(operators.pop())  # Pop the operator from the stack and append it to the postfix expression list
            if operators:  # Ensure stack is not empty before popping
                operators.pop()  # Pop the '('
            step['Postfix Expression'] = ' '.join(postfix_expression)  # Update the postfix expression in the step dictionary
            step['Stack'] = ' '.join(operators)  # Update the operators stack in the step dictionary
            steps.append(step)  # Append the step dictionary to the steps list for PrettyTable output
        elif is_operator(token):  # If the token is an operator
            while (operators and operators[-1] != '(' and
                   is_higher_precedence(operators[-1], token)):  # While there are operators on the stack and the top operator is not a left parenthesis, and the top operator has higher or equal precedence than the current token
                postfix_expression.append(operators.pop())  # Pop the operator from the stack and append it to the postfix expression list
            operators.append(token)  # Push the current token onto the operators stack
            step['Postfix Expression'] = ' '.join(postfix_expression)  # Update the postfix expression in the step dictionary
            step['Stack'] = ' '.join(operators)  # Update the operators stack in the step dictionary
            steps.append(step)  # Append the step dictionary to the steps list for PrettyTable output

    # Pop all the operators from the stack
    while operators:  # While there are still operators on the stack
        postfix_expression.append(operators.pop())  # Pop the operator from the stack and append it to the postfix expression list
        steps.append({'Token': 'Pop', 'Postfix Expression': ' '.join(postfix_expression), 'Stack': ' '.join(operators)}) # Append the step dictionary to the steps list for PrettyTable output
        
    # Output the step-by-step process using PrettyTable
    table = PrettyTable() # Create a PrettyTable object
    table.field_names = ['Token', 'Postfix Expression', 'Stack'] # Define the column names for the table
    for step in steps: # Add each step to the table
        table.add_row([step['Token'], step['Postfix Expression'], step['Stack']]) # Add a row to the table for each step
    

    print('\nStep-by-Step Conversion Process:') # Print a header for the step-by-step conversion process
    print(table) # Print the table

    # Output the final postfix expression as a space-separated string
    print('\nFinal Postfix expression:', ' '.join(postfix_expression)) # Print the final postfix expression
    
    # Evaluate if all tokens are numbers
    all_numbers = all(token.lstrip('-').isdigit() or token.replace('.', '', 1).replace('-', '', 1).isdigit() for token in infix_expression if not (token in '()+-*/^')) # Check if all tokens in the infix expression are numbers (excluding operators and parentheses)
    if all_numbers and all(not token.isalpha() for token in infix_expression): # Ensure there are no alphabetic tokens
        result = evaluate_postfix(' '.join(postfix_expression)) # Evaluate the postfix expression
        print(f'\nResult of the expression: {result}') # Print the result of the expression
    
    print("\nEnter another expression or type 'end'/'End' to stop.\n") # Prompt the user to enter another expression or end the program