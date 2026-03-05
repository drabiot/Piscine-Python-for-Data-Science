import numpy as np


def checkValues(lst: list[int | float]) -> bool:
    """
    Check if the vaues of a given list is an int or a float
    """
    try:
        for i in lst:
            assert isinstance(i, int) or isinstance(i, float)
        return (True)
    except AssertionError:
        return (False)


def checkDiv(lst: list[int | float]) -> bool:
    """
    Check if value in the given list is equal to 0
    """
    try:
        for i in lst:
            assert not i == 0
        return (True)
    except AssertionError:
        return (False)


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Return Body Mass Index's list calculated with
    a given height list & a given wight list
    """
    try:
        assert len(height) == len(weight), "Height & Weight isn't same size"
        assert checkValues(height), "Height values isn't int nor float"
        assert checkValues(weight), "Weight values isn't int nor float"
        assert checkDiv(height), "Division by 0"
        return [(y / (x ** 2)) for x, y in zip(height, weight)]
    except AssertionError as msg:
        print("Error:", msg)
        return (None)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a boolean list if a given BMI list
    is greater than a given value
    """
    arr = np.array(bmi, dtype=float)
    return (arr > limit).tolist()
