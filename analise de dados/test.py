import numpy as np
import pandas as pd

y_true = np.array([1.,2.,1.])
y_pred = np.array([1., 1., 1.])
print(np.sqrt(((y_true-y_pred)**2).mean()))