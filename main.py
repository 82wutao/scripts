from neuralnetworks.utils import csvloader
from neuralnetworks.nn import NeuralNetframework, Layer
from neuralnetworks import activefunc

dataset = csvloader.load_csv(
    "./neuralnetworks/dataset/iris_training.csv")
# in epoches 9999 loss 0.8294268157786799
# layer 0 weights:[[0.07936480923767208, 0.37723050341958186, 0.3419781865221889, 0.7745148676208496], [0.965294469583258, 0.07604943413014098, 0.3485292224485582, 0.35810721874890894], [0.009253964986268626, 0.3123876964616181, 0.5855216999159443, 0.45061720597861643], [0.07226851220932429, 0.8776978475427005, 0.5583419574408577, 0.9680996056059389]] bs:[0.6735796530065276, 0.9362796960926533, 0.47566757485340916, 0.2987653973174743]
# layer 1 weights:[[18.52722778905485, -20.09986844808617, 1.6455632493966692], [-32.15469710509327, 11.125755820726484, 20.914713344450362], [-11.99654757094309, 7.8107960054183305, 4.323316928916304], [10.700248526089878, 1.398912156627498, -11.755964135305815]] bs:[15.216904239337046, -0.00038831466809942025, -14.654651080939518]


nn: NeuralNetframework = NeuralNetframework(
    [(16, activefunc.active_sigmoid, activefunc.build_sigmoid_derivative),
     #  (5, activefunc.active_sigmoid, activefunc.build_sigmoid_derivative),
     #(4, activefunc.active_sigmoid, activefunc.build_sigmoid_derivative),
     (3, activefunc.active_softmax, activefunc.build_softmax_derivative)],
    activefunc.loss_crossentropy, activefunc.crossentropy_derivative)
#
nn.train([r[0] for r in dataset], [r[1] for r in dataset], 10000, 0.02)
