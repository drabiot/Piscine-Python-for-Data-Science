def count_in_list(liste: list, search: str) -> int:
    """
    return how many times a given string occur in a given list
    """
    ret: int = 0
    for element in liste:
        if (element == search):
            ret = ret + 1
    return (ret)
