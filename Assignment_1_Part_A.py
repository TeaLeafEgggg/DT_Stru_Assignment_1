#INT3086 Assignment 1 Part A Self Study
#Oscar Ng Cheuk Hau 11558129 
#Shunting Yard Algorithm to convert infix expression to postfix expression
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

