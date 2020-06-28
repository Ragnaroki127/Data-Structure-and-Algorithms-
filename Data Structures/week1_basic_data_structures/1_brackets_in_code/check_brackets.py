# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    unmatched_brackets_indexes = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            unmatched_brackets_indexes.append(i)
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return i + 1
            top = opening_brackets_stack.pop()
            unmatched_brackets_indexes.pop()
            if not are_matching(top, next):
                return i + 1
            pass
    if len(opening_brackets_stack) != 0:
        return unmatched_brackets_indexes[0] + 1
    else:
        return -1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    if mismatch == -1:
        print('Success')
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
