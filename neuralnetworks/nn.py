

import numpy as np
from typing import List, NoReturn, Tuple, TypeVar


from neuralnetworks import activefunc
from neuralnetworks.activefunc import active_softmax


class Layer:

    def __init__(self, nodes: int, weights: int,
                 active_func: activefunc.ActiveFunc,
                 active_derivative_builder: activefunc.ActiveDerivativeBuilder) -> None:
        self._w_shape: Tuple[int, int] = (weights, nodes)
        self._W: np.matrix = np.random.rand(
            weights * nodes).reshape(weights, nodes)
        self._B: np.ndarray = np.random.rand(nodes)

        self._activefunc = active_func
        self._active_derivative_builder = active_derivative_builder
        self._activefunc_derivative = None

        self._Z: np.matrix = None
        self._A: np.ndarray = None

        self._X_input: np.matrix = None

    def calc_z(self, X: List[float]) -> List[float]:
        self._X_input = np.mat(X)
        self._Z = np.dot(self._X_input, self._W)
        self._Z += self._B
        return self._Z.tolist()

    def calc_a(self) -> List[float]:
        resultset: List[float] = self._activefunc(self._Z.tolist()[0])
        self._A = np.array(resultset)
        return resultset

    def get_Z(self) -> List[float]:
        return self._Z.tolist()[0]

    def get_A(self) -> List[float]:
        return self._A.tolist()

    def update_active_derivate(self, y_exp: List[float]) -> NoReturn:
        self._activefunc_derivative = self._active_derivative_builder(y_exp)

    def gradient_descent(self, delta_next_layer: List[float], weights_next_layer: List[List[float]],
                         learn_rate: float, partial_derivative_arg: List[float]) -> Tuple[List[float], List[List[float]]]:

        DNL: np.matrix = np.mat(delta_next_layer)
        WNL: np.matrix = np.mat(weights_next_layer)
        DCL: np.matrix = np.asarray(np.dot(
            DNL, WNL.T)) * np.array(self._activefunc_derivative(partial_derivative_arg))

        ret: Tuple[List[float], List[List[float]]] = (DCL.tolist()[0],
                                                      self._W.tolist())

        delta_weigts: np.matrix = np.dot(self._X_input.T, DCL)  # TODO 加正则损失
        delta_b: np.ndarray = np.asarray(DCL.tolist()[0])

        self._W = self._W - (learn_rate * delta_weigts)
        self._B = self._B - (learn_rate * delta_b)

        return ret

    def nodes(self) -> int:
        return self._w_shape[1]

    def weights_bs(self) -> Tuple[List[List[float]], List[float]]:
        return (self._W.tolist(), self._B.tolist())


Decimal = TypeVar("Decimal",  int, float)


def generate_eye_matrix(n: int, v: Decimal) -> List[List[Decimal]]:
    matrix: List[List[Decimal]] = []
    for i in range(n):
        row: List[Decimal] = [v if c == i else 0 for c in range(n)]
        matrix.append(row)
    return matrix


class NeuralNetframework:
    _alias_nnfw = TypeVar("_alias_nnfw", bound="NeuralNetframework")

    def __init__(self,
                 layers: List[Tuple[int, activefunc.ActiveFunc, activefunc.ActiveDerivativeBuilder]],
                 loss: activefunc.LossFunc,
                 loss_derivative: activefunc.LossFuncDerivative) -> None:

        self._layers_setting: List[Tuple[int,
                                         activefunc.ActiveFunc, activefunc.ActiveDerivativeBuilder]] = layers
        self._layers: List[Layer] = []

        self._loss: activefunc.LossFunc = loss
        self._loss_derivative: activefunc.LossFuncDerivative = loss_derivative

    def train(self, X: List[List[float]], Y: List[List[float]], epoches: int, learn_rate: float):
        self._layers_setting.insert(0, (len(X[0]), None, None))
        for i in range(1, len(self._layers_setting), 1):
            layer_setting: Tuple(int, activefunc.ActiveFunc,
                                 activefunc.ActiveDerivativeBuilder) = self._layers_setting[i]
            pre_layer_setting: Tuple(int, activefunc.ActiveFunc,
                                     activefunc.ActiveDerivativeBuilder) = self._layers_setting[i-1]
            nodes = layer_setting[0]
            weights = pre_layer_setting[0]
            layer: Layer = Layer(nodes=nodes, weights=weights,
                                 active_func=layer_setting[1], active_derivative_builder=layer_setting[2])
            self._layers.append(layer)
        self._X = X
        self._Y = Y

        for e in range(epoches):
            for x_sample, y_expect in zip(self._X, self._Y):
                y_pred: List[float] = self._feedforward(x_sample)

                # print("debug training x:{},y:{},z:{},softmax{}".format(
                #     x_sample, y_expect, self._layers[-1]._Z.tolist()[0], y_pred))
                self._backpropagation(y_expect, y_pred, learn_rate)
            if e % 100 == 0:
                mean_loss: float = self._test_cost(self._X, self._Y)
                print("in epoches {} loss {}".format(e, mean_loss))

        mean_loss: float = self._test_cost(self._X, self._Y)
        print("in epoches {} loss {}".format(e, mean_loss))

        for li in range(len(self._layers)):
            layer = self._layers[li]
            ws_bs = layer.weights_bs()
            print("layer {} weights:{} bs:{}".format(li, ws_bs[0], ws_bs[1]))

    def _feedforward(self, x: List[float]) -> List[float]:
        _input_x: List[float] = x
        for l in self._layers:
            l.calc_z(_input_x)
            _input_x = l.calc_a()
        return _input_x

    def _test_cost(self, X: List[List[float]], Y: List[List[float]]) -> float:
        # 当前权重参数
        # 得到每个样本的结果，求得 loss
        # sum(loss)/n
        sum: float = 0
        for x_sample, y_expect in zip(X, Y):
            y_pred: List[float] = self._feedforward(x_sample)
            loss: float = self._loss(y_expect, y_pred)
            sum += loss
        return sum/len(X)

    def _backpropagation(self, y_expect: List[float], y_pred: List[float], learn_rate: float):
        delta: List[float] = self._loss_derivative(y_expect, y_pred)

        for l in self._layers[:0:-1]:
            l.update_active_derivate(y_expect)

        out_layer_nodes: int = self._layers[-1].nodes()
        virtual_w: List[List[float]] = generate_eye_matrix(out_layer_nodes, 1)

        weights_next_layer: List[List[float]] = virtual_w
        delta_next_layer: List[float] = delta
        for l in self._layers[:0:-1]:
            output_layer: bool = l._activefunc == activefunc.active_softmax

            partial_derivative_arg: List[float] = l.get_A()
            if not output_layer:
                partial_derivative_arg = l.get_Z()

            delta_next_layer, weights_next_layer = l.gradient_descent(delta_next_layer, weights_next_layer,
                                                                      learn_rate, partial_derivative_arg)
