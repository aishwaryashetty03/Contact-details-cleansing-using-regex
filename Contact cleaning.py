#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd

import numpy as np

import re

from itertools import chain


# In[10]:


data = pd.read_csv("C://Users//Aishwarya//Downloads//Desktop//Dummy Data.csv")


import numpy as np
data = data.replace(np.nan, '', regex=True)
data.head(10)


# In[ ]:





# In[14]:


### splitting email and mobile numbers from telephone

data['Email_address']=data['TELEPHONE'].str.findall('(\S+@\S+)')
#data['Email_address']=data['TELEPHONE'].str.findall('(\S+@\S+)')
data['Email_address']=data['Email_address'].apply(lambda x:''.join(x))
data['phone']= data['TELEPHONE'].apply(lambda x: re.findall(r'\d',x))
#data['phone']=data['TELEPHONE'].apply(lambda x: re.findall(r'\d+',x))
data['phone']=data['phone'].apply(lambda x:''.join(x))
#data['Email_address'].fillna(data['Telephone'],inplace=True)
#data.to_csv("Dummy_data_final.csv")

data.head(10)


# In[11]:


#Extracting email id and phone from notes

data['Email_address_notes']=data['NOTES'].str.findall('(\S+@\S+)')
#data['Email_address']=data['TELEPHONE'].str.findall('(\S+@\S+)')
data['Email_address_notes']=data['Email_address_notes'].apply(lambda x:''.join(x))
data['phone_notes']= data['NOTES'].apply(lambda x: re.findall(r'\d{10}',x))
#data['phone']=data['TELEPHONE'].apply(lambda x: re.findall(r'\d+',x))
data['phone_notes']=data['phone_notes'].apply(lambda x:''.join(x))
#data['Email_address'].fillna(data['Telephone'],inplace=True)
#data.to_csv("Dummy_data_final.csv")

data.head(10)


# In[20]:




data['Email_address']=data['Email_address'].replace(r'^\s*$',np.nan,regex=True)

data['Email_address_notes']=data['Email_address_notes'].replace(r'^\s*$',np.nan,regex=True)

data['Email_address']=data[['Email_address','Email_address_notes']].apply(lambda x:x.str.cat(sep=','),axis=1)


data['phone']=data['phone'].replace(r'^\s*$',np.nan,regex=True)

data['phone_notes']=data['phone_notes'].replace(r'^\s*$',np.nan,regex=True)

data['phone']=data[['phone','phone_notes']].apply(lambda x:x.str.cat(sep=','),axis=1)


# In[21]:


data=data.drop(['Email_address_notes','phone_notes'],axis=1)

data.head(5)


# In[22]:


data['Email_address']=data['Email_address'].replace(r'^\s*$',np.nan,regex=True)
data['phone']=data['phone'].replace(r'^\s*$',np.nan,regex=True)
data['CONTACT']=data[['Email_address','phone']].apply(lambda x:x.str.cat(sep=','),axis=1)

data.head(5)


# In[32]:



#data['Email_address_new'] = data[['Email_address', 'Email_address_notes']].apply(lambda x: '\n'.join(x), axis=1)

#data['Email_address_new']=data['Email_address']+ ";" + data['Email_address_notes']

#new=data['Email_address_notes'].copy()

#data['Email_address']=data["Email_address"].str.cat(new,sep=", ")




# In[23]:


#return lost from series of ; seperated strings

def chainer(s):
    return list(chain.from_iterable(s.str.split(',')))


# In[24]:


# calculate lengths pf splits
lens = data['CONTACT'].str.split(',').map(len)


# In[ ]:





# In[25]:


data1 =pd.DataFrame({'ACCT_CODE':np.repeat(data['ACCT_CODE'],lens),
                    'CUST_NAME':np.repeat(data['CUST_NAME'],lens),
                    'CONTACTID':np.repeat(data['CONTACTID'],lens),
                    'CONTACTTYPE':np.repeat(data['CONTACTTYPE'],lens),
                    'CONTACTNAME':np.repeat(data['CONTACTNAME'],lens),
                    'PHONEID':np.repeat(data['PHONEID'],lens),
                     'TELECODE':np.repeat(data['TELECODE'],lens),
                    'CONTACT':chainer(data['CONTACT'])})


# In[26]:


data1.head(15)


# In[27]:


pattern ='(\S+@\S+)'

data1['TELECODE1']=data1['CONTACT'].str.contains(pattern)

data1['TELECODE1']=data1['TELECODE1'].map({True:'Email',False:'Phone'})


# In[28]:


data1.loc[data1['TELECODE1']=='Email','TELECODE'] ='Email'


# In[29]:


data1.head(15)


# In[30]:


data1=data1.drop('TELECODE1',axis=1)


# In[31]:


data1.head(15)

