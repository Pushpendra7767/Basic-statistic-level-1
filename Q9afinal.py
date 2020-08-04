# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# print dataset
sd = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Q9a.csv")
sd.columns
sd1=sd.columns
print(sd)
# print skewnesws & kurtosis 
sd.skew()
sd.kurt()
sd.corr()
sd.head()
# print max & min, plot histogram, bar and categorise.
# column speed
sd["speed"].max()
sd["speed"].min()
plt.hist(sd['speed'],edgecolor='k')
s1 = [i for i in sd.speed if (i>=3) & (i<12)]
s2 = [i for i in sd.speed if (i>=12) & (i<18)]
s3 = [i for i in sd.speed if (i>=18) & (i<30)]
S4 = [len(s1),len(s2),len(s3)]
S5 = ["4-12","12-18","18-30"]
for i, v in enumerate(S4):
    plt.text(i-.25, 
              v, 
              S4[i], 
              fontsize=18, 
              color="red")
plt.bar(S5,S4)
plt.xticks(S5,rotation=90)
# column dist
sd["dist"].max()
sd["dist"].min()
plt.hist(sd['dist'],edgecolor='k')
d1 = [i for i in sd.dist if (i>=1) & (i<30)]
d2 = [i for i in sd.dist if (i>=30) & (i<60)]
d3 = [i for i in sd.dist if (i>=60) & (i<125)]
D4 = [len(d1),len(d2),len(d3)]
D5 = ["1-30","30-60","60-125"]
for i, v in enumerate(D4):
    plt.text(i-.25, 
              v, 
              D4[i], 
              fontsize=18, 
              color="red")
plt.bar(D5,D4)
plt.xticks(D5,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# speed
sd['speed'].skew()
sd['speed'].kurt()
plt.hist(sd['speed'],edgecolor='k')
sns.distplot(sd['speed'],hist=False)
plt.boxplot(sd['speed'])
# dist
sd['dist'].skew()
sd['dist'].kurt()
plt.hist(sd['dist'],edgecolor='k')
sns.distplot(sd['dist'],hist=False)
plt.boxplot(sd['dist'])
# plot graph between waist and AT
df=pd.crosstab(sd['speed'],sd['dist'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# visulization
plt.plot(np.arange(50),sd.speed)
plt.plot(np.arange(50),sd.dist)
plt.plot(np.arange(50),sd.speed,"ro-")
plt.plot(np.arange(50),sd.dist,"ro-")
sd.speed.value_counts().plot(kind="pie")
sd.speed.value_counts().plot(kind="bar")
plt.plot(sd.speed,sd["dist"],"ro");plt.xlabel("speed");plt.ylabel("dist")
# print correlation.
sd.speed.corr(sd.dist)






















































