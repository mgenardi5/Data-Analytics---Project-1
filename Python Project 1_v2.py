#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
df = pd.read_csv('https://raw.githubusercontent.com/CunyLaguardiaDataAnalytics/datasets/master/2014-15_To_2016-17_School-_Level_NYC_Regents_Report_For_All_Variables.csv')
#Impoart data set and packages


# In[7]:


df.head()
df.dtypes
#highlevel review of dataset


# In[7]:


df['School Name'].unique()
#Review list of school names to chose 1 for comparison to comparator group


# In[8]:


df['Regents Exam'].unique()
#Review list of exam names to choose one as a feature for comparison


# In[8]:


df.drop('Number Scoring Below 65',axis=1,inplace=True)
df.drop('Percent Scoring Below 65',axis=1,inplace=True)
df.drop('Number Scoring 80 or Above',axis=1,inplace=True)
df.drop('Percent Scoring 80 or Above',axis=1,inplace=True)
df.drop('Number Scoring CR',axis=1,inplace=True)
df.drop('Percent Scoring CR',axis=1,inplace=True)
df.drop('Number Scoring 65 or Above',axis=1,inplace=True)
df.drop('Percent Scoring 65 or Above',axis=1,inplace=True)
#Drop columns not needed for analysis


# In[10]:


df.head()
#confirm columns were dropped


# In[9]:


df.groupby(['School Level'])['Mean Score'].count()
#see unique values to school level, choosing group with largest amount of data


# In[10]:


df2=df[df['School Level'] == 'K-8']
#filtering rows only for K-8 so as to choose one school and compare to remaining K-8 group


# In[13]:


df2.head()


# In[11]:


df2.groupby(['School Level'])['Mean Score'].count()
#Confirm school level rows outside of K-8 were dropped in new dataframe


# In[12]:


df3=df2[df2['Regents Exam'] == 'Common Core Algebra']
#filtering rows only for Common Core Algebra


# In[13]:


df3.groupby(['Regents Exam'])['Mean Score'].count()
#Confirm regents exam rows outside of Common Core Algebra were dropped in new dataframe


# In[73]:


df3.head()


# In[14]:


df4 = df3[df3['Mean Score']!='s']
#Drop rows with non-numerical mean score
#convert mean score to float type to support numerical analysis
df4=df4.astype({'Mean Score':'float'})
df4.dtypes


# In[15]:


df4.describe()
#descriptive stats


# In[16]:


df5 = df4[df4['School Name']=='Icahn Charter School']
df5 = df5.drop_duplicates('Year')
df5.drop('School DBN',axis=1,inplace=True)
df5.drop('School Level',axis=1,inplace=True)
df5.drop('Regents Exam',axis=1,inplace=True)
df5.drop('Total Tested',axis=1,inplace=True)
df5.head()
#create data frame with just comparator school removing duplicate years and drop remaining columns no longer needed


# In[29]:


df6 = df4[df4['School Name']!='Icahn Charter School']
df7=df6.groupby(['Year']).apply(lambda x: pd.Series({'Mean Score': np.average(x['Mean Score'], weights=x['Total Tested'])}))
df7.loc[:,'School Name'] = 'All Other K-8'
df7.insert(2,"Years",(2015,2016,2017))
df7.head()
#create df with all other K-8 schools with weighted average mean score


# In[32]:


df9=df5.rename(columns={'Year':'Years'})
df10=df9.merge(df7,how='outer')
df10
#merge dataframes


# In[34]:


df10.groupby(['School Name']).plot(x="Years",y="Mean Score", kind="bar")


# In[74]:


#analysis shows that Icahn Charter School as outperformed the average of K-8 schools on the Common Core Alegbra regents exam in all documented years (2015-2017).


# In[90]:





# In[91]:





# In[92]:





# In[93]:





# In[42]:





# In[64]:





# In[ ]:




