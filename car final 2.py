# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# print dataset
car = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Basic statistics level 1\\cars.csv")
car.columns
ca=car.columns
print(ca)
# print skewness, kurtosis, correlation
car.skew()
car.kurt()
car.corr()
car.head()
# print max & min, plot histogram, bar and categorise.
# column HP
car["HP"].max()
car["HP"].min()
plt.hist(car['HP'],edgecolor='k')
h1 = [i for i in car.HP if (i>=45) & (i<100)]
h2 = [i for i in car.HP if (i>=100) & (i<200)]
h3 = [i for i in car.HP if (i>=200) & (i<325)]
H4 = [len(h1),len(h2),len(h3)]
H5 = ["45-100","100-200","200-325"]
for i, v in enumerate(H4):
    plt.text(i-.25, 
              v, 
              H4[i], 
              fontsize=18, 
              color="red")
plt.bar(H5,H4)
plt.xticks(H5,rotation=90)
# MPG
car["MPG"].max()
car["MPG"].min()
plt.hist(car['MPG'],edgecolor='k')
m1 = [i for i in car.MPG if (i>=10) & (i<25)]
m2 = [i for i in car.MPG if (i>=25) & (i<40)]
m3 = [i for i in car.MPG if (i>=40) & (i<55)]
M4 = [len(m1),len(m2),len(m3)]
M5 = ["45-100","100-200","200-325"]
for i, v in enumerate(M4):
    plt.text(i-.25, 
              v, 
              M4[i], 
              fontsize=18, 
              color="red")
plt.bar(M5,M4)
plt.xticks(M5,rotation=90)
# VOL
car["VOL"].max()
car["VOL"].min()
plt.hist(car['VOL'],edgecolor='k')
v1 = [i for i in car.VOL if (i>=45) & (i<75)]
v2 = [i for i in car.VOL if (i>=75) & (i<100)]
v3 = [i for i in car.VOL if (i>=100) & (i<125)]
v4 = [i for i in car.VOL if (i>=125) & (i<170)]
V5 = [len(v1),len(v2),len(v3),len(v4)]
V6 = ["45-75","75-100","100-125","125-170"]
for i, v in enumerate(V5):
    plt.text(i-.25, 
              v, 
              V5[i], 
              fontsize=18, 
              color="red")
plt.bar(V6,V5)
plt.xticks(V6,rotation=90)
# SP
car["SP"].max()
car["SP"].min()
plt.hist(car['SP'],edgecolor='k')
s1 = [i for i in car.SP if (i>=95) & (i<115)]
s2 = [i for i in car.SP if (i>=115) & (i<125)]
s3 = [i for i in car.SP if (i>=125) & (i<150)]
s4 = [i for i in car.SP if (i>=150) & (i<175)]
S5 = [len(s1),len(s2),len(s3),len(s4)]
S6 = ["95-115","115-125","125-150","150-175"]
for i, v in enumerate(S5):
    plt.text(i-.25, 
              v, 
              S5[i], 
              fontsize=18, 
              color="red")
plt.bar(S6,S5)
plt.xticks(S6,rotation=90)
# WT
car["WT"].max()
car["WT"].min()
plt.hist(car['WT'],edgecolor='k')
w1 = [i for i in car.WT if (i>=10) & (i<25)]
w2 = [i for i in car.WT if (i>=25) & (i<32)]
w3 = [i for i in car.WT if (i>=32) & (i<40)]
w4 = [i for i in car.WT if (i>=40) & (i<55)]
W5 = [len(w1),len(w2),len(w3),len(w4)]
W6 = ["10-25","25-32","32-40","40-55"]
for i, v in enumerate(W5):
    plt.text(i-.25, 
              v, 
              W5[i], 
              fontsize=18, 
              color="red")
plt.bar(W6,W5)
plt.xticks(W6,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# HP
car['HP'].skew()
car['HP'].kurt()
plt.hist(car['HP'],edgecolor='k')
sns.distplot(car['HP'],hist=False)
plt.boxplot(car['HP'])
# MPG
car['MPG'].skew()
car['MPG'].kurt()
plt.hist(car['MPG'],edgecolor='k')
sns.distplot(car['MPG'],hist=False)
plt.boxplot(car['MPG'])
# VOL
car['VOL'].skew()
car['VOL'].kurt()
plt.hist(car['VOL'],edgecolor='k')
sns.distplot(car['VOL'],hist=False)
plt.boxplot(car['VOL'])
# SP
car['SP'].skew()
car['SP'].kurt()
plt.hist(car['SP'],edgecolor='k')
sns.distplot(car['SP'],hist=False)
plt.boxplot(car['SP'])
# WT
car['WT'].skew()
car['WT'].kurt()
plt.hist(car['WT'],edgecolor='k')
sns.distplot(car['WT'],hist=False)
plt.boxplot(car['WT'])
# plot graph between HP & MPG
df=pd.crosstab(car['HP'],car['MPG'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# plot graph between HP & VOL
df=pd.crosstab(car['HP'],car['VOL'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# visulization
plt.plot(np.arange(81),car.HP)
plt.plot(np.arange(81),car.MPG)
plt.plot(np.arange(81),car.VOL)
plt.plot(np.arange(81),car.SP)
plt.plot(np.arange(81),car.WT)
car.HP.corr(car.HP)
car.HP.corr(car.MPG)
car.HP.corr(car.VOL)
car.HP.corr(car.SP)
car.HP.corr(car.WT)
plt.plot(np.arange(81),car.HP,"ro-")
plt.plot(np.arange(81),car.MPG,"ro-")
plt.plot(np.arange(81),car.VOL,"ro-")
plt.plot(np.arange(81),car.SP,"ro-")
plt.plot(np.arange(81),car.WT,"ro-")
car.VOL.value_counts().plot(kind="pie")
car.VOL.value_counts().plot(kind="bar")
sns.pairplot(car,hue="VOL",size=3)
sns.pairplot(car.iloc[:,0:80])
plt.plot(car.HP,car["SP"],"ro");plt.xlabel("HP");plt.ylabel("SP")
c1=car.groupby(car.VOL).count()
c1
c2=car.groupby(car.HP).count()
c2




























