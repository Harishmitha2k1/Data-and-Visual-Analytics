
# coding: utf-8

# # Lab1.Red Wine Quality Data Analytics using Numpy Part-I      

# ### Import modules for numpy

# In[2]:


import numpy as np


# In[3]:


wines = np.genfromtxt("winequality-red.csv", delimiter=";", skip_header=1)


# ### What is its size?

# In[4]:


wines.size


# ### How many wine data rows here?

# In[5]:


wines.shape[0]


# ### How many wine data columns here?

# In[6]:


wines.shape[1]


# ### How many dimensions?

# In[7]:


wines.ndim


# ### What is the type of data?

# In[8]:


type(wines)


# ### What is the data type of wines data?

# In[9]:


wines.dtype


# ### Show top 5 rows

# In[10]:


wines[:5, :]


# ### What is the value at 3rd row, 4th column of wine data?

# In[11]:


wines[2,3]


# ### Select first 3 items in 4th column

# In[12]:


wines[:3, 3]


# ### Show 1st column

# In[13]:


wines[:, 0]


# ### Show 2nd row

# In[14]:


wines[1, :]


# ### Select items from rows 1 to 3 and 5th column

# In[15]:


wines[1:4, 4]


# ### Select entire array

# In[16]:


wines[:,:]


# ### Change 1st value in wines to 100

# In[17]:


wines[0,0]


# In[18]:


wines[0,0] = 100


# In[19]:


wines[0,0] 


# ###  Change it back to 7.4 and print

# In[20]:


wines[0,0] = 7.4


# In[21]:


wines[0,0]


# # 1-Dimensional Numpy Arrays

# ### Select 4th row all column values

# In[22]:


fourth_row = wines[3,]


# ### Display its value

# In[23]:


fourth_row


# ### Show 2nd value

# In[24]:


fourth_row[1]


# ### Convert wine data to integer values and show it

# In[25]:


wines.astype(int)


# # Vectorization Operations

# ### Increase wine quality score (output variable) by 10

# In[26]:


wines[:,11]


# ### Increase by 10

# In[27]:


wines[:, 11] += 10


# ### Display update score

# In[28]:


wines[:, 11]


# ### Multiply alcohol of all wine data by 3 times

# In[29]:


wines[:, 10] *= 3


# ### Show updated alcohol column

# In[30]:


wines[:, 10]


# ### Add quality column by itselt

# In[31]:


wines[:, 11] + wines[:, 11]


# ### Multiply alcohol and wine quality columns. It will perform element wise multiplication

# In[32]:


wines[:,10] * wines[:,11]


# # Broadcasting

# ### Add every row of wines data with a random array of values

# In[33]:


rand_array=np.random.rand(12)


# ### Show rand_array

# In[34]:


rand_array


# ### add wines and rand_array

# In[35]:


wines+rand_array

