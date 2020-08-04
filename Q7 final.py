# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# print dataset
car12 = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Q7.csv")
car12.columns
ca34=car12.columns
print(ca34)
# print skewnesws & kurtosis 
car12.skew()
car12.kurt()
car12.corr()
car12.head()
# print max & min, plot histogram, bar and categorise.
# column points
car12["Points"].max()
car12["Points"].min()
plt.hist(car12['Points'],edgecolor='k')
p1 = [i for i in car12.Points if (i>=2) & (i<3)]
p2 = [i for i in car12.Points if (i>=3) & (i<4)]
p3 = [i for i in car12.Points if (i>=4) & (i<5)]
P4 = [len(p1),len(p2),len(p3)]
P5 = ["2-3","3-4","4-5"]
for i, v in enumerate(P4):
    plt.text(i-.25, 
              v, 
              P4[i], 
              fontsize=18, 
              color="red")
plt.bar(P5,P4)
plt.xticks(P5,rotation=90)
# score
car12["Score"].max()
car12["Score"].min()
plt.hist(car12['Score'],edgecolor='k')
s1 = [i for i in car12.Score if (i>=1) & (i<2.5)]
s2 = [i for i in car12.Score if (i>=2.5) & (i<3.5)]
s3 = [i for i in car12.Score if (i>=3.5) & (i<5.5)]
S4 = [len(s1),len(s2),len(s3)]
S5 = ["2-3","3-4","4-5"]
for i, v in enumerate(S4):
    plt.text(i-.25, 
              v, 
              S4[i], 
              fontsize=18, 
              color="red")
plt.bar(S5,S4)
plt.xticks(S5,rotation=90)
# weigh
car12["Weigh"].max()
car12["Weigh"].min()
plt.hist(car12['Weigh'],edgecolor='k')
w1 = [i for i in car12.Weigh if (i>=14) & (i<17)]
w2 = [i for i in car12.Weigh if (i>=17) & (i<19)]
w3 = [i for i in car12.Weigh if (i>=19) & (i<25)]
W4 = [len(w1),len(w2),len(w3)]
W5 = ["14-17","17-19","19-25"]
for i, v in enumerate(W4):
    plt.text(i-.25, 
              v, 
              W4[i], 
              fontsize=18, 
              color="red")
plt.bar(W5,W4)
plt.xticks(W5,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# points
car12['Points'].skew()
car12['Points'].kurt()
plt.hist(car12['Points'],edgecolor='k')
sns.distplot(car12['Points'],hist=False)
plt.boxplot(car12['Points'])
# score
car12['Score'].skew()
car12['Score'].kurt()
plt.hist(car12['Score'],edgecolor='k')
sns.distplot(car12['Score'],hist=False)
plt.boxplot(car12['Score'])
# weigh
car12['Weigh'].skew()
car12['Weigh'].kurt()
plt.hist(car12['Weigh'],edgecolor='k')
sns.distplot(car12['Weigh'],hist=False)
plt.boxplot(car12['Weigh'])
# plot graph between point and model
df=pd.crosstab(car12['Points'],car12['Model'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# visulization
plt.plot(np.arange(32),car12.Points)
plt.plot(np.arange(32),car12.Score)
plt.plot(np.arange(32),car12.Weigh)
plt.plot(np.arange(32),car12.Points,"ro-")
plt.plot(np.arange(32),car12.Score,"ro-")
plt.plot(np.arange(32),car12.Weigh,"ro-")
car12.Points.value_counts().plot(kind="pie")
car12.Points.value_counts().plot(kind="bar")
car12.Points.corr(car12.Points)
car12.Score.corr(car12.Score)
car12.Points.corr(car12.Weigh)
plt.plot(car12.Points,car12["Score"],"ro");plt.xlabel("Points");plt.ylabel("Score")











































