# import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pylab as plt
# print dataset
comp = pd.read_csv("C:\\Users\\ACER\\Desktop\\scrap\\Basic statistics level 1\\Computer.csv")
comp.columns
co=comp.columns
print(co)
# print skewness & kurtosis
comp.skew()
comp.kurt()
# print max & min, plot histogram, bar and categorise.
# column price
comp["price"].max()
comp["price"].min()
plt.hist(comp['price'],edgecolor='k')
p1 = [i for i in comp.price if (i>=900) & (i<1500)]
p2 = [i for i in comp.price if (i>=1500) & (i<2000)]
p3 = [i for i in comp.price if (i>=2000) & (i<2500)]
p4 = [i for i in comp.price if (i>=2500) & (i<3000)]
p5 = [i for i in comp.price if (i>=3000) & (i<4000)]
p6 = [i for i in comp.price if (i>=4000) & (i<5500)]
P7 = [len(x1),len(x2),len(x3),len(x4),len(x5),len(x6)]
P8 = ["900-1500","1500-2000","2000-2500","2500-3000","3000-4000","4000-5500"]
for i, v in enumerate(P7):
    plt.text(i-.25, 
              v, 
              P7[i], 
              fontsize=18, 
              color="red")
plt.bar(P8,P7)
plt.xticks(P8,rotation=90)
# speed
comp["speed"].max()
comp["speed"].min()
s1 = [i for i in comp.speed if (i>=25) & (i<50)]
s2 = [i for i in comp.speed if (i>=50) & (i<75)]
s3 = [i for i in comp.speed if (i>=75) & (i<110)]
S4 = [len(s1),len(s2),len(s3)]
S5 = ["25-50","50-75","75-100"]
for i, v in enumerate(S4):
    plt.text(i-.25, 
              v, 
              S4[i], 
              fontsize=18, 
              color="red")
plt.bar(S5,S4)
plt.xticks(S5,rotation=90)
# hd
comp["hd"].max()
comp["hd"].min()
h1 = [i for i in comp.hd if (i>=80) & (i<250)]
h2 = [i for i in comp.hd if (i>=250) & (i<500)]
h3 = [i for i in comp.hd if (i>=500) & (i<1000)]
h4 = [i for i in comp.hd if (i>=1000) & (i<1500)]
h5 = [i for i in comp.hd if (i>=1500) & (i<2150)]
H6 = [len(h1),len(h2),len(h3),len(h4),len(h5)]
H7 = ["80-250","250-500","500-1000","1000-1500","1500-2100"]
for i, v in enumerate(H6):
    plt.text(i-.25, 
              v, 
              H6[i], 
              fontsize=18, 
              color="red")
plt.bar(H7,H6)
plt.xticks(H7,rotation=90)
# ram
comp["ram"].max()
comp["ram"].min()
r1 = [i for i in comp.ram if (i>=2) & (i<8)]
r2 = [i for i in comp.ram if (i>=8) & (i<16)]
r3 = [i for i in comp.ram if (i>=16) & (i<32)]
R4 = [len(r1),len(r2),len(r3)]
R5 = ["2-8","8-16","16-32"]
for i, v in enumerate(R4):
    plt.text(i-.25, 
              v, 
             R4[i], 
              fontsize=18, 
              color="red")
plt.bar(R5,R4)
plt.xticks(R5,rotation=90)
# screen
comp["screen"].max()
comp["screen"].min()
n1 = [i for i in comp.screen if i==14]
n2 = [i for i in comp.screen if i==15]
n3 = [i for i in comp.screen if i==17]
N4 = [len(n1),len(n2),len(n3)]
N5 = ["scr-14","scr-15","scr-17"]
for i, v in enumerate(N4):
    plt.text(i-.25, 
              v, 
             N4[i], 
              fontsize=18, 
              color="red")
plt.bar(N5,N4)
plt.xticks(N5,rotation=90)
# print skewness,kurtosis and plot histogram, distplot, boxplot
# price
comp['price'].skew()
comp['price'].kurt()
plt.hist(comp['price'],edgecolor='k')
sns.distplot(comp['price'],hist=False)
plt.boxplot(comp['price'])
# speed
comp['speed'].skew()
comp['speed'].kurt()
plt.hist(comp['speed'],edgecolor='k')
sns.distplot(comp['speed'],hist=False)
plt.boxplot(comp['speed'])
# hd
comp['hd'].skew()
comp['hd'].kurt()
plt.hist(comp['hd'],edgecolor='k')
sns.distplot(comp['hd'],hist=False)
plt.boxplot(comp['hd'])
# ram
comp['ram'].skew()
comp['ram'].kurt()
plt.hist(comp['ram'],edgecolor='k')
sns.distplot(comp['ram'],hist=False)
plt.boxplot(comp['ram'])
# screen
comp['screen'].skew()
comp['screen'].kurt()
plt.hist(comp['screen'],edgecolor='k')
sns.distplot(comp['screen'],hist=False)
plt.boxplot(comp['screen'])
# plot graph between price & screen
df=pd.crosstab(comp['price'],comp['screen'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# speed & screen
df=pd.crosstab(comp['speed'],comp['screen'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# hd & screen
df=pd.crosstab(comp['hd'],comp['screen'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()
# ram & screen
df=pd.crosstab(comp['ram'],comp['screen'])
df.plot(kind="bar",stacked=True)
plt.grid(axis="y")
plt.show()











































































