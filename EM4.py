import xlrd
from sklearn.mixture import GaussianMixture

file_location = "E:\\pycharm\\projects\\511project3\\test faith data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
data=[]
for i in range(272):
    data.append([sheet.cell_value(i,1),sheet.cell_value(i,2)])
gmm = GaussianMixture(n_components=2)
gmm.fit(data)
print('mu:',gmm.means_)
print('cov:',gmm.covariances_)
print('weight:',gmm.weights_)
