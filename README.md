DT_Stru_Assignment_1
Overview
This repository contains the Python implementation for INT3086 Assignment 1 (15%) on Data Structures, focusing on converting infix expressions to postfix notation and evaluating postfix expressions using a custom Stack Abstract Data Type (ADT). The program follows the assignment requirements outlined in the PDF, including a self-study on infix/postfix notations, development of a Stack class, and two key methods: to_postfix(inExp) and eval_postfix(postExp). It includes a user-friendly main interface for testing, step-by-step visualization using PrettyTable, and support for operators (+, -, *, /, ^), parentheses, numbers (integers, decimals, negatives), and variables (alphabets).
The code demonstrates the Shunting Yard algorithm for conversion and stack-based evaluation, with inline comments for clarity. It avoids Python's built-in stack structures, using a custom Stack class with push, pop, is_empty, and peek operations.
Key Features

Custom Stack ADT: Implements basic stack operations without using built-in lists for core logic (though internally uses a list for efficiency, as per good programming practices).
Infix to Postfix Conversion: Handles operator precedence, associativity (left for +,-,*,/; right for ^), and parentheses.
Postfix Evaluation: Computes results for numeric expressions, skipping variables.
Visualization: PrettyTable displays step-by-step processes for both conversion and evaluation.
User Interface: Interactive loop with examples, error handling, and exit option ('end').
Supported Inputs:

Simple: 2 + 3 * 4 → Postfix: 2 3 4 * +
With Parentheses: (4+5)*(2-3) → Postfix: 4 5 + 2 3 - * → Result: -9
Negatives/Decimals: -2.5 + 3.7 * -1.0 → Postfix: -2.5 3.7 -1.0 * + → Result: -6.2
Variables: A + B * C → Postfix: A B C * + (Evaluation skipped)



Installation and Setup

Clone the Repository:
textgit clone https://github.com/TeaLeafEgggg/DT_Stru_Assignment_1.git
cd DT_Stru_Assignment_1

Install Dependencies:

Requires Python 3.9+.
Install PrettyTable for table visualization:
textpip install prettytable
(Or pip3 install prettytable on macOS/Linux.)


Run the Program:
textpython Assignment_1_Part_B.py

Follow the prompts to enter infix expressions.
Type 'end' to exit.



Usage
Example Run
textEnter infix expression: (4+5)*(2-3)

Step-by-Step Infix to Postfix Conversion Process:
+---------+-------------------+---------+
| Token   | Postfix Expression| Stack   |
+---------+-------------------+---------+
| (       |                   | (       |
| 4       | 4                 | (       |
| +       | 4                 | ( +     |
| 5       | 4 5               | ( +     |
| )       | 4 5 +             |         |
| *       | 4 5 +             | *       |
| (       | 4 5 +             | * (     |
| 2       | 4 5 + 2           | * (     |
| -       | 4 5 + 2           | * ( -   |
| 3       | 4 5 + 2 3         | * ( -   |
| )       | 4 5 + 2 3 -       | *       |
| Pop     | 4 5 + 2 3 - *     |         |
+---------+-------------------+---------+

Converted Postfix: 4 5 + 2 3 - *

Step-by-Step Postfix Evaluation Process:
+---------+------------+
| Token   | Stack      |
+---------+------------+
| 4       | 4.0        |
| 5       | 4.0 5.0    |
| +       | 9.0        |
| 2       | 9.0 2.0    |
| 3       | 9.0 2.0 3.0|
| -       | 9.0 -1.0   |
| *       | -9.0       |
+---------+------------+

Evaluation Result: -9.0
Testing Recommendations

Simple: 10 + 20 * 30 (Result: 610.0)
Complex: 3 + 4 * 2 / (1 - 5) ^ 2 (Result: -1.125)
Variables: A + B * C (Conversion only)
Edge Cases: Unbalanced parentheses (triggers error handling)

Code Structure

Stack Class: Core ADT with push, pop, is_empty, peek.
to_postfix(inExp): Tokenizes input, applies Shunting Yard algorithm, visualizes steps.
eval_postfix(postExp): Evaluates tokens using stack, visualizes stack changes.
main(): Interactive UI with examples and error handling.

Big-O Analysis

to_postfix(inExp): O(n) time, where n is input length. Single pass for tokenization and processing; stack operations O(1). Space: O(n).
eval_postfix(postExp): O(m) time, where m is number of tokens (~n). Single pass evaluation; stack O(m/2). Space: O(m).
Overall: Efficient for typical expressions; suitable for real-time use.

Report and Assessment
This implementation meets the assignment criteria:

Custom Stack ADT used exclusively.
Step-by-step visualization before results.
Inline comments and method descriptions.
Unique UI with personal style (e.g., welcome message, examples).
Report: Include screenshots of test runs (e.g., above example) and Big-O discussion.


Last Updated: October 20, 2025
