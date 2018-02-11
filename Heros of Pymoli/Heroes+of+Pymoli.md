
Heros of Pymoli Data Analysis.
1. The players are overwhelmingly male. There were 633 male players and only 136 female players.
2. The 20-24 age group purchases the most items and had the highest purchase amount of all age groups.
3. The total revenue generated for all players was $2286.33.
4. it would be intereting to see the ages of the top five spenders to see if they are in the 20-24 age group that purchased the most items and had the highest purchase amount.



```python
#Dependencies

import pandas as pd
import numpy as np
```


```python
#Store file path as a variable.

purchase_data = "Resources/purchase_data.json"

```


```python
# Read the purchase data JSON file with the pandas library. Show header.

purchase_data_df = pd.read_json(purchase_data)
purchase_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Display a statistical overview of the purchase data.
purchase_data_df.describe()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>780.000000</td>
      <td>780.000000</td>
      <td>780.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>22.729487</td>
      <td>91.293590</td>
      <td>2.931192</td>
    </tr>
    <tr>
      <th>std</th>
      <td>6.930604</td>
      <td>52.707537</td>
      <td>1.115780</td>
    </tr>
    <tr>
      <th>min</th>
      <td>7.000000</td>
      <td>0.000000</td>
      <td>1.030000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.000000</td>
      <td>44.000000</td>
      <td>1.960000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>22.000000</td>
      <td>91.000000</td>
      <td>2.880000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>25.000000</td>
      <td>135.000000</td>
      <td>3.910000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>45.000000</td>
      <td>183.000000</td>
      <td>4.950000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total number of players.

players_df = purchase_data_df.groupby("SN")["SN"].nunique()
players_df.count()
```




    573




```python
#Number of unique items.

items_df = purchase_data_df.groupby("Item Name")["Item Name"].nunique()
items_df.count()
```




    179




```python
#Average purchase price.

average_price_df = purchase_data_df["Price"].mean()
average_price_df.round(2)
```




    2.9300000000000002




```python
#Total number of purchases.

total_purchases_df = len(purchase_data_df)
total_purchases_df
```




    780




```python
# Total Revenue.

total_revenue_df = purchase_data_df["Price"].sum()
total_revenue_df.round(2)
```




    2286.3299999999999




```python
purchasing_analysis_df = pd.DataFrame({"Number of Unique Items":[items_df],
                                             "Average Purchase Price":[average_price_df],
                                            "Total Number of Purchases":[total_purchases_df],
                                             "Total Revenue":[total_revenue_df]})
purchasing_analysis_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Number of Unique Items</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.931192</td>
      <td>Item Name
Abyssal Shard                       ...</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Count
gender_count_df = purchase_data_df.groupby("Gender")["SN"].nunique()
gender_count_df.head()
```




    Gender
    Female                   100
    Male                     465
    Other / Non-Disclosed      8
    Name: SN, dtype: int64




```python
# Gender Percentage
gender_percentage_df = gender_count_df/573
gender_percentage_df.round(2)
```




    Gender
    Female                   0.17
    Male                     0.81
    Other / Non-Disclosed    0.01
    Name: SN, dtype: float64




```python
#Gender demographics DataFrame.

gender_demographics_df = pd.DataFrame({"Gender Count": gender_count_df,"Gender Percentage":gender_percentage_df})
gender_demographics_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender Count</th>
      <th>Gender Percentage</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>0.174520</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>0.811518</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
      <td>0.013962</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total number of purchases by gender.


gender_purchases_df = purchase_data_df.groupby("Gender")["Item Name"]
gender_purchases_df.count()
```




    Gender
    Female                   136
    Male                     633
    Other / Non-Disclosed     11
    Name: Item Name, dtype: int64




```python
# Average price of items by gender.

gender_average_df = purchase_data_df.groupby("Gender")["Price"].mean()
gender_average_df.round(2)
```




    Gender
    Female                   2.82
    Male                     2.95
    Other / Non-Disclosed    3.25
    Name: Price, dtype: float64




```python
#Total Purchase value by gender.

gender_total_df = purchase_data_df.groupby("Gender")["Price"].sum()
gender_total_df
```




    Gender
    Female                    382.91
    Male                     1867.68
    Other / Non-Disclosed      35.74
    Name: Price, dtype: float64




```python
#Normalized gender total.
normalized_gender_total_df = gender_total_df/gender_count_df
normalized_gender_total_df.round(2)
```




    Gender
    Female                   3.83
    Male                     4.02
    Other / Non-Disclosed    4.47
    dtype: float64




```python
# Purchasing analysis DataFrame by gender.

gender_analysis_df = pd.DataFrame({"Purchase Count":gender_purchases_df, 
                                   "Average Purchase Price":gender_average_df,
                                   "Total Purchase Value":gender_total_df,
                                   "Normalized Totals":normalized_gender_total_df})
gender_analysis_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>2.815515</td>
      <td>3.829100</td>
      <td>(Female, [Interrogator, Blood Blade of the Que...</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>2.950521</td>
      <td>4.016516</td>
      <td>(Male, [Bone Crushing Silver Skewer, Stormbrin...</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>3.249091</td>
      <td>4.467500</td>
      <td>(Other / Non-Disclosed, [War-Forged Gold Defle...</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Create bins in which data will be held. Bins are <10, 10-14, 15-19, 20-24, 25-29, 30-34, 35-39 >39.

bins = [0,10,15,20,25,30,35,40, 45]
age_ranges = ["<10", "10-14","15-19", "20-24", "25-29", "30-34", "35-39", ">=40"]
```


```python
# Cut purchase data and place the ages into bins
pd.cut(purchase_data_df["Age"], bins, labels=age_ranges)

```




    0      35-39
    1      20-24
    2      30-34
    3      20-24
    4      20-24
    5      15-19
    6      15-19
    7      25-29
    8      20-24
    9      30-34
    10     20-24
    11     15-19
    12     25-29
    13     20-24
    14     35-39
    15     20-24
    16     20-24
    17     20-24
    18     25-29
    19     30-34
    20     20-24
    21     10-14
    22     10-14
    23     15-19
    24     10-14
    25     20-24
    26     25-29
    27     30-34
    28     10-14
    29     15-19
           ...  
    750    20-24
    751    25-29
    752    10-14
    753    15-19
    754    30-34
    755    20-24
    756    20-24
    757    30-34
    758    15-19
    759    15-19
    760    25-29
    761    25-29
    762    35-39
    763    25-29
    764    20-24
    765    10-14
    766    20-24
    767    15-19
    768    20-24
    769    20-24
    770    20-24
    771    20-24
    772    10-14
    773    20-24
    774    20-24
    775    20-24
    776    10-14
    777    15-19
    778    15-19
    779    20-24
    Name: Age, Length: 780, dtype: category
    Categories (8, object): [<10 < 10-14 < 15-19 < 20-24 < 25-29 < 30-34 < 35-39 < >=40]




```python
purchase_data_df["Age Range"] = pd.cut(purchase_data_df["Age"], bins, labels= age_ranges)
purchase_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age Range</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Players percentage by age range.

age_group_percentage_df = round(purchase_data_df["Age Range"].value_counts()/780,2)
age_group_percentage_df
```




    20-24    0.39
    15-19    0.24
    10-14    0.10
    25-29    0.10
    30-34    0.07
    35-39    0.06
    <10      0.04
    >=40     0.00
    Name: Age Range, dtype: float64




```python
# Purchase count by age range.

age_group_count_df = purchase_data_df.groupby("Age Range")["Item Name"]
age_group_count_df.count()
```




    Age Range
    <10       32
    10-14     78
    15-19    184
    20-24    305
    25-29     76
    30-34     58
    35-39     44
    >=40       3
    Name: Item Name, dtype: int64




```python
# Average purchase price by age range.

age_group_average_df = purchase_data_df.groupby("Age Range")["Price"].mean()
age_group_average_df.round(2)
```




    Age Range
    <10      3.02
    10-14    2.87
    15-19    2.87
    20-24    2.96
    25-29    2.89
    30-34    3.07
    35-39    2.90
    >=40     2.88
    Name: Price, dtype: float64




```python
#Total purchase value by age range.

age_group_total_df = purchase_data_df.groupby("Age Range")["Price"].sum()
age_group_total_df
```




    Age Range
    <10       96.62
    10-14    224.15
    15-19    528.74
    20-24    902.61
    25-29    219.82
    30-34    178.26
    35-39    127.49
    >=40       8.64
    Name: Price, dtype: float64




```python
#Normalized totals by age range.

normalized_age_total_df = age_group_total_df/573
normalized_age_total_df.round(2)
```




    Age Range
    <10      0.17
    10-14    0.39
    15-19    0.92
    20-24    1.58
    25-29    0.38
    30-34    0.31
    35-39    0.22
    >=40     0.02
    Name: Price, dtype: float64




```python
# Convert to DataFrame.

age_range_df = pd.DataFrame({"Purchase Count":age_group_count_df,
                            "Average Purchase Price":age_group_average_df,
                            "Total Purchase Value": age_group_total_df,
                            "Normalized Totals": normalized_age_total_df
})
age_range_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Normalized Totals</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Age Range</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.019375</td>
      <td>0.168621</td>
      <td>(&lt;10, [Darkheart, Butcher of the Champion, Woe...</td>
      <td>96.62</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>2.873718</td>
      <td>0.391187</td>
      <td>(10-14, [Phantomlight, Brimstone, Conqueror Ad...</td>
      <td>224.15</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>2.873587</td>
      <td>0.922757</td>
      <td>(15-19, [Sleepwalker, Mercenary Sabre, Alpha, ...</td>
      <td>528.74</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>2.959377</td>
      <td>1.575236</td>
      <td>(20-24, [Stormbringer, Dark Blade of Ending Mi...</td>
      <td>902.61</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>2.892368</td>
      <td>0.383630</td>
      <td>(25-29, [Interrogator, Blood Blade of the Quee...</td>
      <td>219.82</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>3.073448</td>
      <td>0.311099</td>
      <td>(30-34, [Primitive Blade, Expiration, Warscyth...</td>
      <td>178.26</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>2.897500</td>
      <td>0.222496</td>
      <td>(35-39, [Bone Crushing Silver Skewer, Bonecarv...</td>
      <td>127.49</td>
    </tr>
    <tr>
      <th>&gt;=40</th>
      <td>2.880000</td>
      <td>0.015079</td>
      <td>(&gt;=40, [Venom Claymore, Suspension, Despair, F...</td>
      <td>8.64</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Overall spending analysis

players_purchase_count_df = purchase_data_df.groupby("SN").count()["Price"].rename("Purchase Count")
players_average_price_df = purchase_data_df.groupby("SN").mean()["Price"].rename("Average Purchase Price")
players_total_df = purchase_data_df.groupby("SN").sum()["Price"].rename("Total Purchase Value")

#Convert to DataFrame.

total_user_data_df = pd.DataFrame({"Purchase Count":players_purchase_count_df,
                                   "Average Purchase Price": players_average_price_df,
                                   "Total Purchase Value": players_total_df})
total_user_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Adairialis76</th>
      <td>2.460000</td>
      <td>1</td>
      <td>2.46</td>
    </tr>
    <tr>
      <th>Aduephos78</th>
      <td>2.233333</td>
      <td>3</td>
      <td>6.70</td>
    </tr>
    <tr>
      <th>Aeduera68</th>
      <td>1.933333</td>
      <td>3</td>
      <td>5.80</td>
    </tr>
    <tr>
      <th>Aela49</th>
      <td>2.460000</td>
      <td>1</td>
      <td>2.46</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>1.270000</td>
      <td>1</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sort table to show the top five spenders.

top_five_spenders = total_user_data_df.sort_values("Total Purchase Value", ascending=False)
top_five_spenders.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>3.412000</td>
      <td>5</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>3.390000</td>
      <td>4</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>3.185000</td>
      <td>4</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>4.243333</td>
      <td>3</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3.860000</td>
      <td>3</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Total items purchases analysis.

items_purchase_count_df = purchase_data_df.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Count")
items_average_price_df = purchase_data_df.groupby(["Item ID", "Item Name"]).mean()["Price"].rename("Average Purchase Price")
items_value_total_df = purchase_data_df.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")

# Convert to DataFrame

items_purchased_df = pd.DataFrame({"Purchase Count":items_purchase_count_df,
                                   "Item Price":items_average_price_df,
                                   "Total Purchase Value":items_value_total_df,})

items_purchased_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <th>Splinter</th>
      <td>1.82</td>
      <td>1</td>
      <td>1.82</td>
    </tr>
    <tr>
      <th>1</th>
      <th>Crucifer</th>
      <td>2.28</td>
      <td>4</td>
      <td>9.12</td>
    </tr>
    <tr>
      <th>2</th>
      <th>Verdict</th>
      <td>3.40</td>
      <td>1</td>
      <td>3.40</td>
    </tr>
    <tr>
      <th>3</th>
      <th>Phantomlight</th>
      <td>1.79</td>
      <td>1</td>
      <td>1.79</td>
    </tr>
    <tr>
      <th>4</th>
      <th>Bloodlord's Fetish</th>
      <td>2.28</td>
      <td>1</td>
      <td>2.28</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sort table to show the five the most popular items.

most_popular_items_df = items_purchased_df.sort_values("Purchase Count", ascending=False)
most_popular_items_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>2.35</td>
      <td>11</td>
      <td>25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>2.23</td>
      <td>11</td>
      <td>24.53</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>2.07</td>
      <td>9</td>
      <td>18.63</td>
    </tr>
    <tr>
      <th>175</th>
      <th>Woeful Adamantite Claymore</th>
      <td>1.24</td>
      <td>9</td>
      <td>11.16</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>1.49</td>
      <td>9</td>
      <td>13.41</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Sort table to show the five the most profitable items.

most_profitable_items_df = items_purchased_df.sort_values("Total Purchase Value", ascending=False)
most_profitable_items_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>4.14</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>4.25</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>4.95</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>4.87</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>3.61</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>


