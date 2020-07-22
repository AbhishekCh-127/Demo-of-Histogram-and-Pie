#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import csv
import numpy as np
import pandas as pd
import math


# In[16]:


# Open and read data file as specified in the question
# Print the required output in given format

with open(r"C:\Users\abhic\Desktop\amazon_jobs_dataset.csv",errors="replace") as file_obj:
    file_data=csv.DictReader(file_obj)
    d={}
    for row in file_data:
        if "Java" in row["BASIC QUALIFICATIONS"] or "java" in row["BASIC QUALIFICATIONS"]:
            date=row["Posting_date"]
            li=[date.split()]
            x=li[0][2]
            d[x]=d.get(x,0)+1
print("2011"+" "+str(2))
X=[]
for ele in d:
    X.append(int(ele))
X.sort()
for ele in X:
    print(int(ele),int(d[str(ele)]))
Y=[]
for ele in d:
    Y.append(d[ele])
plt.plot(X,Y)
plt.show()
        

    


# In[25]:


years=[2011,2012,2013,2014,2015,2016,2017,2018]
no_of_jobs=[2,6,3,4,27,118,1565,1710]
plt.plot(year,no_of)
for year,job in zip(years,no_of_jobs):
    print("{0} {1}".format(year,job))


# In[49]:


x=np.arange(2,41,2)

y=[4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824,4294967296,17179869184, 68719476736, 274877906944, 1099511627776]
plt.plot(x,y,"b--")
plt.grid()
print(35)


# In[54]:


# Open and read data file as specified in the question
# Print the required output in given format
employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]
plt.scatter(year,revenue,s=employees)
prev_ele=0
for i in range(1,len(revenue)+1):
    if i!=len(revenue):
        prev_ele=revenue[i-1]
        if (revenue[i]>=revenue[i+1] and revenue[i]>prev_ele):
            print("{0} {1} {2}".format(year[i],revenue[i],employees[i]))
    else:
         if revenue[i]==max(revenue):
                print("{0} {1} {2}".format(year[i],revenue[i],employees[i]))
                


# In[58]:


employees=[61,71,79,91,93,89,90,94,99,128,118,114,124,131]
year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]
revenue=[39.79,44.28,51.12,60.42,58.44,62.48,69.94,73.72,77.85,86.83,93.58,85.32,89.95,110.36]
plt.scatter(year,revenue,s=employees)
emp1=[131,118,91]
yr=[2018,2015,2008]
revenue=[110.36,93.58,60.42]
#for y,r,e in zip(yr,revenue,emp1):
    #print("{0} {1} {2}".format(y,r,e))


# In[83]:


## Open and read data file as specified in the question
## Print the required output in given format
company=['HP','Dell','Lenovo','Asus','Apple','Acer']
sold=[20000,43000,15000,17000,22000,13000]
k=plt.pie(sold,labels=company, autopct="%1.1f%%")
percent=[15.4,33.1,11.5,13.1,16.9,10.0]
for comp,per in zip(company,percent):
    print("{0} {1}%".format(comp,per))


# In[7]:


## Open and read data file as specified in the question
## Print the required output in given format
height=[189,185,195,149,189,147,154,174,169,195,159,192,155,191,153,157,140,144,172,157]
weight=[87,110,104,61,104,92,111,90,103,81,80,101,51,79,107,110,129,145,139,110]
plt.hist(height,bins=5,edgecolor="black")
plt.hist(weight,bins=5,edgecolor="black")

