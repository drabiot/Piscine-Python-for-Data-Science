import numpy


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    bmi: list[int | float] = []
    iteration = min(len(weight), len(height))
    for i in range (iteration):
        bmi.append(weight[i] / (height[i] * height[i]))
    return (bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ret: list[bool] = []
    for element in bmi:
        if (element > limit):
            ret.append(True)
        else:
            ret.append(False)
    return (ret)
