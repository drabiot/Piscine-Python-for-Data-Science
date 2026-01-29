import sys


def checkInput(arg: str = "") -> str:
    """Check the size and the number of the given input"""
    if (len(sys.argv) <= 1):
        while (len(arg) <= 0):
            arg = input("What is the text to count?\n")
        return (arg + '\n')
    assert (len(sys.argv) <= 2), "AssertionError: more than one argument is provided"
    return (sys.argv[1])


def parseInput(arg: str):
    """Parse the given input & count:
       - Total Characters
       - Upper Case Letters
       - Lower Case Letters
       - Punctuation Marks
       - Spaces
       - Digits"""
    totChar: int = len(arg)
    upCase: int = sum(map(str.isupper, arg))
    lowCase: int = sum(map(str.islower, arg))
    puMark: int = sum(1 for c in arg if "\"\'-[]{}()—–…,:;!?.".find(c) != -1)
    space: int = sum(map(str.isspace, arg))
    digit: int = sum(map(str.isdigit, arg))

    print("The text contains", totChar, "characters:")
    print(upCase, "upper letters")
    print(lowCase, "lower letters")
    print(puMark, "punctuation marks")
    print(space, "spaces")
    print(digit, "digits")


def main():
    arg: str = checkInput()
    if len(arg) <= 0:
        return (1)
    parseInput(arg)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(error)
