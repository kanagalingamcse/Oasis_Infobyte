# -*- coding: utf-8 -*-
"""CAR_PRICE_PREDICTION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWffrctbPLs7w7NwDN_T5J5-FGhvc3jd

# **CAR PRICE PREDICTION WITH MACHINE LEARNING**

![09.jpg](data:image/jpeg;base64,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AYOpmABBBBY88888888888888888884rtuGLBBDV8rBOH9ICCKc88888888888888rAS83TOLBeFBBiBWAH5AE888888888888888885DAmmBBRLH5BpBBBBRtduYd88888888888888888hBXzJLBPlW4BqBBBBBBzbV088888888888888888oBOICEXiHUe1jBBBBBBWiBB878888888888888888PjBC6ZBBCBABBBBBBBCCBBBBDZ88888888888888trsCpgBBBBBBOGkGIMOsILBBBRz888888888F3888iiELBBBBBAOO98M999XtIlBAEH888888884/hzzzgxBMECCNRhQyzO9U++IyyCfL3nX8888885yMnABBQoLX6z9z888889/88888888nmXf+98888d8QWDBBDFld4Uy0888888888888808K8gOGW8888hmvhLBBExD888xLq88888888884WRUMe7Wd888889CI3/AEU4MPLHe88xxxxxxxww0j/8AGOZMWTPPPPPPI9XP/wD8Xi3nb4pkX/8A/wD/AP8A46+GsrxV/cZk88888888c/cONccV0Vw4mdwww840wppuVMuOs/M88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888/8QAJhEAAwACAgICAgEFAAAAAAAAAAERITEQIEFhMEBRkYFwcYCx0f/aAAgBAwEBPxD/AAEqKioqKil6IYvtv4l9+Ia+BMpSl+4+tSE09d0/rUpSsr6vbgWwNx6c7Fv6rfFXeChFVmRekPWeyqqKKdV9WyIWeSGMYmkq5qK3pG6poKS0aF4NGbshCE+g3FR+XgPiSkKKqxibhGTI0LSDE6MnsJJcUVKqMSovZgWkRUIU/pN8NVQUPA/P/RsHnrC1aqmLZRjnN3PahjR6A1r9M98MfyCOQ17G/wA9EIQ86CnOkXGKpo/kmBtlW38iZO7SYigsfTa4psajzxsc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)

Download **Dataset here [CAR PRICE PREDICTION](https://drive.google.com/file/d/1EUfj25s3IVVe4Kxrz1hmf9QCSzy_G6Dh/view?usp=share_link)**

### Knowing about the Dataset

**Importing the Required Libraries**
"""

# Numpy Library for Numerical Calculations
import numpy as np

# Pandas Library for Dataframe
import pandas as pd

# Math Library for Mathematical Calulations
import math

# Pickle Library for Saving the Model
import pickle

# Matplotlib and Seaborn for Plottings
import matplotlib.pyplot as plt
import seaborn as sns

# Train_Test_Split for splitting the Dataset
from sklearn.model_selection import train_test_split

# Linear Regression, Decision Tree are Models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

# Mean Absolute Error, R2 Score and Mean Squared Error is for Analysis of Models
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error
from sklearn.metrics import accuracy_score

from google.colab import drive
drive.mount('/content/drive')

"""**Reading informations in the Dataset**"""

car_price = pd.read_csv("/content/drive/MyDrive/Oasis Infobyte/Data Science - Internship/Car-Price-Prediction/CarPrice.csv")

"""**Checking for null values in Data**"""

car_price.isnull().sum()

"""**Checking the First Five Values in the Data**"""

car_price.head()

"""**Checking the Last Five Values in the Data**"""

car_price.tail()

"""**Dimensions of the Dataset**"""

car_price.shape

"""**Describing the Dataset**"""

car_price.describe()

"""**Checking for the classes in the Data**"""

car_price.groupby('carbody').size()

"""**Taking the required Informations**"""

car = car_price[["symboling", "wheelbase", "carlength", "carwidth", "carheight", "curbweight", "enginesize", "boreratio", "stroke", "compressionratio", "horsepower", "peakrpm", "citympg", "highwaympg", "price"]]
car

"""**Plotting the Bivariate Bar for the Dataset**"""

def plot_bivariate_bar(dataset, cols, width, height, hspace, wspace):
    dataset = dataset.select_dtypes(include = [np.int64])
    plt.style.use('seaborn-whitegrid')
    fig = plt.figure(figsize=(width, height))
    fig.subplots_adjust(left = None, bottom = None, right = None, top = None, wspace = wspace, hspace = hspace)
    rows = math.ceil(float(dataset.shape[1]) / cols)
    for i, column in enumerate(dataset.columns):
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.set_title(column)
        if dataset.dtypes[column] == np.int64:
            g = sns.countplot(y = column, data = dataset)
            substrings = [s.get_text()[:15] for s in g.get_yticklabels()]
            g.set(yticklabels = substrings)

plot_bivariate_bar(car, cols = 5, width = 20, height = 15, hspace = 0.2, wspace = 0.5)

"""**Plotting the Joint Plot for the Dataset**"""

plt.figure(figsize = (10, 10))
sns.jointplot(data = car)
plt.show()

"""**Plotting the Correlation Matrix of the Dataset**"""

plt.figure(figsize = (20, 10))
sns.set_style('darkgrid')
sns.heatmap(car.corr(), annot = True, cmap = 'viridis')
plt.show()

x = car.drop(["price"], 1)
y = car["price"]
xtrain, xtest, ytrain, ytest = train_test_split(x, y, random_state = 16, test_size = 0.25, shuffle=True)

"""### Model Building

**Creating the Model**
"""

model1 = LinearRegression()
model2 = DecisionTreeRegressor()

"""**Fitting the Model**"""

model1.fit(xtrain, ytrain)
model1.score(xtrain, ytrain)

model2.fit(xtrain, ytrain)
model2.score(xtrain, ytrain)

"""### Testing Model

**Testing the Model**
"""

Linear_predictions = model1.predict(xtest)
Decision_predictions = model2.predict(xtest)

"""**Metrics**"""

print("Linear Regression Model:")
print("************************")
print('R2_score:', r2_score(ytest, Linear_predictions))
print('Mean Absolute Error:', mean_absolute_error(ytest, Linear_predictions))
print('Mean Squared Error:', mean_squared_error(ytest, Linear_predictions))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(ytest, Linear_predictions)))
print("---------------------------------------------")
print("Decision Tree Regression Model:")
print("******************************")
print('R2_score:', r2_score(ytest, Decision_predictions))
print('Mean Absolute Error:', mean_absolute_error(ytest, Decision_predictions))
print('Mean Squared Error:', mean_squared_error(ytest, Decision_predictions))
print('Root Mean Squared Error:', np.sqrt(mean_squared_error(ytest, Decision_predictions)))

print("Accuracy of Linear Regression Model: ", model1.score(xtrain, ytrain))
print("Accuracy of Decision Tree Regression Model: ", model2.score(xtrain, ytrain))

"""### Saving Models

**Saving the Models**
"""

filename = "Linear_Regression.pkl"
pickle.dump(model1, open(filename, 'wb'))
filename = "Decision_Tree_Regressor.pkl"
pickle.dump(model2, open(filename, 'wb'))
print("Saved all Models")