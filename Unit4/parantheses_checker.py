from StacksProject.stack import Stack


class ParanthesesChecker:
    def __init__(self):
        pass

    def is_balanced(self, parantheses):
        stack = Stack()

        for char in parantheses:
            if char in "([{":
                stack.push(char)

            elif char in ")]}":
                if stack.is_empty():
                    return False
                elif stack.pop() not in "([{":
                    return False

        return stack.is_empty()


def main():
    checker = ParanthesesChecker()

    print(checker.is_balanced("()()()(())"))
    print(checker.is_balanced(")()"))
    print(checker.is_balanced("{[][([])()()()]}"))


if __name__ == "__main__":
    main()
