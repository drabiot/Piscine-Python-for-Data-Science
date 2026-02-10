import sys
from ft_filter import ft_filter


def main():
    assert len(sys.argv) > 1 and len(sys.argv) <= 3, "AssertionError: the arguments are bad"
    assert sys.argv[2].isdigit(), "AssertionError: the arguments are bad"
    print([i for i in ft_filter(lambda x : len(x) == int(sys.argv[2]), sys.argv[1].split(None))])


if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(error)
