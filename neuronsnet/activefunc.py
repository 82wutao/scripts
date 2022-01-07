
import math
from typing import Callable, List
import numpy as np


def sigmoid_func(z: float) -> float:
    ''' 1/(1 + e^{-x})'''
    p: float = 1 + math.exp(-z)
    return 1/p


def sigmoid_func_derivative(a: float) -> float:
    f: Callable[[float], float] = sigmoid_func
    return f(a)*(1-f(a))


def softmax(yi: float, yc: List[float]) -> float:
    sum: float = 0
    for y in yc:
        sum = sum + math.exp(y)

    return math.exp(yi)/sum


def loss_mse(y_expected: List[float], y_pred: List[float]) -> float:
    '''Mean Squared Error 均方误差'''
    ye = np.array(y_expected)
    yp = np.array(y_pred)
    diff = ye - yp
    return np.sum(diff**2)/len(y_expected)
# https://zhuanlan.zhihu.com/p/79657669
# 对于回归问题，对out直接计算损失，损失函数为MSE
# 对于分类问题，out后接softmax进行分类，然后使用CE(cross entropy)计算loss.
