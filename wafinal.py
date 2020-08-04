# import pacakages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# print dataset
wa = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Basic statistics level 1\\wc.csv")
wa.columns
wa1=wa.columns
print(wa1)
# print skewness and kurtosis of dataset
wa.skew()
wa.kurt()
wa.corr()
wa.head()
# print max & min, plot histogram, bar and categorise.
# column waist
wa["Waist"].max()
wa["Waist"].min()
plt.hist(wa['Waist'],edgecolor='k')
w1 = [i for i in wa.Waist if (i>=60) & (i<80)]
w2 = [i for i in wa.Waist if (i>=80) & (i<100)]
w3 = [i for i in wa.Waist if (i>=100) & (i<125)]
W4 = [len(w1),len(w2),len(w3)]
W5 = ["60-80","80-100","100-125"]
for i, v in enumerate(W4):
    plt.text(i-.25, 
              v, 
              W4[i], 
              fontsize=18, 
              color="red")
plt.bar(W5,W4)
plt.xticks(W5,rotation=90)
# column AT
wa["AT"].max()
wa["AT"].min()
plt.hist(wa['AT'],edgecolor='k')
a1 = [i for i in wa.AT if (i>=10) & (i<70)]
a2 = [i for i in wa.AT if (i>=70) & (i<140)]
a3 = [i for i in wa.AT if (i>=140) & (i<260)]
A4 = [len(a1),len(a2),len(a3)]
A5 = ["10-70","70-140","140-260"]
for i, v in enumerate(A4):
    plt.text(i-.25, 
              v, 
              A4[i], 
              fontsize=18, 
              color="red")
plt.bar(A5,A4)
plt.xticks(A5,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# waist
wa['Waist'].skew()
wa['Waist'].kurt()
plt.hist(wa['Waist'],edgecolor='k')
sns.distplot(wa['Waist'],hist=False)
plt.boxplot(wa['Waist'])
# AT
wa['AT'].skew()
wa['AT'].kurt()
plt.hist(wa['AT'],edgecolor='k')
sns.distplot(wa['AT'],hist=False)
plt.boxplot(wa['AT'])

# plot graph between waist and AT
df=pd.crosstab(wa['Waist'],wa['AT'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# visulization
plt.plot(np.arange(109),wa.Waist)
plt.plot(np.arange(109),wa.AT)
plt.plot(np.arange(109),wa.Waist,"ro-")
plt.plot(np.arange(109),wa.AT,"ro-")
wa.Waist.value_counts().plot(kind="pie")
wa.Waist.value_counts().plot(kind="bar")
plt.plot(wa.Waist,wa["AT"],"ro");plt.xlabel("Waist");plt.ylabel("AT")
# print correlation.
wa.Waist.corr(wa.Waist)
wa.Waist.corr(wa.AT)









