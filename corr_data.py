import numpy as np
from numpy.random import multivariate_normal
# import pandas as pd
# import openpyxl as xls
# import matplotlib.pyplot as plt


cov_matrix =[[1,0.21,0.56,0.36,0.67],
             [0.21,1,0.68,0.15,0.64],
             [0.56,0.68,1,0.11,0.79],
             [0.36,0.15,0.11,1,0.41],
             [0.67,0.64,0.79,0.411,1]]

data = multivariate_normal([0,0,0,0,0],cov_matrix,size=3000)
np.savetxt("data.csv",data,delimiter=",")

# for i in range(29):
#    gen_arr = multivariate_normal([0,0,0,0,0],cov_matrix,size=100)
#    data = np.concatenate((data,gen_arr),axis=0)

for d in data:
    print(d)

# print(data)
# print(data.shape)