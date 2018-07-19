import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

mu1 = [1, 1]
mu2 = [4, 4]
sigma1 = [[2, 0], [0, 2]]
sigma2 = [[2, 0], [0, 2]]
w = [0.5, 0.5]
N = 300
Y = []
for i in range(N):
    if np.random.uniform(0,1) <= w[0]:
        x1, y1 = np.random.multivariate_normal(mu1, sigma1)
        plt.scatter(x1, y1, c='r')
        Y.append([x1, y1])
    else:
        x2, y2 = np.random.multivariate_normal(mu2, sigma2)
        plt.scatter(x2, y2, c='g')
        Y.append([x2, y2])
gs = np.array(Y)
plt.figure(2)
plt.hist(gs,  bins=np.arange(-4, 10, 0.5), histtype='bar', edgecolor='g', alpha=0.5)
plt.title('histogram of the GMM samples')
plt.xlabel('X')
plt.ylabel('Y')
plt.figure(1)
plt.title('300 GMM samples scatter plot')
plt.xlabel('X')
plt.ylabel('Y')
gmm = GaussianMixture(n_components=2)
gmm.fit(gs)
print('mu:', gmm.means_)
print('cov:', gmm.covariances_)
print('weight:', gmm.weights_)
plt.figure(3)
X1, Y1 = np.meshgrid(np.linspace(-5, 8), np.linspace(-5, 8))
XX = np.array([X1.ravel(), Y1.ravel()]).T
Z = np.log(-gmm.score_samples(XX))
Z = Z.reshape(X1.shape)
plt.contour(X1, Y1, Z)
plt.scatter(gs[:,0], gs[:,1])
plt.title('contour of GMM samples after EM')
plt.axis('tight')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()