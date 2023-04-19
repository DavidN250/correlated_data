#import libraries

import numpy as np
from numpy.random import multivariate_normal

#Declare the correlation matrix, it has to be a square matrix

cov_matrix =[[1,0.21,0.56,0.36,0.67],
             [0.21,1,0.68,0.15,0.64],
             [0.56,0.68,1,0.11,0.79],
             [0.36,0.15,0.11,1,0.41],
             [0.67,0.64,0.79,0.411,1]]

#Generate Data using multivariate_normal

data = multivariate_normal([0,0,0,0,0],cov_matrix,size=100) #this will generate 100 random values

#Save data in csv file

np.savetxt("generated_data.csv",data,delimiter=",")

#Display data in console if you want

for record in data:
    print(record)
