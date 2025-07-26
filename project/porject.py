import numpy as np
import pandas as pd

# loading the dataset
df=pd.read_csv("C:\\Users\\Lenovo\\Desktop\\project\\data.csv",encoding='latin1')
print(df.head())

#checking structure
print(df.info())
print("describe")
print(df.describe())
print("columns")
print(df.columns)

# checking the missing values
print("missing values" )
print(df.isnull().sum())
# there is no mising values in our data 

#  1 - Which region has the highest sales?
# group method  for region and sum
region1=df.groupby("Region")["Sales"].sum()
print(region1)

print("\n the higest sale is : " ,region1.max())

# 2- which category brings most profit
product=df.groupby("Category")["Profit"].sum()
print(product)
print(" \n the higest profit : " ,product.max())

# 3-top most profitable cities

city=df.groupby("City")["Profit"].sum()
top_10_cities=city.sort_values(ascending=False).head(10)
print("\n here are the top 10  profitable cites : ",top_10_cities)

# 3-top most loss making cities
top_10_cities=city.sort_values(ascending=True).head(10)
print("\n here are the top 10  loss making cites : ",top_10_cities)

# 4 - Which sub-category has good sales but poor profit? 
sub=df.groupby("Sub-Category")[["Sales","Profit"]].sum()
print(sub)
 # now sorting them in descending order so that we can know which sub category gives poor profit
sub_cat=sub.sort_values(by="Sales",ascending=False)
print('\n',sub_cat)

# 5 - overall trend of orders by Ship Mode, Segment, etc.?

#count orders by ship mode
mode=df["Ship Mode"].value_counts()
print("\n order count by ship mode")

print(mode)
#count orders by segment
seg=df["Segment"].value_counts()
print("\n order count by segment")

print(seg)
#now combine by usnig groupby 
mode_seg=df.groupby(["Ship Mode","Segment"]).size().sort_values(ascending=False)
print("\n order count by ship mode and segment")
print(mode_seg)

# df.to_csv("cleaned_data.csv",index=False)