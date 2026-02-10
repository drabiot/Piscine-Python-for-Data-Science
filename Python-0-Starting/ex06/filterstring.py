from sys import argv
from ft_filter import ft_filter


def main():
    assert len(argv) > 2 and len(argv) < 4
    assert argv[2].isdigit()
    it = int(argv[2])
    st = argv[1].split(None)
    print([i for i in ft_filter(lambda x: len(x) == it, st)])


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError: the arguments are bad")
