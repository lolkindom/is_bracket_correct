BRACKET_CHECKER_DICT = {')': '(', ']': '[', '}': '{'}


def bracket_checker(stack):
    if stack[-1] in BRACKET_CHECKER_DICT:
        if len(stack) == 1:
            return False

        if stack[-2] == BRACKET_CHECKER_DICT[stack[-1]]:
            stack.pop()
            stack.pop()
        else:
            return False
    return True


def is_bracket_correct(bracket_sequence):
    stack = []
    if len(bracket_sequence) % 2 == 1:
        return False

    for i in range(len(bracket_sequence)):
        stack.append(bracket_sequence[i])
        if not bracket_checker(stack):
            return False

    return True


bracket_sequence = input()
print(is_bracket_correct(bracket_sequence))