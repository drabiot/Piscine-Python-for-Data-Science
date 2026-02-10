from sys import argv


def translate(s: str) -> str:
    """Translate a given string into morse code"""
    NESTED_MORSE = {
        " ": "/ ", "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ".", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. ",
    }
    i: int = 0
    trans: str = ""
    while i < len(s):
        trans = trans + NESTED_MORSE[s[i]]
        i = i + 1
    return (trans[:-1])


def main():
    assert len(argv) == 2
    for c in argv[1]:
        assert c.isalnum() or c == ' '
    print(translate(argv[1].upper()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError: the arguments are bad")
