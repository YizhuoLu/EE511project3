import matplotlib.pyplot as plt
import xlrd

file_location = "E:\\pycharm\\projects\\511project3\\test faith data1.xlsx"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
x=[]
y=[]
for i in range(272):
    x.append(sheet.cell_value(i,1))
    y.append(sheet.cell_value(i,2))
plt.scatter(x,y,c='blue',alpha=0.5)
plt.title('scatter plot')
plt.xlabel('Eruption time in mins')
plt.ylabel('Waiting time to next eruption')
plt.show()
