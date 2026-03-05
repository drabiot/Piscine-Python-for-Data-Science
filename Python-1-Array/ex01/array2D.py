from numpy import size


def checkSize(array: list) -> bool:
    """
    Check if the list have the same length everywhere
    """
    baseValue: int = size(array[0], 0)
    try:
        for i in array:
            assert size(i, 0) == baseValue
    except AssertionError:
        return (False)
    return (True)


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice the given list by his start index, to his end index
    Print his original size, the his sliced size
    Return the sliced list
    """
    try:
        assert isinstance(family, list), "Not a list"
        assert isinstance(start, int), "Start isn't an int"
        assert isinstance(end, int), "End isn't an int"
        assert checkSize(family), "List isn't the same length"
        print("My shape is :", (size(family, 0), size(family, 1)))
        slicedFam = family[start:end]
        print("My new shape is :", (size(slicedFam, 0), size(slicedFam, 1)))
        return (slicedFam)
    except AssertionError as msg:
        msg = str(msg)
        if (msg):
            print("Error:", msg)
        return (None)
