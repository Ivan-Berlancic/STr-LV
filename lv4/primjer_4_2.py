import numpy as np
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

def non_func(x):
    y = 1.6345 - 0.6235*np.cos(0.6067*x) - 1.3501*np.sin(0.6067*x) - 1.1622 * np.cos(2*x*0.6067) - 0.9443*np.sin(2*x*0.6067)
    return y

def add_noise(y):
    np.random.seed(14)
    varNoise = np.max(y) - np.min(y)
    y_noisy = y + 0.1*varNoise*np.random.normal(0,1,len(y))
    return y_noisy
 
x = np.linspace(1,10,50)
y_true = non_func(x)
y_measured = add_noise(y_true)

x = x[:, np.newaxis]
y_measured = y_measured[:, np.newaxis]

# make polynomial features
poly2 = PolynomialFeatures(degree=2)
poly6 = PolynomialFeatures(degree=6)
poly15 = PolynomialFeatures(degree=15)

xnew2 = poly2.fit_transform(x)
xnew6 = poly6.fit_transform(x)
xnew15 = poly15.fit_transform(x)

np.random.seed(12)
indeksi = np.random.permutation(len(xnew2))
indeksi_train = indeksi[0:int(np.floor(0.7*len(xnew2)))]
indeksi_test = indeksi[int(np.floor(0.7*len(xnew2)))+1:len(xnew2)]

xtrain2 = xnew2[indeksi_train,]
xtrain6 = xnew6[indeksi_train,]
xtrain15 = xnew15[indeksi_train,]

ytrain = y_measured[indeksi_train]

xtest2 = xnew2[indeksi_test,]
xtest6 = xnew6[indeksi_test,]
xtest15 = xnew15[indeksi_test,]

ytest = y_measured[indeksi_test]

linearModel2 = lm.LinearRegression()
linearModel6 = lm.LinearRegression()
linearModel15 = lm.LinearRegression()

linearModel2.fit(xtrain2, ytrain)
linearModel6.fit(xtrain6, ytrain)
linearModel15.fit(xtrain15, ytrain)

ytest_p2 = linearModel2.predict(xtest2)
ytest_p6 = linearModel6.predict(xtest6)
ytest_p15 = linearModel15.predict(xtest15)

MSE_test2 = mean_squared_error(ytest, ytest_p2)
MSE_test6 = mean_squared_error(ytest, ytest_p6)
MSE_test15 = mean_squared_error(ytest, ytest_p15)

plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.plot(xtest2[:,1],ytest_p2,'og',label='predicted')
plt.plot(xtest2[:,1],ytest,'or',label='test')
plt.legend(loc = 4)
plt.title(f"2-degree polynomial (MSE = {MSE_test2:.2f})")

plt.subplot(2,2,2)
plt.plot(xtest6[:,1],ytest_p6,'og',label='predicted')
plt.plot(xtest6[:,1],ytest,'or',label='test')
plt.legend(loc = 4)
plt.title(f"6-degree polynomial (MSE = {MSE_test6:.2f})")

plt.subplot(2,1,2)
