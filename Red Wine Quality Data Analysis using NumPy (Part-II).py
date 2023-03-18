
# coding: utf-8

# # Lab2. Red Wine Quality Data Analysis using NumPy Part-II

# In[2]:


import numpy as np


# In[3]:


wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)


# # NumPy Aggregation Methods

# ### Find sum of all residual sugar values

# In[4]:


x=wines[:,3]
sum(x)


# ### Find sums of every feature value. There are 12 features altogether

# In[5]:


sum(wines)


# ### Find sum of every row

# In[6]:


z=wines[:,:].sum(axis=1)
z


# ### What is its size?

# In[7]:


len(wines)


# ### What is the maximum residual sugar value in red wines data?

# In[8]:


a=wines[:,3]
a=a.astype('int32')
a


# ### find its maximum residual sugar value

# In[9]:


max(a)


# ### What is the minimum residual sugar value in red wines data?

# In[10]:


min(a)


# ### What is the average residual sugar value in red wines data?

# In[11]:


np.mean(x)


# ### What is 25 percentile residual sugar value?

# In[12]:


np.percentile(x,25)


# ### What is 75 percentile residual sugar value?

# In[13]:


np.percentile(x,75)


# ### Find the average of each feature value

# In[14]:


y=wines[:,:]
y
y.mean(axis=0)


# # NumPy Array Comparisons

# ### Show all wines with quality > 5

# In[15]:


wines[:,11]>5


# ### Show all wines with quality > 7

# In[16]:


f=wines[:,11]>7
f


# ### check if any wines value is True for the condition quality > 7

# In[17]:


True in f


# ### Show first 3 rows where wine quality > 7, call it high_quality

# In[18]:


high_quality=[wines[:,11]>7][:3]
high_quality


# ### Show only top 3 rows and all columns of high_quality wines data

# In[19]:


wines[high_quality][0:3]


# ### Show wines with a lot of alcohol > 10 and high wine quality > 7

# In[20]:


b=(wines[:,10]>10)&(wines[:,11]>7)
b


# ### show only alcohol and wine quality columns

# In[21]:


wines[b,10:]


# # Combining NumPy Arrays

# ### Combine red wine and white wine data

# ### Open white wine dataset

# In[22]:


white_wines = np.genfromtxt("winequality-white.csv", delimiter=";", skip_header=1)


# ### Show size of white_wines

# In[23]:


white_wines.shape


# ### combine wines and white_wines data frames using vstack and call it all_wines

# In[24]:


all_wines=np.vstack((wines,white_wines))


# In[25]:


all_wines.shape


# ### Combine wines and white_wines data frames using concatenate method

# In[26]:


all_wines1=np.concatenate((wines,white_wines),axis=0)


# In[27]:


all_wines1.shape


# # Matrix Operations and Reshape

# ### Find Transpose of wines and print its size

# In[28]:


tran=wines.T
tran.shape


# ### Convert wines data into 1D array

# In[29]:


wines.ravel()


# ### Reshape second row of wines into a 2-dimensional array with 2 rows and 6 columns

# In[30]:


wines[1].reshape((2,6))


# # Sort alcohol column Ascending Order

# In[31]:


sorted_alcohol=np.sort(wines[:,-2])


# In[32]:


sorted_alcohol


# ### Make sorting to take place in-place

# In[33]:


wines[:,-2].sort()


# In[34]:


wines[:,-2]


# ### Show top 10 rows

# In[35]:


wines[:,-2]


# ### Sort alcohol column Descending Order

# In[36]:


sorted_alcohol_desc=np.sort(wines[:,10])[::-1]


# In[37]:


sorted_alcohol_desc


# ### will original data be modified?. Check top 10 rows

# In[38]:


wines[:,-2]

