import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
import csv

f = open('nips-87-92.csv', 'r')
csv_f = csv.reader(f)
row = list(csv_f)
m = np.array(row)
df = pd.DataFrame(m)
# 11463
columns = df.shape[1] - 2
rows = df.shape[0] - 1
f.close()
X = m[:,2:len(row[0])]
print(X[1][0])
# k means determine k
elbow = []
K = range(1, 30)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    elbow.append([k, kmeanModel.inertia_])
E = np.array(elbow)
# print(kmeanModel.labels_)
# Plot the elbow
plt.plot(E[:, 0], E[:, 1], 'bx-')
plt.xlabel('k')
plt.ylabel('Sum of squared errors')
plt.title('The Elbow Method showing the optimal k')
plt.show()

