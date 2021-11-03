"""
main.py
Driver for Linked Lists
"""
from stack import Stack

OPERATORS = {  # PEMDAS
    "(": -1,  # Paranteses are exempt from the rule
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "%": 1,
    "^": 2
}


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

    oper_stack = Stack()
    output_list = []

    expr = expr.split(' ')

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

        elif char in OPERATORS.keys():
            # If character is an operator

            # If operator stack is empty
            if oper_stack.is_empty():
                oper_stack.push(char)

            # If the new operator has less priority than old
            elif OPERATORS[char] < OPERATORS[oper_stack.top()]:
                output_list.append(oper_stack.pop())
                oper_stack.push(char)

            # If the new operator has more priority than old
            elif OPERATORS[char] > OPERATORS[oper_stack.top()]:
                oper_stack.push(char)
        else:
            # If character is an operand, append it to the
            # output
            output_list.append(char)

    while not oper_stack.is_empty():
        output_list.append(oper_stack.pop())

    return ' '.join(output_list)


def main():
    print(in2post("3 + 4"))


if __name__ == "__main__":
    main()
