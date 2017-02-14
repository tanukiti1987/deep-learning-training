import numpy as np
import matplotlib.pylab as plt

# from step import step_function

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
