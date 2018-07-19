import xlrd
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

file_location = "E:\\pycharm\\projects\\511project3\\test faith data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
x=[]
y=[]
for i in range(272):
    x.append(sheet.cell_value(i,1))
    y.append(sheet.cell_value(i,2))
P = np.array(list(zip(x, y)))
plt.figure('figure 1')
plt.title('Initial clustering scatter plot')
plt.xlabel('Eruption time in mins')
plt.ylabel('Waiting time to next eruption')
plt.scatter(x, y, c='black', s=7)

# Euclidean Distance equals to vector norms
def dist(a, b, axis1=1):
    return np.linalg.norm(a - b, axis=axis1)

k = 2
C_x = np.random.randint(0, np.amax(x), size=k)
C_y = np.random.randint(0, np.amax(y), size=k)
C = np.array(list(zip(C_x, C_y)), dtype=np.float16)

# plotting aside centroids
plt.scatter(x, y, c='black', s=7)
plt.scatter(C_x, C_y, marker='*', s=200, c='blue')
# plt.show()

# store the value of centroids
C_pre = np.zeros(C.shape)
# the distance between the previous centroid and updated centroid
newdis = dist(C, C_pre, None)
clusters = np.zeros(len(P))
# update the centroids until the newdis equals to zero
while newdis != 0:
    # assign points to its closest centroid
    for i in range(len(P)):
        distances = dist(P[i], C)
        mindis = np.argmin(distances)
        clusters[i] = mindis
    C_pre = deepcopy(C)
    # find new centroids
    for i in range(k):
        points = [P[j] for j in range(len(P)) if clusters[j] == i]
        C[i] = np.mean(points, axis=0)
    newdis = dist(C, C_pre, None)
colors = ['r', 'g']
for i in range(k):
    points = np.array([P[j] for j in range(len(P)) if clusters[j] == i])
    plt.figure('figure 2')
    plt.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
plt.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='black')
plt.title('The last clustering scatter plot')
plt.xlabel('Eruption time in mins')
plt.ylabel('Waiting time to next eruption')
plt.show()