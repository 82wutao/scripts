
import math
from typing import Callable, Dict, List,   TypeVar
import numpy as np
import functools as util_funcs

LossFunc = Callable[[List[float], List[float]], float]
LossFuncDerivative = Callable[[List[float], List[float]], List[float]]

ActiveFunc = Callable[[List[float]], List[float]]
ActiveFuncDerivative = Callable[[List[float]], List[float]]

ActiveDerivativeBuilder = Callable[[List[float]], ActiveFuncDerivative]


def active_sigmoid(Z: List[float]) -> List[float]:
    ''' 1/(1 + e^{-x})'''
    ret: List[float] = [1/(1 + math.exp(-z)) for z in Z]
    return ret


def active_softmax(Y: List[float]) -> List[float]:
    '''激活函数'''
    a: float = max(Y)

    s: float = 0
    exp_yi: List[float] = []
    for yi in Y:
        r: float = math.exp(yi-a)
        s = s + r
        exp_yi.append(r)

    return [expi/s for expi in exp_yi]


def sigmoid_derivative(Z: List[float]) -> List[float]:
    '''f(a)*(1-f(a))'''
    A: List[float] = active_sigmoid(Z)
    return [a * (1-a)for a in A]


def softmax_derivative(y_expected: List[float], Y_pred: List[float]) -> List[float]:
    '''
    激活函数偏导数，求delta: softmax偏导数\n
    每个xi的 softmax 概率输出都相对yexp =1 的节点概率误差求偏导数
    '''
    return [util_funcs.reduce(lambda s, x:s+x,
                              [Y_pred[i]*(1-Y_pred[j]) if j == i else -(Y_pred[j] * Y_pred[i])
                               for i in range(len(Y_pred)) if y_expected[i] > 0], 0)
            for j in range(len(Y_pred))]


def build_sigmoid_derivative(y_expected: List[float]) -> ActiveFuncDerivative:
    return sigmoid_derivative


def build_softmax_derivative(y_expected: List[float]) -> ActiveFuncDerivative:
    def _wrap(Y_pred: List[float]) -> List[float]:
        return softmax_derivative(y_expected, Y_pred)
    return _wrap


def loss_meansquarederror(y_expected: List[float], y_pred: List[float]) -> float:
    '''损失函数: 均方误差'''
    ye = np.array(y_expected)
    yp = np.array(y_pred)
    diff = ye - yp
    return np.sum(diff**2)/len(y_expected)


def loss_crossentropy(y_expected: List[float], y_pred: List[float]) -> float:
    '''损失函数: 交叉熵'''
    cost: float = util_funcs.reduce(lambda s, x: -(x[0] * math.log(x[1]))+s,
                                    [expected_pred for expected_pred in zip(y_expected, y_pred) if expected_pred[0] > 0], 0)
    return cost


def meansquarederror_derivative(y_expected: List[float], y_pred: List[float]) -> List[float]:
    '''损失函数偏导数，求delta: 均方误差偏导数'''

    n: int = len(y_pred)
    return [(ep[1]-ep[0]) * 2 / n for ep in zip(y_expected, y_pred)]


def crossentropy_derivative(y_expected: List[float], y_pred: List[float]) -> List[float]:
    '''损失函数偏导数，求delta: 交叉熵偏导数。softmax 的每个概率输出的偏导数都一样'''
    delta: float = util_funcs.reduce(lambda s, x: -(x[0]/x[1]) + s,
                                     [expected_pred for expected_pred in zip(y_expected, y_pred) if expected_pred[0] > 0], 0)
    ret: List[float] = [delta for i in range(len(y_pred))]
    return ret


s_r = active_softmax([2, 3, 4])
print("softmax {}".format(s_r))

sd_r = softmax_derivative([0, 1, 0], s_r)
print("softmax_derivative {}".format(sd_r))

cd_r = crossentropy_derivative([0, 1, 0], s_r)
print([z[0] * z[1] for z in zip(sd_r, cd_r)])
