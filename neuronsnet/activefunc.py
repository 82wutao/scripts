
import math
from typing import Callable


def sigmoid_func(z: float) -> float:
    ''' 1/(1 + e^{-x})'''
    p: float = 1 + math.exp(-z)
    return 1/p


def sigmoid_func_derivative(a: float) -> float:
    f: Callable[[float], float] = sigmoid_func
    return f(a)*(1-f(a))
