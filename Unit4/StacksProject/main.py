"""
main.py
Driver for Linked Lists
"""
import os
from stack import Stack

# The file of the data path
data_path = os.path.join(os.getcwd(), "StacksProject/data/data.txt")

OPERATORS = {  # PEMDAS
    "(": {  # Parantheses are exampt from the rule
        "weight": -1,
        "func": lambda x, y: None
    },
    ")": {
        "weight": -1,
        "func": lambda x, y: None
    },
    "+": {
        "weight": 0,
        "func": lambda x, y: x + y
    },
    "-": {
        "weight": 0,
        "func": lambda x, y: x - y
    },
    "*": {
        "weight": 1,
        "func": lambda x, y: x * y
    },
    "/": {
        "weight": 1,
        "func": lambda x, y: x / y
    },
    "%": {
        "weight": 1,
        "func": lambda x, y: x % y
    },
    "^": {
        "weight": 2,
        "func": lambda x, y: x ** y
    }
}


def format_expr(expr):
    """
    Formats the expression to have spaces between each operator and operand

    Paramaters:
    -----------
    expr : String
        The expresion

    Returns:
    --------
    String
        The formated expression
    """
    # Remove all spaces from expr
    expr = ''.join(filter(lambda x: x != ' ', expr))

    i = 0
    while i < len(expr) - 1:
        # If the character is an operator
        if expr[i] in OPERATORS.keys():
            # Insert space between the two chars
            expr = expr[:i+1] + ' ' + expr[i+1:]
            i += 2
        # If the character is an operand and the next char is not
        elif expr[i] not in OPERATORS.keys() and expr[i + 1] in OPERATORS.keys():
            # Insert space between the two cars
            expr = expr[:i+1] + ' ' + expr[i+1:]
            i += 2
        else:
            i += 1

    return expr


def in2post(expr):
    """
    Takes in an expression such as
    '3 * 2 + 3 * (9 * 5)'
    and outputs it as a postfix expression
    e.g
    '3 2 * 3 9 5 * * +'

    Paramaters:
    -----------
    expr : String
        The infix expresion being converted to postfix
        Each opperand and opperator needs to be deliminated by a space

    Returns:
    --------
    String
        The postfix expression
    """

    if not isinstance(expr, str):
        raise ValueError("Expression must be a string")

    oper_stack = Stack()
    output_list = []

    # Format expr to have spaces deliminating each value
    expr = format_expr(expr)
    # Convert expr into a list
    expr = expr.split(" ")

    for char in expr:
        if char == '(':
            # If the character is a left parantheses,
            # Push it onto the operator stack
            oper_stack.push(char)
        elif char == ')':
            # If the character is a right parantheses,
            # Push every operator from the operator stack
            # Until a left parantheses is found
            operator = ''
            while operator != '(':
                operator = oper_stack.pop()

                # Parantheses not needed in output
                if operator != '(':
                    output_list.append(operator)

                else:
                    break

                if oper_stack.is_empty():
                    raise SyntaxError("The expression is invalid")
        elif char in OPERATORS.keys():
            # If character is an operator

            # If operator stack is empty
            if oper_stack.is_empty():
                oper_stack.push(char)
                continue

            # Add all the operators of lesser value on the opperator stack until
            # a greater operator is reached.
            while not oper_stack.is_empty() and OPERATORS[char]["weight"] <= OPERATORS[oper_stack.top()]["weight"]:
                output_list.append(oper_stack.pop())
            oper_stack.push(char)
        else:
            # If character is an operand, append it to the
            # output
            output_list.append(char)

    while not oper_stack.is_empty():
        oper = oper_stack.pop()
        if oper == "(":
            raise SyntaxError("Expression not valid")
        output_list.append(oper)

    return ' '.join(output_list)


def eval_postfix(expr):
    """
    Evaluates an expression in postfix notation

    Paramaters:
    -----------
    expr : String
        The expression (postfix notation)

    Returns:
    Float
        The evaluated expression
    """
    if not isinstance(expr, str):
        raise ValueError("Expr must be a string")

    # Split the list by spaces, and remove any extra spaces and empty strings
    expr = list(filter(lambda x: x not in ['', ' '], expr.split(' ')))

    operands = Stack()

    if len(expr) == 1:  # If there is only one value
        return float(expr[0])

    for char in expr:
        if char in OPERATORS.keys():
            # If the character is an opperator, use it to determine the next value
            # Because the stack reverses the order, we need to switch the assignment order as well
            if operands.size() >= 2:
                value_two = float(operands.pop())
                value_one = float(operands.pop())
            else:
                raise SyntaxError("Invalid postscript")

            # Input the two operands into the operators function,
            # and push it onto the opperands stack
            operands.push(OPERATORS[char]["func"](value_one, value_two))

        else:
            # If the character is an operand
            operands.push(char)

    output = operands.pop()
    if not operands.is_empty():
        raise SyntaxError("Invalid postscript")

    return output


def get_expr():
    """
    Collects the expressions from the data file

    Returns:
    --------
    List[String]
        The expressions in the data file
    """
    expressions = []
    with open(data_path, "r") as data:
        for expr in data.readlines():
            expressions.append(expr.strip())

    return expressions


def main():
    """
    Driver function for main.py
    """
    expressions = get_expr()
    for expression in expressions:
        expr = expression
        post = in2post(expr)
        eval_ = eval_postfix(post)

        print("infix: " + expr)
        print("postfix: " + post)
        print("answer: " + str(eval_))


if __name__ == "__main__":
    main()
