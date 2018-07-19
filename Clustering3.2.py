import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import csv

f = open('nips-87-92.csv', 'r')
csv_f = csv.reader(f)
row = list(csv_f)
m = np.array(row)
df = pd.DataFrame(m)
columns = df.shape[1] - 2
rows = df.shape[0] - 1
f.close()
Y = m[:, 1]
X = m[:,2:len(row[0])]
print(X[1][0])

kmeanModel = KMeans(n_clusters=25).fit(X)
C = []
for i in range(699):
    C.append([Y[i], kmeanModel.labels_[i]])
np.array(C)
for i in range(1,26):
    M = []
    for j in range(699):
        if C[j][1] == i:
            M.append(C[j][0])
    print('label:',i)
    print(M)


