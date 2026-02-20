import numpy as np


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Return Body Mass Index's list calculated with
    a given height list & a given wight list
    """
    if len(height) != len(weight):
        print("Error: Height list & Weight list aren't the same size")
        return None
    try:
        h = np.array(height, dtype=float)
        w = np.array(weight, dtype=float)
    except (ValueError, TypeError):
        print("Error: Need only digit")
        return None
    if np.any(h == 0):
        print("Error: Can't divide by 0")
        return None
    return (w / (h ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a boolean list if a given BMI list
    is greater than a given value
    """
    arr = np.array(bmi, dtype=float)
    return (arr > limit).tolist()
