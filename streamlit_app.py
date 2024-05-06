import streamlit as st
import pandas as pd
import ast
import re

# Directory path
path = "C:/Research/SEC-EDGAR-Analysis/scripts/model_gen_data_extracted/"
# Read the CSV files for each company
df_aapl = pd.read_csv(path + 'AAPL_extracted1.csv', header=None)
df_goog = pd.read_csv(path + 'GOOG_extracted1.csv', header=None)
df_meta = pd.read_csv(path + 'META_extracted1.csv', header=None)

# Convert the strings in each row to lists
df_aapl = df_aapl.map(ast.literal_eval)
df_goog = df_goog.map(ast.literal_eval)
df_meta = df_meta.map(ast.literal_eval)

# Transpose the DataFrames
df_aapl = df_aapl.T
df_goog = df_goog.T
df_meta = df_meta.T

# Set column names
df_aapl.columns = ['Employees', 'Stock Prices', 'Year']
df_goog.columns = ['Employees', 'Stock Prices', 'Year']
df_meta.columns = ['Employees', 'Stock Prices', 'Year']

# Explode lists into columns
df_aapl = df_aapl.apply(pd.Series.explode).reset_index(drop=True)
df_goog = df_goog.apply(pd.Series.explode).reset_index(drop=True)
df_meta = df_meta.apply(pd.Series.explode).reset_index(drop=True)


def convert_to_numeric(df):
    # Convert 'Employees' column to integers
    df['Employees'] = df['Employees'].apply(lambda x: int(re.sub(r'[^\d]', '', x)))
    
    # Convert 'Stock Prices' column to floats
    df['Stock Prices'] = df['Stock Prices'].apply(lambda x: float(re.sub(r'[^\d.]+', '', x).rstrip('.')))
    
    # Convert 'Year' column to integers
    df['Year'] = df['Year'].astype(int)
    
    return df

df_aapl = convert_to_numeric(df_aapl)
df_goog = convert_to_numeric(df_goog)
df_meta = convert_to_numeric(df_meta)

# Create a Streamlit app
st.title('Employee Attrition and Stock Price Visualization')

# Dropdown to select company
selected_company = st.selectbox('Select Company', ['AAPL', 'GOOG', 'META'])

# Line chart based on selected company and data type
if selected_company == 'AAPL':
    df = df_aapl
    st.subheader('Attrition of Employees (K) vs Stock Prices ($)')
    df_copy = df.copy()  # Create a copy of the DataFrame to avoid modifying the original
    df_copy['Employees'] = df_copy['Employees'] / 1000  # Divide the column values by 1000 so that we can compare
    st.area_chart(data=df_copy, x='Year', y=['Employees', 'Stock Prices'], color=['#FF0000', '#0000FF'], width=0, height=0, use_container_width=True)
elif selected_company == 'GOOG':
    df = df_goog
    st.subheader('Attrition of Employees (K) vs Stock Prices ($)')
    df_copy = df.copy()  # Create a copy of the DataFrame to avoid modifying the original
    df_copy['Employees'] = df_copy['Employees'] / 1000  # Divide the column values by 1000 so that we can compare
    st.area_chart(data=df_copy, x='Year', y=['Employees', 'Stock Prices'], color=['#FF0000', '#0000FF'], width=0, height=0, use_container_width=True)
else:
    df = df_meta
    st.subheader('Attrition of Employees (K) vs Stock Prices ($)')
    df_copy = df.copy()  # Create a copy of the DataFrame to avoid modifying the original
    df_copy['Employees'] = df_copy['Employees'] / 1000  # Divide the column values by 1000 so that we can compare
    st.area_chart(data=df_copy, x='Year', y=['Employees', 'Stock Prices'], color=['#FF0000', '#0000FF'], width=0, height=0, use_container_width=True)

# Dropdown to select data type
data_type = st.radio('Select Data Type', ('Employees', 'Stock Prices'))

if data_type == 'Employees':
    st.subheader('Employees Over Time')
    st.line_chart(data=df, x='Year', y='Employees', color=None, width=0, height=0, use_container_width=True)

elif data_type == 'Stock Prices':
    st.subheader('Stock Prices Over Time')
    st.line_chart(data=df, x='Year', y='Stock Prices', color=None, width=0, height=0, use_container_width=True)