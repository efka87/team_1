#Task 1: Create a bar chart that shows the count of customers for each unique value in the 'Gender' column (including NaN values). 

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('/content/transaction_dataset.csv')
gender_counts = dataset['Gender'].value_counts(dropna=False)

gender_counts.plot(kind='bar', edgecolor='black')

plt.title('Count of Customers by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


#Create a horizontal bar chart that shows the top 5 most frequent names in the DataFrame, based on the 'name' column. 
#First, create a grouped DataFrame (name_df), then filter it using iloc, and finally create the visualization.)

name_df = dataset.groupby('Name').size().reset_index(name = 'count')
name_df = name_df.sort_values(by ='count', ascending = False)
name_df = name_df.iloc[:5]


plt.barh(name_df['Name'], name_df['count'], color='skyblue')
plt.xlabel('Count')
plt.ylabel('Name')
plt.title('Top 5 Most Frequent Names')
