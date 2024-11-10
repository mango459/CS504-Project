#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:19:30 2024

@author: andreapaloschavez
"""

import pandas as pd

# Load the data from the csv file
data_path = '/Users/andreapaloschavez/Library/CloudStorage/OneDrive-Avantus/CS504/python/raw_19-23.csv'
csv = pd.read_csv(data_path)

# Create DataFrame
df = pd.DataFrame(csv)

# Calculate basic statistics for numerical fields
statistics = {
    'mean': df.mean(),
    'median': df.median(),
    'mode': df.mode().iloc[0],
    'range': df.max() - df.min()
}

# Convert to DataFrame for better display
statistics_df = pd.DataFrame(statistics)

print(statistics_df)

import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot categorical distributions
def plot_categorical_distribution(df, column, title):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=column, order=df[column].value_counts().index, palette='Set2')
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Analyze and plot distributions for categorical variables
plot_categorical_distribution(df, 'enterprise_flag', 'Distribution of Enterprise Flag')
plot_categorical_distribution(df, 'affordability_cat', 'Distribution of Affordability Category')
plot_categorical_distribution(df, 'purpose_of_loan', 'Distribution of Purpose of Loan')
plot_categorical_distribution(df, 'type_of_seller', 'Distribution of Type of Seller')

# Display frequency counts for each categorical variable
for column in ['enterprise_flag', 'affordability_cat', 'purpose_of_loan', 'type_of_seller']:
    print(f'Frequency Counts for {column}:')
    print(df[column].value_counts())
    print()

# Note: import plotly.express as px works if you aren't using Spyder
# My setup is finicky so I send it to browser to view the visuals
import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser'
    
# Distribution of Properties by Affordability Category 
# to identify trends in affordable housing availability
def plot_affordability_distribution(df):
    fig = px.histogram(df, x='affordability_cat', 
                       title='Distribution of Properties by Affordability Category', 
                       labels={'affordability_cat': 'Affordability Category'},
                       color_discrete_sequence=['#636EFA'])
    fig.update_layout(xaxis_title='Affordability Category', yaxis_title='Count')
    fig.show()

plot_affordability_distribution(df)
# The high count in category 4 may imply that a substantial number of properties 
# are affordable to families making around 80-100% of the Area Median Income (AMI).
# The limited representation in lower affordability categories could raise concerns 
# about accessibility to affordable housing for very low-income families, 
# highlighting an area for potential policy intervention or further investigation.

    
# Analyze Relationship Between Tract Income Ratio and Affordability Category 
# to see how income levels influence housing affordability.
def plot_income_ratio_by_affordability(df):
    fig = px.box(df, x='affordability_cat', y='tract_income_ratio',
                 title='Tract Income Ratio by Affordability Category',
                 labels={'affordability_cat': 'Affordability Category', 'tract_income_ratio': 'Tract Income Ratio'},
                 color='affordability_cat', 
                 color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_layout(yaxis_title='Tract Income Ratio', xaxis_title='Affordability Category')
    fig.show()
    
plot_income_ratio_by_affordability(df)
# The median income ratios for affordability categories 0 and 4 appear lower 
# compared to categories 1 and 2, suggesting that properties categorized as 
# less affordable are found in areas with lower median incomes.
# The data suggests that lower tract income ratios correlate with higher 
# affordability categories, meaning that as income levels decrease, the 
# affordability of housing options also tends to improve, albeit limitedly