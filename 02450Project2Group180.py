#Implementation of Classification and Regression.
#Import the necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.linalg import svd
import seaborn as sn

#Load matrix X as csv file
#data is the matrix that contains the data set with the errors changed
data = pd.read_csv('processed.cleveland.data')
real_data = data.values

#X is the matrix that contains the data without the classes
cols = range(0, 13)
cols1 = range(0,14)
cor_data = real_data[:,cols1]
X = real_data[:, cols]
X = np.array(X)

#List with the attributes name
attributeNames = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach',
                  'exang','oldpeak','slope','ca','thal']
