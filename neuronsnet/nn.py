
from sys import flags
from typing_extensions import Self
import numpy as np
from typing import Callable, List, NoReturn, Tuple, TypeVar


from neuronsnet import activefunc


ActiveFunction = Callable[[List[float]], List[float]]
DerivativeActiveFunction = Callable[[List[float]], List[float]]

# def active_func(Z: List[float]) -> List[float]:
#     result: List[float] = []
#     for z in Z:
#         r: float = activefunc.sigmoid_func(z)
#         result.append(r)
#     return result


# def active_func_derivative(A: List[float]) -> List[float]:
#     rs: List[float] = []
#     for a in A:
#         r: float = activefunc.sigmoid_func_derivative(a)
#         rs.append(r)
#     return rs


class Layer:

    def __init__(self, nodes: int, weights: int,
                 active_func: ActiveFunction, derivative_active: DerivativeActiveFunction) -> None:
        self._w_shape: Tuple[int, int] = (weights, nodes)
        self._W: np.matrix = np.random.rand(
            weights * nodes).reshape(weights, nodes)
        self._B: np.ndarray = np.random.rand(nodes)

        self._Active_Func = active_func
        self._Derivative_Active = derivative_active

        self._Z: np.ndarray = None
        self._A: np.ndarray = None

        self._X_input: np.ndarray = None
        pass

    def calc_z(self, X: List[float]) -> List[float]:
        self._X_input = np.array(X)
        self._Z = self._X_input.dot(self._W) + self._B
        return self._Z.tolist()

    def calc_a(self) -> List[float]:
        resultset: List[float] = self._Active_Func(self._Z.tolist())
        self._A = np.array(resultset)
        return resultset

    def back(self) -> NoReturn:
        pass


#Trainable = TypeVar('Trainable')
#TagsMapper = Callable[[Trainable], Tuple[List[float], float]]
#''' object => (X[x1,x2,x3,...],y)'''
Loss = Callable[[float, float], float]


class NeuronsNetFramework:
    _alias_nnfw = TypeVar("_alias_nnfw", bound="NeuronsNetFramework")

    def __init__(self, layers: List[Tuple[int, ActiveFunction, DerivativeActiveFunction]], loss: Loss) -> None:
        self._layers_setting: List[Tuple[int,
                                         ActiveFunction, DerivativeActiveFunction]] = layers
        self._loss: Loss = loss
        self._layers: List[Layer] = []
        pass

    @staticmethod
    def build(layers: List[Tuple[int, ActiveFunction, DerivativeActiveFunction]],
              loss: Loss) -> _alias_nnfw:

        framework: NeuronsNetFramework = NeuronsNetFramework(layers, loss)
        return framework

    # def train_obj(X: List[Trainable], mapper: TagsMapper, loss: Loss):
    #     pass

    def set_train_data(self, X: List[List[float]], Y: List[float], input_nodes: int):
        self._layers_setting.insert(0, (input_nodes, None, None))
        for i in range(1, len(self._layers_setting), 1):
            _layer: Tuple(int, ActiveFunction,
                          DerivativeActiveFunction) = self._layers_setting[i]
            _pre_layer: Tuple(int, ActiveFunction,
                              DerivativeActiveFunction) = self._layers_setting[i-1]
            nodes = _layer[0]
            weights = _pre_layer[0]
            self._layers.append(Layer(nodes=nodes, weights=weights,
                                      active_func=_layer[1], derivative_active=_layer[2]))
        self._X = X
        self._Y = Y
        pass

    def train(self, epoches: int):
        # for e in epoches:
        #     for sample in self._X:
        #         _forward()
        #         _cost()
        #         _back()
        #     loss
        pass

    def _forward(self, x: List[float]) -> List[float]:
        _input_x: List[float] = x
        for l in self._layers:
            l.calc_z(_input_x)
            _input_x = l.calc_a()
        return _input_x

    def _cost(self):
        pass

    def _back(self):
        pass
    pass


l = Layer(3, 4)
print(l.calc_z([1, 1, 1, 1]))
print(l.calc_a())
