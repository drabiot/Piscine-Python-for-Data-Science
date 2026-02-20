def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[int | float]:
    """
    Return Body Mass Index's list calculated with
    a given height list & a given wight list
    """
    bmi: list[int | float] = []
    iteration = min(len(weight), len(height))
    for i in range(iteration):
        if (
            isinstance(weight[i], (int, float))
            and isinstance(height[i], (int, float))
        ):
            bmi.append(weight[i] / (height[i] * height[i]))
        else:
            return (bmi)
    return (bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Returns a boolean list if a given BMI list
    is greater than a given value
    """
    ret: list[bool] = []
    for element in bmi:
        if (element > limit):
            ret.append(True)
        else:
            ret.append(False)
    return (ret)
