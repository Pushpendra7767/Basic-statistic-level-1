# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# print dataset
sw = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Q9b.csv")
sw.columns
sw1=sw.columns
print(sw1)
# print skewnesws & kurtosis 
sw.skew()
sw.kurt()
sw.corr()
sw.head()
# print max & min, plot histogram, bar and categorise.
# column sp
sw["SP"].max()
sw["SP"].min()
plt.hist(sw['SP'],edgecolor='k')
s1 = [i for i in sw.SP if (i>=98) & (i<115)]
s2 = [i for i in sw.SP if (i>=115) & (i<130)]
s3 = [i for i in sw.SP if (i>=130) & (i<175)]
S4 = [len(s1),len(s2),len(s3)]
S5 = ["98-115","115-130","130-175"]
for i, v in enumerate(S4):
    plt.text(i-.25, 
              v, 
              S4[i], 
              fontsize=18, 
              color="red")
plt.bar(S5,S4)
plt.xticks(S5,rotation=90)
# column wt
sw["WT"].max()
sw["WT"].min()
plt.hist(sw['SP'],edgecolor='k')
w1 = [i for i in sw.WT if (i>=14) & (i<30)]
w2 = [i for i in sw.WT if (i>=30) & (i<35)]
w3 = [i for i in sw.WT if (i>=35) & (i<55)]
W4 = [len(w1),len(w2),len(w3)]
W5 = ["14-30","30-35","35-55"]
for i, v in enumerate(W4):
    plt.text(i-.25, 
              v, 
              W4[i], 
              fontsize=18, 
              color="red")
plt.bar(W5,W4)
plt.xticks(W5,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# sp
sw['SP'].skew()
sw['SP'].kurt()
plt.hist(sw['SP'],edgecolor='k')
sns.distplot(sw['SP'],hist=False)
plt.boxplot(sw['SP'])
# wt
sw['WT'].skew()
sw['WT'].kurt()
plt.hist(sw['WT'],edgecolor='k')
sns.distplot(sw['WT'],hist=False)
plt.boxplot(sw['WT'])
# plot graph between waist and AT
df=pd.crosstab(sw['SP'],sw['WT'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# visulization
plt.plot(np.arange(81),sw.SP)
plt.plot(np.arange(81),sw.WT)
plt.plot(np.arange(81),sw.SP,"ro-")
plt.plot(np.arange(81),sw.WT,"ro-")
sw.SP.value_counts().plot(kind="pie")
sw.SP.value_counts().plot(kind="bar")
plt.plot(sw.SP,sw["WT"],"ro");plt.xlabel("SP");plt.ylabel("WT")
# print correlation.
sw.SP.corr(sw.WT)



























