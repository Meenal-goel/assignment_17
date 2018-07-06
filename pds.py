#1-Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.

import pandas as pd
import numpy as np

info = {
        'name':['Meenal'],
        'age' :[18],
        'mail id':['mnl02@gmail.com'],
        'phone no.':[9854712563]
       }

df1 = pd.DataFrame(info)
print("MY INFO:\n",df1)
print("-"*20)
print("\n")
info_f1 = {
        'name':['Anshul'],
        'age' :[17],
        'mail id':['anshul03@gmail.com'],
        'phone no.':[7854712563]
       }
info_f2 = {
        'name':['Riya'],
        'age' :[18],
        'mail id':['riya06@gmail.com'],
        'phone no.':[9814712563]
       }
info_f3 = {
        'name':['Gauri'],
        'age' :[19],
        'mail id':['gauri06@gmail.com'],
        'phone no.':[9054712563]
        
       }
df2 = pd.DataFrame(info_f1)
df3 = pd.DataFrame(info_f2)
df4 = pd.DataFrame(info_f3)
list_try = [df2,df3,df4]

for i in list_try:
    df1 = df1.append(i,ignore_index =True)
    
print("After ADDING FRIENDS' INFO: \n",df1)
print("\n")
print("*"*80)
print("\n")

#2-Download the dataset from this link , 
'''Import the data and print the following :
a.) First 5 rows of Dataframe 
b.) First 10 rows of the Dataframe 
c.) find basic statistics on the particular dataset. 
d.) Find the last 5 rows of the dataframe 
e.) Extract the 2nd column and find basic statistics on it.'''

import pandas as pd

dff = pd.read_csv("C:/Git/assignment_17/weather.csv")
print("First 5 rows of Dataframe ")
print("-"*80)
first_5 = dff.head()
print(first_5)
print("\n")

print("First 10 rows of the Dataframe ")
print("-"*80)
first_10 = dff.head(10)
print(first_10)
print("\n")

print(" Basic statistics on the particular dataset")
print("-"*80)
basic_part = dff.describe()
print(basic_part)
print("\n")

print("Last 5 rows of the dataframe ")
print("-"*80)
last_5 = dff.tail()
print(last_5)
print("\n")

print(" Extract the 2nd column and find basic statistics on it.")
print("-"*80)
cols = [1]
basic = dff[dff.columns[cols]]
print(basic)

