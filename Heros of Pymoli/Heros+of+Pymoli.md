
Heros of Pymoli Data Analysis.
1. The players are overwhelmingly male. There were 633 malae players and onl7 136 female players.
2. The 20-24 age group had the most purchases.
3. The total revenue generated for all players was $2286.33



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
# Read the purchase data csv file with the pandas library. Show header.

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

total_players_df = purchase_data_df["SN"]
total_players_df.head()
```




    0       Aelalis34
    1          Eolo46
    2     Assastnya25
    3    Pheusrical25
    4          Aela59
    Name: SN, dtype: object




```python
#Number of unique items.
items_df = len(purchase_data_df["Item Name"].value_counts())
items_df
```




    179




```python
#Average purchase price.

average_df = round(purchase_data_df["Price"].mean(), 2)
average_df
```




    2.9300000000000002




```python
#Total number of purchases.

total_purchases_df = len(purchase_data_df["Item Name"])
total_purchases_df
```




    780




```python
# Total Revenue.

total_revenue_df = round(purchase_data_df["Price"].sum(),2)
total_revenue_df
```




    2286.3299999999999




```python
purchasing_analysis_df = pd.DataFrame({"Number of Unique Items":[items_df],
                                             "Average Purchase Price":[average_df],
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
      <td>2.93</td>
      <td>179</td>
      <td>780</td>
      <td>2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Gender Count
gender_count_df = purchase_data_df["Gender"].value_counts()
gender_count_df.head()
```




    Male                     633
    Female                   136
    Other / Non-Disclosed     11
    Name: Gender, dtype: int64




```python
# Gender Percentage
gender_percentage_df = round(purchase_data_df["Gender"].value_counts()/780,2)
gender_percentage_df
```




    Male                     0.81
    Female                   0.17
    Other / Non-Disclosed    0.01
    Name: Gender, dtype: float64




```python

#Total number of purchases.

total_purchases_df = len(purchase_data_df["Item Name"])
total_purchases_df
```




    780




```python
female_count_df = purchase_data_df.loc[purchase_data_df["Gender"]=="Female",:]
female_count_df.head()
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
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>16</th>
      <td>22</td>
      <td>Female</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>1.14</td>
      <td>Sundista85</td>
    </tr>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Female players purchase count.

female_purchases_df = len(female_count_df["Item ID"])
female_purchases_df
```




    136




```python
# Average price of items brought by female players.

female_average_df = round(female_count_df["Price"].mean(),2)
female_average_df
```




    2.8199999999999998




```python
#Total Purchase value for female players.

female_total_df = round(female_count_df["Price"].sum(), 2)
female_total_df
```




    382.91000000000003




```python
#Normalized female total.
normalized_female_total_df = round(female_count_df["Price"].sum(), 2)/136
normalized_female_total_df
```




    2.8155147058823533




```python
purchase_data_df = purchase_data_df.reset_index(drop=True)
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
male_count_df = purchase_data_df.loc[purchase_data_df["Gender"]=="Male",:]
male_count_df.head()
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
#Male players purchase count.

male_purchases_df = len(male_count_df["Item ID"])
male_purchases_df
```




    633




```python
# Average price of items brought by male players.

male_average_df = round(male_count_df["Price"].mean(),2)
male_average_df
```




    2.9500000000000002




```python
#Total Purchase value for male players.

male_total_df = round(male_count_df["Price"].sum(), 2)
male_total_df
```




    1867.6800000000001




```python
#Normalized male total.
normalized_male_total_df = round(male_count_df["Price"].sum(), 2)/633
normalized_male_total_df
```




    2.9505213270142181




```python
#Other / Non-Diclosed player count.

other_count_df = purchase_data_df.loc[purchase_data_df["Gender"]=="Other / Non-Disclosed",:]
other_count_df
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
      <th>177</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>155</td>
      <td>War-Forged Gold Deflector</td>
      <td>3.73</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>209</th>
      <td>33</td>
      <td>Other / Non-Disclosed</td>
      <td>157</td>
      <td>Spada, Etcher of Hatred</td>
      <td>2.21</td>
      <td>Frichistasta59</td>
    </tr>
    <tr>
      <th>244</th>
      <td>21</td>
      <td>Other / Non-Disclosed</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Tyaerith73</td>
    </tr>
    <tr>
      <th>267</th>
      <td>33</td>
      <td>Other / Non-Disclosed</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Frichistasta59</td>
    </tr>
    <tr>
      <th>276</th>
      <td>12</td>
      <td>Other / Non-Disclosed</td>
      <td>128</td>
      <td>Blazeguard, Reach of Eternity</td>
      <td>4.00</td>
      <td>Aillycal84</td>
    </tr>
    <tr>
      <th>298</th>
      <td>26</td>
      <td>Other / Non-Disclosed</td>
      <td>141</td>
      <td>Persuasion</td>
      <td>3.27</td>
      <td>Faralcil63</td>
    </tr>
    <tr>
      <th>329</th>
      <td>27</td>
      <td>Other / Non-Disclosed</td>
      <td>61</td>
      <td>Ragnarok</td>
      <td>3.97</td>
      <td>Eurisuru25</td>
    </tr>
    <tr>
      <th>423</th>
      <td>32</td>
      <td>Other / Non-Disclosed</td>
      <td>29</td>
      <td>Chaos, Ender of the End</td>
      <td>3.79</td>
      <td>Aithelis62</td>
    </tr>
    <tr>
      <th>593</th>
      <td>22</td>
      <td>Other / Non-Disclosed</td>
      <td>115</td>
      <td>Spectral Diamond Doomblade</td>
      <td>4.25</td>
      <td>Euna48</td>
    </tr>
    <tr>
      <th>709</th>
      <td>34</td>
      <td>Other / Non-Disclosed</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Assassa38</td>
    </tr>
    <tr>
      <th>763</th>
      <td>27</td>
      <td>Other / Non-Disclosed</td>
      <td>48</td>
      <td>Rage, Legacy of the Lone Victor</td>
      <td>4.32</td>
      <td>Eurisuru25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Other/non-diclosed gender players purchase count.

other_purchases_df = len(other_count_df["Item ID"])
other_purchases_df
```




    11




```python
# Average price of items brought by other/non-disclosed players.

other_average_df = round(other_count_df["Price"].mean(),2)
other_average_df
```




    3.25




```python
#Total Purchase value for other/non-disclosed players.

other_total_df = round(other_count_df["Price"].sum(), 2)
other_total_df
```




    35.740000000000002




```python
#Normalized totals for other/non-disclosed players.

normalized_other_total_df = round(other_count_df["Price"].sum(), 2)/11
normalized_other_total_df
```




    3.2490909090909095




```python
female_purchase_analysis_df = pd.DataFrame({"Purchase Count":[female_purchases_df],
                                            "Average Purchase Price":[female_average_df],
                                            "Total Purchase Value":[female_total_df],
                                            "Normalized Total":[normalized_female_total_df]
})

female_purchase_analysis_df
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
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.82</td>
      <td>2.815515</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing analysis for male players.

male_purchase_analysis_df = pd.DataFrame({"Purchase Count":[male_purchases_df],
                                         "Average Purchase Price":[male_average_df],
                                         "Total Purchase Value":[male_total_df],
                                         "Normalized Total": [normalized_male_total_df]})
                                         
male_purchase_analysis_df
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
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.95</td>
      <td>2.950521</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Purchasing analysis for other/non-disclosed players.

other_purchase_analysis_df = pd.DataFrame({"Purchase Count":[other_purchases_df],
                                         "Average Purchase Price":[other_average_df],
                                         "Total Purchase Value":[other_total_df],
                                         "Normalized Total":[normalized_other_total_df]})
other_purchase_analysis_df
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
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.25</td>
      <td>3.249091</td>
      <td>11</td>
      <td>35.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
female_purchase_analysis_df.append(male_purchase_analysis_df).append(other_purchase_analysis_df)
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
      <th>Normalized Total</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.82</td>
      <td>2.815515</td>
      <td>136</td>
      <td>382.91</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.95</td>
      <td>2.950521</td>
      <td>633</td>
      <td>1867.68</td>
    </tr>
    <tr>
      <th>0</th>
      <td>3.25</td>
      <td>3.249091</td>
      <td>11</td>
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
age_group =purchase_data_df.groupby("Age Range")

print(age_group["SN"].count())
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
    Name: SN, dtype: int64



```python
Age_group_percentage_df = round(purchase_data_df["Age Range"].value_counts()/780,2)
Age_group_percentage_df
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
under_10_count_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "<10",:]
under_10_count_df.head()
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
      <th>70</th>
      <td>7</td>
      <td>Female</td>
      <td>158</td>
      <td>Darkheart, Butcher of the Champion</td>
      <td>3.56</td>
      <td>Eosurdru76</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>121</th>
      <td>7</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Lassjask63</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7</td>
      <td>Female</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Heosurnuru52</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>170</th>
      <td>9</td>
      <td>Male</td>
      <td>71</td>
      <td>Demise</td>
      <td>4.07</td>
      <td>Reulae52</td>
      <td>&lt;10</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
      <td>&lt;10</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Players under 10 purchase count.

under_10_purchases_df = len(under_10_count_df["Item ID"])
under_10_purchases_df
```




    32




```python
#Average price of items purchased by players under 10.


under10_average_df = round(under_10_count_df["Price"].mean(),2)
under10_average_df
```




    3.02




```python
#Total purchase value for players under 10.

under10_total_df = round(under_10_count_df["Price"].sum(), 2)
under10_total_df
```




    96.620000000000005




```python
#Normalized under 10 players total.
normalized_under10_total_df = round(under_10_count_df["Price"].sum(), 2)/32
normalized_under10_total_df
```




    3.0193750000000001




```python
#Filter players 10-14.

count_10to14_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "10-14",:]
count_10to14_df.head()
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
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
      <td>10-14</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Male</td>
      <td>17</td>
      <td>Lazarus, Terror of the Earth</td>
      <td>3.47</td>
      <td>Palatyon26</td>
      <td>10-14</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Players 10-14 purchase count.

purchases_10to14_df = len(count_10to14_df["Item ID"])
purchases_10to14_df
```




    78




```python
#Average price of items purchased by players 10 to 14.

average10to14_df = round(count_10to14_df["Price"].mean(),2)
average10to14_df
```




    2.8700000000000001




```python
#Total purchase value for players 10-14.

total_10to14_df = round(count_10to14_df["Price"].sum(), 2)
total_10to14_df
```




    224.15000000000001




```python
#Normalized total players 10 to 14.

norm_10to14_df = round(count_10to14_df["Price"].sum(), 2)/78
norm_10to14_df
```




    2.8737179487179487




```python
#Players 15-19 filter.

count15to19_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "15-19",:]
count15to19_df.head()
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
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Sally64</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>23</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Chanosia65</td>
      <td>15-19</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
      <td>15-19</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 15 to 19 purchase count.
purchase15to19_df = len(count15to19_df["Item ID"])
purchase15to19_df
```




    184




```python
#Average purchase price for players 15 to 19.

average15to19_df = round(count15to19_df["Price"].mean(),2)
average15to19_df
```




    2.8700000000000001




```python
#Total purchase value for 15 to 19.

total_15to19_df = round(count15to19_df["Price"].sum(),2)
total_15to19_df
```




    528.74000000000001




```python
#Normalized total players 15 to 19.

norm_15to19_df = round(count15to19_df["Price"].sum(), 2)/184
norm_15to19_df
```




    2.8735869565217391




```python
#Make a filter for players 20-24.

filter20to24_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "20-24",:]
filter20to24_df.head()
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
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total purchases for players 20-24.

purchases20to24_df = len(filter20to24_df["Item ID"])
purchases20to24_df
```




    305




```python
# Average purchase price players 20-24.

average20to24_df = round(filter20to24_df["Price"]).mean()
average20to24_df
```




    2.9344262295081966




```python
#Total purchase value players 20-24.
total20to24_df = round(filter20to24_df["Price"]).sum()
total20to24_df

```




    895.0




```python
# Normalized values for players 20 to 24.
norm20to24_df = round(filter20to24_df["Price"]).sum()/305
norm20to24_df

```




    2.9344262295081966




```python
#Make a filter for players 25-29. 
filter25to29_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "25-29",:]
filter25to29_df.head()
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
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
      <td>25-29</td>
    </tr>
    <tr>
      <th>79</th>
      <td>29</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Undirrala66</td>
      <td>25-29</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Total purchases for players 25-29.

tp_25to29_df = len(filter25to29_df["Item ID"])
tp_25to29_df
```




    76




```python
# Average purchase price for players 25-29.

average25to29_df = round(filter25to29_df["Price"]).mean()
average25to29_df
```




    2.8947368421052633




```python
#Total purchase value for players 25-29.

tvp_25to29_df = round(filter25to29_df["Price"]).sum()
tvp_25to29_df
```




    220.0




```python
#Normalized totals for players 25-29.

norm25to29_df = round(filter25to29_df["Price"]).sum()/76
norm25to29_df
```




    2.8947368421052633




```python
#Filter players 30 to 34.

filter30to34_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "30-34",:]
filter30to34_df.head()
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
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>37</th>
      <td>31</td>
      <td>Male</td>
      <td>171</td>
      <td>Scalpel</td>
      <td>3.62</td>
      <td>Sondossa91</td>
      <td>30-34</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Players 30 to 34 purchase count.

tp30to34_df = len(filter30to34_df["Item ID"])
tp30to34_df
```




    58




```python
# Average purchase price 30 to 34.

average30to34_df = round(filter30to34_df["Price"]).mean()
average30to34_df
```




    3.1206896551724137




```python
#Total purchase value for players ages 30 to 34.

total30to34_df = round(filter30to34_df["Price"]).sum()
total30to34_df
```




    181.0




```python
#Normalized total for players ages 30 to 34.

norm30to34_df = round(filter30to34_df["Price"]).sum()/58
norm30to34_df
```




    3.1206896551724137




```python
#Filter players ages 35 to 39.

filter35to39_df = purchase_data_df.loc[purchase_data_df["Age Range"] == "35-39",:]
filter35to39_df.head()
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
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>81</th>
      <td>38</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Yaristi64</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>106</th>
      <td>37</td>
      <td>Female</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Chadossa56</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>179</th>
      <td>40</td>
      <td>Male</td>
      <td>70</td>
      <td>Hope's End</td>
      <td>3.89</td>
      <td>Chanosiaya39</td>
      <td>35-39</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchase count for players 35-39.

count35to39_df = len(filter35to39_df["Item ID"])
count35to39_df
```




    44




```python
#Average purchase prices for players 35 to 39.

average35to39_df = round(filter35to39_df["Price"]).mean()
average35to39_df
```




    2.8409090909090908




```python
#Total purchase value for players 35 to 39.

total35to39_df = round(filter35to39_df["Price"]).sum()
total35to39_df
```




    125.0




```python
#Normalized values for players 35 to 39.

norm35to39_df = round(filter35to39_df["Price"]).sum()/44
norm35to39_df
```




    2.8409090909090908




```python
#Filter players 40 and over.

over40players_df = purchase_data_df.loc[purchase_data_df["Age Range"] == ">=40",:]
over40players_df.head()
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
      <th>264</th>
      <td>45</td>
      <td>Male</td>
      <td>124</td>
      <td>Venom Claymore</td>
      <td>2.72</td>
      <td>Marassaya49</td>
      <td>&gt;=40</td>
    </tr>
    <tr>
      <th>319</th>
      <td>42</td>
      <td>Male</td>
      <td>110</td>
      <td>Suspension</td>
      <td>2.11</td>
      <td>Lisista27</td>
      <td>&gt;=40</td>
    </tr>
    <tr>
      <th>644</th>
      <td>43</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Raesurdil91</td>
      <td>&gt;=40</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchase count for players 40 and over.

count40_df = len(over40players_df["Item ID"])
count40_df
```




    3




```python
#Average price for players 40 and over.

average40_df = round(over40players_df["Price"]).mean()
average40_df
```




    3.0




```python
#Total purchase value for players 40 and over.
total40_df = round(over40players_df["Price"]).sum()
total40_df

```




    9.0




```python
#Normalized values for players 40 and over.

norm40_df = round(over40players_df["Price"]).sum()/3
norm40_df
```




    3.0




```python
# Players under 10 summary.

under10_df = pd.DataFrame({"Purchase Count":[under_10_purchases_df],
               "Average Purchase Price":[under10_average_df],
               "Total Purchase Value":[under10_total_df],
               "Normalized Totals":[normalized_under10_total_df]})
under10_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.02</td>
      <td>3.019375</td>
      <td>32</td>
      <td>96.62</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 10 to 14 summary.

summary10to14_df = pd.DataFrame({"Purchase Count":[purchases_10to14_df],
               "Average Purchase Price":[average10to14_df],
               "Total Purchase Value":[total_10to14_df],
               "Normalized Totals":[norm_10to14_df]})
summary10to14_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.87</td>
      <td>2.873718</td>
      <td>78</td>
      <td>224.15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 15 to 19 summary.

summary15to19_df = pd.DataFrame({"Purchase Count":[purchase15to19_df],
               "Average Purchase Price":[average15to19_df],
               "Total Purchase Value":[total_15to19_df],
               "Normalized Totals":[norm_15to19_df ]})
summary15to19_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.87</td>
      <td>2.873587</td>
      <td>184</td>
      <td>528.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 20 to 24 summary.

summary20to24_df = pd.DataFrame({"Purchase Count":[purchases20to24_df],
               "Average Purchase Price":[average20to24_df],
               "Total Purchase Value":[total20to24_df],
                "Normalized Totals":norm20to24_df})
summary20to24_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.934426</td>
      <td>2.934426</td>
      <td>305</td>
      <td>895.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 25 to 29 summary.

summary25to29_df = pd.DataFrame({"Purchase Count":[tp_25to29_df],
               "Average Purchase Price":[average20to24_df],
               "Total Purchase Value":[tvp_25to29_df],
               "Normalized Totals":[norm25to29_df]})
summary25to29_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.934426</td>
      <td>2.894737</td>
      <td>76</td>
      <td>220.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 30 to 34 summary.

summary30to34_df = pd.DataFrame({"Purchase Count":[tp30to34_df],
               "Average Purchase Price":[average30to34_df],
               "Total Purchase Value":[total30to34_df],
               "Normalized Totals":[norm30to34_df]})
summary30to34_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.12069</td>
      <td>3.12069</td>
      <td>58</td>
      <td>181.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 35 to 39 summary.

summary35to39_df = pd.DataFrame({"Purchase Count":[count35to39_df],
               "Average Purchase Price":[average35to39_df],
               "Total Purchase Value":[total35to39_df],
               "Normalized Totals":[norm35to39_df]})
summary35to39_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.840909</td>
      <td>2.840909</td>
      <td>44</td>
      <td>125.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Players 40 and over summary.

summary40_df = pd.DataFrame({"Purchase Count":[count40_df],
               "Average Purchase Price":[average40_df],
               "Total Purchase Value":[total40_df],
               "Normalized Totals":norm40_df})
summary40_df
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.0</td>
      <td>3.0</td>
      <td>3</td>
      <td>9.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
under10_df.append(summary10to14_df.append(summary15to19_df.append(summary20to24_df.append(summary25to29_df.append(summary30to34_df.append(summary35to39_df.append(summary40_df)))))))
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
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3.020000</td>
      <td>3.019375</td>
      <td>32</td>
      <td>96.62</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.870000</td>
      <td>2.873718</td>
      <td>78</td>
      <td>224.15</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.870000</td>
      <td>2.873587</td>
      <td>184</td>
      <td>528.74</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.934426</td>
      <td>2.934426</td>
      <td>305</td>
      <td>895.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.934426</td>
      <td>2.894737</td>
      <td>76</td>
      <td>220.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>3.120690</td>
      <td>3.120690</td>
      <td>58</td>
      <td>181.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2.840909</td>
      <td>2.840909</td>
      <td>44</td>
      <td>125.00</td>
    </tr>
    <tr>
      <th>0</th>
      <td>3.000000</td>
      <td>3.000000</td>
      <td>3</td>
      <td>9.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Using GroupBy in order to separate the data into fields according to "Item Namw" values
grouped_items_df = purchase_data_df.groupby(['Item Name', 'Price'])

# The object returned is a "GroupBy" object and cannot be viewed normally...
print(grouped_items_df)

# In order to be visualized, a data function must be used...
grouped_items_df.count()
```

    <pandas.core.groupby.DataFrameGroupBy object at 0x117942278>





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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>SN</th>
      <th>Age Range</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th>Price</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Abyssal Shard</th>
      <th>2.04</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Aetherius, Boon of the Blessed</th>
      <th>4.75</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Agatha</th>
      <th>1.91</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Alpha</th>
      <th>1.56</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Alpha, Oath of Zeal</th>
      <th>2.88</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Alpha, Reach of Ending Hope</th>
      <th>1.55</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Amnesia</th>
      <th>3.57</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Apocalyptic Battlescythe</th>
      <th>3.91</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <th>2.23</th>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Avenger</th>
      <th>4.16</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Azurewrath</th>
      <th>2.22</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <th>2.35</th>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Betrayer</th>
      <th>1.67</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Blade of the Grave</th>
      <th>1.69</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Blazefury, Protector of Delusions</th>
      <th>1.50</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Blazeguard, Reach of Eternity</th>
      <th>4.00</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Blindscythe</th>
      <th>3.66</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Blood Infused Guardian</th>
      <th>2.86</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Blood-Forged Skeletal Spine</th>
      <th>4.77</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Bloodlord's Fetish</th>
      <th>2.28</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Bone Crushing Silver Skewer</th>
      <th>3.37</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Bonecarvin Battle Axe</th>
      <th>2.46</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Brimstone</th>
      <th>2.52</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Brutality Ivory Warmace</th>
      <th>1.72</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Celeste</th>
      <th>3.71</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Celeste, Incarnation of the Corrupted</th>
      <th>2.31</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Chaos, Ender of the End</th>
      <th>3.79</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Conqueror Adamantite Mace</th>
      <th>1.96</th>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">Crucifer</th>
      <th>2.28</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2.77</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>Thorn, Conqueror of the Corrupted</th>
      <th>2.04</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Thorn, Satchel of Dark Souls</th>
      <th>4.51</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Thunderfury Scimitar</th>
      <th>3.02</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Toothpick</th>
      <th>3.48</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Torchlight, Bond of Storms</th>
      <th>1.77</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Tranquility, Razor of Black Magic</th>
      <th>2.47</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <th>2.07</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Twilight's Carver</th>
      <th>1.14</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Undead Crusader</th>
      <th>4.67</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Unending Tyranny</th>
      <th>1.21</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Unholy Wand</th>
      <th>1.88</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Vengeance Cleaver</th>
      <th>3.70</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Venom Claymore</th>
      <th>2.72</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Verdict</th>
      <th>3.40</th>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Victor Iron Spikes</th>
      <th>3.55</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Vindictive Glass Edge</th>
      <th>4.26</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>War-Forged Gold Deflector</th>
      <th>3.73</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Warmonger, Gift of Suffering's End</th>
      <th>3.96</th>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Warped Diamond Crusader</th>
      <th>4.66</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Warped Fetish</th>
      <th>2.41</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Warped Iron Scimitar</th>
      <th>4.08</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Whistling Mithril Warblade</th>
      <th>4.32</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Winter's Bite</th>
      <th>1.39</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Winterthorn, Defender of Shifting Worlds</th>
      <th>4.89</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Woeful Adamantite Claymore</th>
      <th>1.24</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Wolf</th>
      <th>1.84</th>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Wolf, Promise of the Moonwalker</th>
      <th>1.88</th>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Worldbreaker</th>
      <th>3.29</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Yearning Crusher</th>
      <th>1.06</th>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Yearning Mageblade</th>
      <th>1.79</th>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
<p>183 rows × 5 columns</p>
</div>




```python
count = purchase_data_df['Item Name'].value_counts()
count.head()
```




    Final Critic                            14
    Arcane Gem                              11
    Betrayal, Whisper of Grieving Widows    11
    Stormcaller                             10
    Serenity                                 9
    Name: Item Name, dtype: int64




```python
count = purchase_data_df['Item ID'].value_counts()
count.head()
```




    84     11
    39     11
    31      9
    34      9
    175     9
    Name: Item ID, dtype: int64




```python
purchase_data_df.groupby(['SN', 'Item Name'])['SN'].count()
```




    SN              Item Name                                   
    Adairialis76    Bonecarvin Battle Axe                           1
    Aduephos78      Alpha, Oath of Zeal                             1
                    Final Critic                                    1
                    Primitive Blade                                 1
    Aeduera68       Betrayal, Whisper of Grieving Widows            1
                    Crying Steel Sickle                             1
                    Soul-Forged Steel Shortsword                    1
    Aela49          Bonecarvin Battle Axe                           1
    Aela59          Stormfury Mace                                  1
    Aelalis34       Blade of the Grave                              1
                    Bone Crushing Silver Skewer                     1
    Aelin32         Eternal Cleaver                                 1
    Aeliriam77      Orenmir                                         1
                    Torchlight, Bond of Storms                      1
    Aeliriarin93    Thorn, Conqueror of the Corrupted               1
    Aeliru63        Stormcaller                                     1
                    Stormfury Longsword                             1
    Aellyria80      Whistling Mithril Warblade                      1
    Aellyrialis39   Darkheart                                       1
    Aellysup38      Splitter, Foe Of Subtlety                       1
    Aelollo59       Fate, Vengeance of Eternal Justice              1
    Aenarap34       Lightning, Etcher of the King                   1
    Aenasu69        Persuasion                                      1
    Aeral43         Venom Claymore                                  1
    Aeral85         Spectral Diamond Doomblade                      1
    Aeral97         Betrayal, Whisper of Grieving Widows            1
    Aeri84          Betrayal, Whisper of Grieving Widows            1
                    Spectral Diamond Doomblade                      1
    Aerillorin70    Wolf, Promise of the Moonwalker                 1
    Aerithllora36   Dreamkiss                                       1
                                                                   ..
    Yadanun74       Worldbreaker                                    1
    Yalaeria91      Wolf, Promise of the Moonwalker                 1
    Yaliru88        Celeste                                         1
    Yalo71          Warped Fetish                                   1
    Yalostiphos68   Renewed Skeletal Katana                         1
    Yaralnura48     Alpha, Reach of Ending Hope                     1
                    Sun Strike, Jaws of Twisted Visions             1
    Yararmol43      Alpha, Reach of Ending Hope                     1
    Yarirarn35      Alpha, Oath of Zeal                             1
    Yaristi64       Woeful Adamantite Claymore                      1
    Yarithllodeu72  Feral Katana                                    1
    Yarithphos28    Betrayal, Whisper of Grieving Widows            1
    Yarithsurgue62  Nirvana                                         1
                    Vengeance Cleaver                               1
    Yarmol79        Misery's End                                    1
    Yarolwen77      Arcane Gem                                      1
                    Hopeless Ebon Dualblade                         1
    Yasriphos60     Brimstone                                       1
                    Scalpel                                         1
                    Vindictive Glass Edge                           1
    Yasrisu92       Frenzied Scimitar                               1
    Yasur35         Stormcaller                                     1
    Yasur85         Thorn, Conqueror of the Corrupted               1
    Yasurra52       Eternal Cleaver                                 1
    Yathecal72      Restored Bauble                                 1
                    Warped Diamond Crusader                         1
    Yathecal82      Oathbreaker, Last Hope of the Breaking Storm    1
    Zhisrisu83      Curved Axe                                      1
                    Nirvana                                         1
    Zontibe81       Celeste                                         1
    Name: SN, Length: 777, dtype: int64




```python
# Set new index to last_name
sn_purchase_data_df = purchase_data_df.set_index("SN")
sn_purchase_data_df.head()
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
      <th>Age Range</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Aelalis34</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>35-39</td>
    </tr>
    <tr>
      <th>Eolo46</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>Assastnya25</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>30-34</td>
    </tr>
    <tr>
      <th>Pheusrical25</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>20-24</td>
    </tr>
    <tr>
      <th>Aela59</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>20-24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#total players purchase count.

total_purchases_df = sn_purchase_data_df["Item ID"].value_counts()
total_purchases_df
```




    84     11
    39     11
    31      9
    34      9
    175     9
    13      9
    106     8
    44      8
    92      8
    65      8
    152     8
    107     8
    172     7
    179     7
    115     7
    154     7
    79      7
    158     7
    108     7
    66      7
    11      7
    130     7
    18      7
    124     6
    103     6
    101     6
    121     6
    102     6
    73      6
    145     6
           ..
    116     2
    89      2
    64      2
    9       2
    167     2
    80      2
    74      2
    72      2
    146     2
    149     2
    150     2
    178     2
    62      2
    58      2
    56      2
    55      2
    4       1
    2       1
    3       1
    59      1
    28      1
    168     1
    164     1
    43      1
    156     1
    147     1
    136     1
    126     1
    109     1
    0       1
    Name: Item ID, Length: 183, dtype: int64


