import math


def euclidean_division(numerator: int, denominator: int) -> tuple[int, int]:
    """Compute the euclidean division of the passed integers"""
    if denominator == 0:
        raise Exception("division by zero")
    quotient = math.floor(numerator / denominator)
    remainder = numerator % denominator
    return quotient, remainder
