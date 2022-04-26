from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("papers.csv")
data=df.drop_duplicates(['Title','Affiliation'])
n = 10
a=data['Affiliation'].value_counts()[:n].index.tolist()
print(a)
data_google=data.loc[df['Affiliation'] == "Google"]
print(data_google)
d_google = dict(data_google["Year"].value_counts())
D_google = dict(reversed(list(d_google.items())))
y_google= list(D_google.values())
x=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
# plt.scatter(range(len(D_google)), list(D_google.values()),color='maroon')
# plt.xticks(range(len(D_google)), list(D_google.keys()))
# plt.show()
data_stan=data.loc[df['Affiliation'] == "Stanford University"]
d_stan = dict(data_stan["Year"].value_counts())
D_stan = dict(reversed(list(d_stan.items())))
y_stan = list(D_stan.values())
# plt.scatter(range(len(D_stan)), list(D_stan.values()),color='green')
# plt.xticks(range(len(D_stan)), list(D_stan.keys()))

# plt.plot(x,y_stan,color='green',label='stanford')


data_carnegie = data.loc[df['Affiliation'] == "Carnegie Mellon University"]
d_carnegie = dict(data_carnegie["Year"].value_counts())
D_carnegie = dict(reversed(list(d_stan.items())))
y_carnegie = list(D_carnegie.values())

data_ucberkeley = data.loc[df['Affiliation'] == "UC Berkeley"]
d_ucberkeley = dict(data_ucberkeley["Year"].value_counts())
D_ucberkeley = dict(reversed(list(d_ucberkeley.items())))
y_ucberkeley = list(D_ucberkeley.values())

data_mit=data.loc[df['Affiliation'] == "MIT"]
d_mit = dict(data_mit["Year"].value_counts())
D_mit = dict(reversed(list(d_mit.items())))
y_mit=list(D_mit.values())
plt.plot(x,y_google,'b',x,y_stan,'r',x,y_carnegie,'y',x,y_ucberkeley,'c',x,y_mit,'m')
plt.show()
# print(data_google)
# data=data['Affiliation'].value_counts(ascending=False)
c = dict(data["Affiliation"].value_counts(ascending=False))
C = dict(list(c.items())[0: 10]) 
# print(c)
plt.figure(figsize=(25,10))
plt.bar(range(len(C)), list(C.values()))
plt.xticks(range(len(C)), list(C.keys()))
# plt.show()



new_df = df.groupby(['Title','Affiliation']).first()


# c = dict(new_df["Affiliation"].value_counts())
# C = dict(reversed(list(c.items())))
# plt.figure(figsize=(25,10))
# plt.bar(range(len(C)), list(c.values()))
# plt.xticks(range(len(C)), list(C.keys()))
# plt.show()

sorted_yr=df.sort_values("Year")

remove_dupli=sorted_yr.drop_duplicates(subset='Title', keep="last")
example=sorted_yr.drop_duplicates(subset=('Affiliation','Title'), keep="last")
# print(example[0:20])
d = dict(remove_dupli["Year"].value_counts())
D = dict(reversed(list(d.items())))
plt.figure(figsize=(25,10))
plt.bar(range(len(D)), list(D.values()))
plt.xticks(range(len(D)), list(D.keys()))
# plt.show()
# print(sorted_yr)
years = sorted_yr["Year"].to_list()
years = list(set(years))
# print(years)
# df.plot(x="year",y=sorted_yr["year"].value_counts(),figsize=(9, 6))
# plt.title("Average Income over the Years")
# plt.show()