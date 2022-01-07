
import math
from typing import Callable, List
import numpy as np


def sigmoid(z: float) -> float:
    ''' 1/(1 + e^{-x})'''
    p: float = 1 + math.exp(-z)
    return 1/p


def sigmoid_derivative(a: float) -> float:
    '''f(a)*(1-f(a))'''
    f: Callable[[float], float] = sigmoid
    return f(a)*(1-f(a))


def softmax(Y: List[float]) -> List[float]:
    '''激活函数'''
    s: float = 0
    for y in Y:
        s = sum + math.exp(y)

    return [math.exp(i)/s for i in Y]


def meansquarederror(y_expected: List[float], y_pred: List[float]) -> float:
    '''损失函数: 均方误差'''
    ye = np.array(y_expected)
    yp = np.array(y_pred)
    diff = ye - yp
    return np.sum(diff**2)/len(y_expected)


def meansquarederror_derivative(y_expected: List[float], y_pred: List[float]) -> float:
    '''损失函数偏导数，求delta: 均方误差偏导数'''
    ye = np.array(y_expected)
    yp = np.array(y_pred)
    diff = yp-ye
    return np.sum(diff*2)/len(y_expected)

# https://zhuanlan.zhihu.com/p/79657669
# 对于回归问题，对out直接计算损失，损失函数为MSE
# 对于分类问题，out后接softmax进行分类，然后使用CE(cross entropy)计算loss.
