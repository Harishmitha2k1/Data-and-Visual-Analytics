
# coding: utf-8

# # Lab3. Pandas Indexing and Selection

# ## Simple Series and DataFrames

# ##### Import necessary modules

# In[2]:


import pandas as pd


# ##### Create a Series to store Temperature values for 1 week

# In[3]:


temperature_trichy = pd.Series([40.2, 39.8, 36.3, 39.1, 41.3, 32.9, 36.6])


# ##### show temperature values

# In[4]:


temperature_trichy


# ##### What is the weather on 2nd day?

# In[14]:


weather_2nd_day=temperature_trichy[1]
weather_2nd_day


# ##### Find all days and temperatures where temperature over 40.0 degree Celsius

# In[15]:


temperature_trichy[temperature_trichy>40.0]


# ##### Find only day, not temperature where temperature over 40.0 degree Celsius

# In[16]:


temperature_trichy[temperature_trichy>40.0].keys()


# ### Create a Dataframe for student details from List

# In[17]:


students = [['DS01', 'Rex', '1msc'], ['DS02', 'peter', '2msc'], ['CS01', 'ann', '3bsc']]
df_stud = pd.DataFrame(students, columns=['rollno', 'name', 'class'])


# ##### show df_stud dataframe

# In[18]:


df_stud


# ##### Display all column names of df_stud

# In[19]:


df_stud.columns


# ##### Add a new column "address" with values ['Delhi', 'Bangalore', 'Chennai'] to df_stud

# In[20]:


address= ['Delhi', 'Bangalore', 'Chennai']
df_stud['address']=address


# In[21]:


df_stud


# ### Create a Dataframe for Phone book from Dictionary

# In[24]:


phonebook = {'rex':[9942002764, 'rex@abc.com'],'sam':[9932176542,'sam@xyz.com'],'peter':[9865323645,'ann@bhc.com']}
df_phonebook=pd.DataFrame.from_dict(phonebook,orient='index')


# ##### Display df_phonebook

# In[25]:


df_phonebook


# ### Exploratory Data Analysis on Video Game Review Dataset

# ##### Import ign.csv dataset

# In[102]:


reviews = pd.read_csv("ign.csv")


# ##### Show top-5 rows

# In[103]:


reviews.head()


# ##### Show bottom 3 rows

# In[104]:


reviews.tail(3)


# ##### How many rows and columns here?

# In[105]:


reviews.shape


# ##### What are the datatypes?

# In[106]:


reviews.dtypes


# ### Selecting Columns

# ##### Select a single column, say title and print head

# In[107]:


reviews.title.tail()


# ##### Select multiple columns, title and genre and print head

# In[108]:


reviews[['title','genre']].head(10)


# ### Selection using Positions

# ##### Select top-5 rows and all columns, same as head() using iloc

# In[109]:


reviews.iloc[0:5,:]


# ##### Select rows from position 5 onwards, and columns from position 5 onwards.

# In[110]:


reviews.iloc[4:,4:].head()


# ##### Select the first column, and all of the rows for the column

# In[111]:


reviews.iloc[:,0].head()


# ##### the 10th row, and all of the columns for that row.

# In[116]:


reviews.iloc[9,:]


# ##### First column is not useful. So remove it

# ### Selection using Row and Column Labels3

# In[120]:


reviews=reviews.drop("Unnamed: 0",axis=1)


# In[121]:


reviews.head()


# ##### We have already created students dataframe as below. Let us access name column with loc()

# In[48]:


students = [['DS01', 'Rex', '1msc'], ['DS02', 'peter', '2msc'], ['CS01', 'ann','3bsc']]
df_stud = pd.DataFrame(students, columns=['rollno', 'name', 'class']) 
# row index automatically generated


# In[49]:


df_stud


# ##### Print all names using loc

# In[50]:


df_stud.loc[:,'name']


# ##### Let us come back to our reviews. Display the first five rows of reviews using the loc method

# In[51]:


reviews.loc[:4,:]


# ##### Select score_phrase column using loc and print head

# In[52]:


reviews.loc[:4,'score_phrase']


# ##### Print top 10 values of column label "score_phrase"

# In[53]:


reviews.loc[:9,'score_phrase']


# ##### Select from reviews of rows from 5 to 15

# In[54]:


some_reviews=reviews.loc[5:15,:]


# ##### print top 5 rows from some_reviews

# In[55]:


some_reviews.head()


# ##### Select scores of first 3 rows some_reviews

# In[56]:


some_reviews.loc[:,'score'].head(3)


# ##### Select "score", "genre", and "release_year" columns from reviews dataframe and print head

# In[57]:


reviews.loc[:,['score','genre','release_year']].head()


# ##### What is the datatype of "score" column?

# In[58]:


a=reviews.loc[:,'score']
type(a)


# ### Aggregate Columns

# ##### Find average value of score column in reviews dataframe

# In[59]:


reviews.score.mean()


# ##### Find average value of all numeric columns

# In[60]:


reviews.mean()


# ##### Find average value for each numeric column

# In[61]:


reviews.mean()


# ##### Find average value for each row containing numeric values and print head

# In[62]:


reviews.mean(axis=1).head()


# #### Find lowest, highest, median, standard deviation of score column of reviews dataframe

# ##### show median of "score" column of reviews dataframe

# In[63]:


reviews.score.median()


# ##### show minimum of "score" column of reviews dataframe

# In[64]:


a=reviews.score
min(a)


# ##### show maximum of "score" column of reviews dataframe

# In[65]:


max(a)


# ##### show standard deviation of "score" column of reviews dataframe

# In[66]:


reviews['score'].std()


# ##### How many non-null values in "score" column of reviews dataframe?

# In[67]:


reviews['score'].notnull().sum()


# ##### Show the summary of reviews dataframe

# In[68]:


reviews.describe()


# ##### Check if review score has any correlation with other columns of reviews

# In[69]:


reviews.corr()


# ##### Review score has no correlation with other features. So, release timing doesn’t linearly relate to review score

# ### Math Operations on DF columns

# ##### Divide the values of "score" column in reviews dataframe by 2. There will be too many values, so just print head

# In[70]:


(reviews.score/2).head()


# ### Boolean Indexing in Pandas

# ##### Select all video games whose review score > 7, call it score_filter

# In[71]:


score_filter =(reviews.score>7)


# ##### Print head of score_filter

# In[72]:


score_filter.head()


# ##### Select all rows for score_filter column and print its head

# In[73]:


filtered_reviews =reviews[reviews.score>7]


# ##### Show the size of filtered_reviews

# In[74]:


filtered_reviews.shape


# ##### Show top 10 "title" from filtered_reviews

# In[75]:


(filtered_reviews.title).head(10)


# ##### Find games released for the Xbox One platform that have a score of more than 7

# ##### First create a filter, called xbox_one_filter for the conditions

# In[76]:


xbox_one_filter=(reviews["score"] > 7) & (reviews["platform"] == "Xbox One")


# ##### Select those rows from reviews of xbox_one_filter and print head

# In[77]:


filtered_reviews2 = reviews[xbox_one_filter]
filtered_reviews2.head()
#show top 5 rows of filtered_reviews2


# In[78]:


# What is the size of filtered_reviews2
filtered_reviews2.shape


# ##### Select all video games which are 'Action' genre

# In[79]:


action_reviews = reviews[reviews.genre == 'Action']


# In[80]:


action_reviews.head()


# In[81]:


#What is the size of action_reviews?
action_reviews.shape


# ### Plot Review Ratings of two Play Stations and Compare Which one has more ratings?

# ##### Plot Histogram for the frequencies of different score ranges of Xbox One platform

# In[84]:


# Import plotting libraries
import matplotlib.pyplot as plt
# Plot the following histogram of score values for Xbox One platform
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")


# ##### Plot Histogram for Frequencies of the scores of Play Station4 platform

# In[83]:


reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

