import numpy as np


def sigmoid_forward(x: np.ndarray) -> np.ndarray:
    result=np.clip(x,-500,500)
    return 1.0/(1.0+np.exp(-result))
    pass


def sigmoid_backward(grad_output: np.ndarray, output: np.ndarray) -> np.ndarray:
    return grad_output *output*(1.0-output)
    pass
