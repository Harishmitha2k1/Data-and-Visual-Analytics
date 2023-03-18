
# coding: utf-8

# ### Rollno:225229113

# ## Lab8. Pandas Time Series Analysis

# In[10]:


# Importing required modules
import pandas as pd


# In[11]:


# Settings for pretty plots
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.show()


# In[12]:


# Reading in the data
data = pd.read_csv('amazon_stock.csv')


# ### Inspect top 10 rows

# In[17]:


data.head(10)


# ### Remove unwanted columns

# In[14]:


data = data.drop(['None','ticker'],axis=1)


# In[15]:


data.head()


# In[16]:


# Look at the datatypes of the various columns , call info()
data.info()


# ### Inspect the datatypes of columns

# In[18]:


data.dtypes


# #### Convert "Date" string column into actual Date object

# In[19]:


data['Date'] = pd.to_datetime(data['Date'])


# In[20]:


data.dtypes


# #### Let us check our data once again, with head()

# In[21]:


data.head()


# ### Set Date object to be index

# #### Here Date is one of the columns. But we want date to be the index. So, set date as index for the frame. Make inplace=True'

# In[22]:


data.set_index(['Date'], inplace=True)


# In[23]:


data.head()


# ### Understand stock data

# In[24]:


data['Adj_Close'].plot(figsize=(12,6), title = 'Adjusted Closing Price')


# ### Understand data timeindex

# In[25]:


from datetime import datetime
my_year=2020
my_month =5
my_day=1
my_hour=13
my_minute=36
my_second=45
test_date=datetime(my_year,my_month,my_day)
test_date


# In[26]:


test_date = datetime(my_year, my_month, my_day,my_hour, my_minute, my_second)
print("The Day is : ", test_date.day)
print("The Hour is : ", test_date.hour)
print("The Month is : ", test_date.month)


# #### Find minimum and maximum dates from data frame,call info() method

# In[27]:


data.info()


# In[28]:


print("Minimum Date : ",data.index.min())
print("Maximum date : ",data.index.max())


# #### Retrieve index of earliest and latest dates using argmin and argmax

# In[29]:


print("Minimum Date Location : ",data.index.argmin())
print("Maximum date Location : ",data.index.argmax())


# ### 1.Resampling Operation

# #### Resample enterire data frame

# #### Resample data with year end frequency ("Y") with average stock price

# In[30]:


data.resample('Y').mean()


# ### Resample a specific column

# ##### Plot a bar chart to show the yearly(Use "A") mean adjusted close price

# In[31]:


data['Adj_Close'].resample('A').mean().plot(kind = 'bar', figsize=(10,4))
plt.title(" Yearly Mean Adj close Price for Amazon")
plt.show()


# #### Plot bar chart of Quarterly(Use "Q")Average Volume for all years

# In[32]:


data['Open'].resample('MS').max().plot(kind = 'bar', figsize=(20,4))
plt.title(" Monthly Maximum Opening Price for Amazon")
plt.show()


# #### Plot bar chart of quarterly (use 'Q')average volume for all years

# In[33]:


data['Volume'].resample('Q').mean().plot(kind = 'bar', figsize=(10,4))
plt.title(" Quarterly Average Volume for Amazon")
plt.show()


# ### 2.Time shifting operations

# #### Shifting data forward and backward

# #### Show head of data

# In[34]:


data.head()


# #### Shift data by 1day forward

# In[35]:


data.shift(periods = 1).head()


# #### Shift data by 1 day backward

# In[36]:


data.shift(periods = -1).head()


# ### Shifting time index

# In[37]:


data.head(10)


# In[38]:


data.shift(periods = 3,freq='MS')


# #### Application:Computing Retrun on investment

# In[39]:


ROI = 100* (data['Adj_Close'].tshift(periods = - 365, freq ='D')/data['Adj_Close']-1)
ROI.plot(figsize=(16,8))
plt.ylabel('% Return On Investment')


# ### 3.Rolling Window or moving window operations

# In[40]:


data['Adj_Close'].plot(figsize=(12,8), color='red')


# #### Find rolling mean for 7 days and show top-10 rows

# In[41]:


data.rolling(7).mean().head(10)


# #### Plot a line char for"Open" column.

# In[42]:


data['Open'].plot(figsize=(12,8))
data['Open'].rolling(30).mean().plot(figsize=(12,8), color='red')

