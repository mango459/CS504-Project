# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:18:46 2024

@author: apaige
"""
# Import Libraries 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset as a Dataframe 
df = pd.read_excel(r"C:\Users\apaige\Downloads\preprocessed_data.xlsx")

# Histogram - Tract Income Ratio Distribution
plt.figure(figsize=(10,6))
df['tract_income_ratio'].hist(bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Frequency')
plt.show()

# Histogram - Tract Income Ratio Distribution (without gridlines)
# This plot tells us that for all 3 Income Ratio Tracks, the median number of housing units is 0.
# This plot also shows that the Distribution of housing units is concentrated around 0
# Overall, the number of housing units across all income ratio tracts is sparse
# This corroborates other data highlighting housing shortages across the United States
plt.figure(figsize=(10,6))
plt.hist(df['tract_income_ratio'], bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Frequency')
plt.show()

# Histogram - Distribution of Affordable Housing Units
# This plot shows us that the vast majorities of multifamily properties do not have any affordable units
plt.figure(figsize=(10,6))
plt.hist(df['num_affordable_units'], bins=30, color='brown', edgecolor='black')
plt.title('Distribution of Affordable Units')
plt.xlabel('Affordable Housing Units')
plt.ylabel('Frequency')
plt.show()

# Violin Plot - Income tract ratio vs. Unit Volume
plt.figure(figsize=(10,6))
sns.violinplot(x='tract_income_ratio', y='num_units', data=df, palette='muted')
plt.title('Distribution of Housing Units Across Tract Income Ratios')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Number of Housing Units')
plt.show()

# Violin - Distribution of Affordable housing units across Income Ratio Tracts
plt.figure(figsize=(10,6))
sns.violinplot(x='tract_income_ratio', y='num_affordable_units', data=df, palette='muted')

# Overlay the individual data points with stripplot
sns.stripplot(x='tract_income_ratio', y='num_affordable_units', data=df, 
              color='k', jitter=True, dodge=True, marker='o', alpha=0.5)

# Add data labels to each point
for i in range(df.shape[0]):
    plt.text(df['tract_income_ratio'].iloc[i], df['num_affordable_units'].iloc[i], 
             f'{df["num_affordable_units"].iloc[i]}', horizontalalignment='center', 
             size=8, color='black', alpha=0.7)

# Add titles and labels
plt.title('Distribution of Affordable Housing Units Across Tract Income Ratios')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Number of Affordable Housing Units')

# Show the plot
plt.show()


# Scatterplot - Income Ratio Tract vs. Number of Housing Units 
# This plot shows use that the number of housing units for all 3 income ratio tracts falls under 1000
plt.figure(figsize=(10,6))
sns.scatterplot(x='tract_income_ratio', y='num_units', data=df, color='purple', alpha=0.6)
plt.title('Housing Units vs. Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Number of Housing Units')
plt.show()

# Scatterplot - Income Ratio Tract vs. Number of Affordable Housing Units
plt.figure(figsize=(10,6))
sns.scatterplot(x='tract_income_ratio', y='num_affordable_units', data=df, color='purple', alpha=0.6)
plt.title('Affordable Housing Units vs. Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Number of Affordable Housing Units')
plt.show() 


# Scatterplot - Income Ratio Tract vs. Number of Affordable Housing Units
plt.figure(figsize=(10,6))
sns.scatterplot(x='tract_income_ratio', y='num_affordable_units', data=df, color='green', alpha=0.6)
plt.title('Housing Units vs. Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Number of Affordable Housing Units')
plt.show()

# Kernel Density Estimate - shows the probability density of the tract_income ratio values
plt.figure(figsize=(10,6))
sns.kdeplot(df['tract_income_ratio'], fill=True, color='green', linewidth=2)
plt.title('Density of Tract Income Ratio')
plt.xlabel('Tract Income Ratio')
plt.ylabel('Density')
plt.show()



