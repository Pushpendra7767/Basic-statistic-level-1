# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as plt
# print dataset
mba = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\1 SC\\Basic statistics level 1\\mba.csv")
mba.columns
mb=mba.columns
print(mb)
# print skewnesws & kurtosis 
mba.skew()
mba.kurt()
mba['gmat'].skew()
mba['gmat'].kurt()
k=list(mba.index)
# categorise thew dataset and plot distplot, boxplot, histogram & barplot.
plt.hist(mba['gmat'],edgecolor='k')
sns.distplot(mba['gmat'],hist=False)
plt.boxplot(mba['gmat'])
plt.boxplot(mba['gmat'],1,'rs',0)

index = np.arange(773)
mba.shape
# plot bar graph category wise
x1 = [i for i in mba.gmat if (i>650) & (i<700)]
x2 = [i for i in mba.gmat if (i>600) & (i<650)]
x3 = [i for i in mba.gmat if (i>700) & (i<750)]
x4 = [i for i in mba.gmat if (i>750) & (i<800)]
X5 = [len(x1),len(x2),len(x3),len(x4)]
X6 = ["650-700","600-650","700-750","750-800"]
for i, v in enumerate(X5):
    plt.text(i-.25, 
              v, 
              X5[i], 
              fontsize=18, 
              color="red")
plt.bar(X6,X5)





















































