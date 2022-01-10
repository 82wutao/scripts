from neuralnetworks.utils import csvloader
from neuralnetworks.nn import NeuralNetframework, Layer
from neuralnetworks import activefunc

dataset = csvloader.load_csv(
    "./neuralnetworks/dataset/iris_training.csv", None)

# self,
#                  layers: List[Tuple[int, activefunc.ActiveFunc, activefunc.ActiveDerivativeBuilder]],
#                  loss: activefunc.LossFunc,
#                  loss_derivative: activefunc.LossFuncDerivative
nn: NeuralNetframework = NeuralNetframework(
    [(4, activefunc.active_sigmoid, activefunc.build_sigmoid_derivative),
     (3, activefunc.active_softmax, activefunc.build_softmax_derivative)],
    activefunc.loss_crossentropy, activefunc.crossentropy_derivative)
#
nn.train([r[0] for r in dataset], [r[1] for r in dataset], 100, 0.1)
