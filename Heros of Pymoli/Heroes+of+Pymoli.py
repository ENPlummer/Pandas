
# coding: utf-8

# Heros of Pymoli Data Analysis.
# 1. The players are overwhelmingly male. There were 633 male players and only 136 female players.
# 2. The 20-24 age group purchases the most items and had the highest purchase amount of all age groups.
# 3. The total revenue generated for all players was $2286.33.
# 4. it would be intereting to see the ages of the top five spenders to see if they are in the 20-24 age group that purchased the most items and had the highest purchase amount.
# 

# In[1]:


#Dependencies

import pandas as pd
import numpy as np


# In[2]:


#Store file path as a variable.

purchase_data = "Resources/purchase_data.json"


# In[3]:


# Read the purchase data JSON file with the pandas library. Show header.

purchase_data_df = pd.read_json(purchase_data)
purchase_data_df.head()


# In[4]:


#Display a statistical overview of the purchase data.
purchase_data_df.describe()


# In[5]:


#Total number of players.

players_df = purchase_data_df.groupby("SN")["SN"].nunique()
players_df.count()


# In[6]:


#Number of unique items.

items_df = purchase_data_df.groupby("Item Name")["Item Name"].nunique()
items_df.count()


# In[7]:


#Average purchase price.

average_price_df = purchase_data_df["Price"].mean()
average_price_df.round(2)


# In[8]:


#Total number of purchases.

total_purchases_df = len(purchase_data_df)
total_purchases_df


# In[9]:


# Total Revenue.

total_revenue_df = purchase_data_df["Price"].sum()
total_revenue_df.round(2)


# In[10]:


purchasing_analysis_df = pd.DataFrame({"Number of Unique Items":[items_df],
                                             "Average Purchase Price":[average_price_df],
                                            "Total Number of Purchases":[total_purchases_df],
                                             "Total Revenue":[total_revenue_df]})
purchasing_analysis_df


# In[11]:


# Gender Count
gender_count_df = purchase_data_df.groupby("Gender")["SN"].nunique()
gender_count_df.head()


# In[12]:


# Gender Percentage
gender_percentage_df = gender_count_df/573
gender_percentage_df.round(2)


# In[13]:


#Gender demographics DataFrame.

gender_demographics_df = pd.DataFrame({"Gender Count": gender_count_df,"Gender Percentage":gender_percentage_df})
gender_demographics_df


# In[14]:


#Total number of purchases by gender.


gender_purchases_df = purchase_data_df.groupby("Gender")["Item Name"]
gender_purchases_df.count()


# In[15]:


# Average price of items by gender.

gender_average_df = purchase_data_df.groupby("Gender")["Price"].mean()
gender_average_df.round(2)


# In[16]:


#Total Purchase value by gender.

gender_total_df = purchase_data_df.groupby("Gender")["Price"].sum()
gender_total_df


# In[17]:


#Normalized gender total.
normalized_gender_total_df = gender_total_df/gender_count_df
normalized_gender_total_df.round(2)


# In[18]:


# Purchasing analysis DataFrame by gender.

gender_analysis_df = pd.DataFrame({"Purchase Count":gender_purchases_df, 
                                   "Average Purchase Price":gender_average_df,
                                   "Total Purchase Value":gender_total_df,
                                   "Normalized Totals":normalized_gender_total_df})
gender_analysis_df


# In[19]:


#Create bins in which data will be held. Bins are <10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39 >39.

bins = [0,10,15,20,25,30,35,40, 45]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]


# In[20]:


# Cut purchase data and place the ages into bins
pd.cut(purchase_data_df["Age"], bins, labels=age_ranges)


# In[21]:


purchase_data_df["Age Range"] = pd.cut(purchase_data_df["Age"], bins, labels= age_ranges)
purchase_data_df.head()


# In[22]:


#Players percentage by age range.

age_group_percentage_df = round(purchase_data_df["Age Range"].value_counts()/780,2)
age_group_percentage_df


# In[23]:


# Purchase count by age range.

age_group_count_df = purchase_data_df.groupby("Age Range")["Item Name"]
age_group_count_df.count()


# In[24]:


# Average purchase price by age range.

age_group_average_df = purchase_data_df.groupby("Age Range")["Price"].mean()
age_group_average_df.round(2)


# In[25]:


#Total purchase value by age range.

age_group_total_df = purchase_data_df.groupby("Age Range")["Price"].sum()
age_group_total_df


# In[26]:


#Normalized totals by age range.

normalized_age_total_df = age_group_total_df/573
normalized_age_total_df.round(2)


# In[27]:


# Convert to DataFrame.

age_range_df = pd.DataFrame({"Purchase Count":age_group_count_df,
                            "Average Purchase Price":age_group_average_df,
                            "Total Purchase Value": age_group_total_df,
                            "Normalized Totals": normalized_age_total_df
})
age_range_df


# In[28]:


#Overall spending analysis

players_purchase_count_df = purchase_data_df.groupby("SN").count()["Price"].rename("Purchase Count")
players_average_price_df = purchase_data_df.groupby("SN").mean()["Price"].rename("Average Purchase Price")
players_total_df = purchase_data_df.groupby("SN").sum()["Price"].rename("Total Purchase Value")

#Convert to DataFrame.

total_user_data_df = pd.DataFrame({"Purchase Count":players_purchase_count_df,
                                   "Average Purchase Price": players_average_price_df,
                                   "Total Purchase Value": players_total_df})
total_user_data_df.head()


# In[29]:


# Sort table to show the top five spenders.

top_five_spenders = total_user_data_df.sort_values("Total Purchase Value", ascending=False)
top_five_spenders.head()


# In[30]:


# Total items purchases analysis.

items_purchase_count_df = purchase_data_df.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")
items_average_price_df = purchase_data_df.groupby(["Item ID", "Item Name"]).mean()["Price"].rename("Average Purchase Price")
items_value_total_df = purchase_data_df.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")

# Convert to DataFrame

items_purchased_df = pd.DataFrame({"Purchase Count":items_purchase_count_df,
                                   "Item Price":items_average_price_df,
                                   "Total Purchase Value":items_value_total_df,})

items_purchased_df.head()


# In[31]:


# Sort table to show the five the most popular items.

most_popular_items_df = items_purchased_df.sort_values("Purchase Count", ascending=False)
most_popular_items_df.head()


# In[32]:


# Sort table to show the five the most profitable items.

most_profitable_items_df = items_purchased_df.sort_values("Total Purchase Value", ascending=False)
most_profitable_items_df.head()

