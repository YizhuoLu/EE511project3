import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GMM

Y=[]
for i in range(300):
    mu, sigma = 0, 1
    z1 = np.random.normal(mu, sigma)
    z2 = np.random.normal(mu, sigma)
    Z = [z1, z2]
    # set mu1, mu2, sigma1, sigma2, sigma21
    mu1, mu2, sigma1, sigma2, sigma21 = 5, 10, 1, 1, 0
    c11 = np.sqrt(sigma1)
    c22 = np.sqrt(sigma2)
    c21 = sigma21 / (np.sqrt(sigma1))
    X1 = mu1 + c11 * z1
    X2 = mu2 + c21 * z1 + c22 * z2
    X = [X1, X2]
    Y.append(X)
# data = np.array(Y)
# for i in range(len(Y)):
#     plt.scatter(Y[i][0],Y[i][1],c='b')
# plt.show()
(pmu, ppi, psigma)= GMM.fit(Y)
print('the predicted mu is:', pmu)
print('the predicted weight is:', ppi)
print('the predicted variance is:', psigma)