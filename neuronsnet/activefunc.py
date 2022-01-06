
import math
from typing import Callable


def sigmoid_func(z: float) -> float:
    ''' 1/(1 + e^{-x})'''
    p: float = 1 + math.exp(-z)
    return 1/p


def sigmoid_func_derivative(a: float) -> float:
    f: Callable[[float], float] = sigmoid_func
    return f(a)*(1-f(a))


def loss_4_sigmoid(y_expected: float, y_pred: float) -> float:
    pass
# https://zhuanlan.zhihu.com/p/79657669
# 对于回归问题，对out直接计算损失，损失函数为MSE
# 对于分类问题，out后接softmax进行分类，然后使用CE(cross entropy)计算loss.
