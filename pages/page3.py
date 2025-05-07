import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("North East of England")
st.subheader("Median house prices of districts in North East of England")

# Loading the datasets
northeast_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_northeast_median_houseprice_transposed.csv', index_col = 0)
northeast_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_northeast_median_residence_transposed.csv', index_col = 0)

df7 = northeast_price_district

df7 = df7.reset_index() # resetting the index
df7= df7.rename(columns={df7.columns[0]: 'year'}) # changing the index name
df7_long = df7.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions7 = df7_long['region'].unique()

# to let user select or remove regions from region column
selected_regions7 = st.multiselect("Select a region:", list(regions7), key='page3_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type7 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page3_chart_selection')

# so that chart only appears if options are selected
if selected_regions7:
    # filtering data to only include selected regions
    filtered7 = df7_long[df7_long['region'].isin(selected_regions7)]
    
    if chart_type7 == 'Line Chart':
        # creates a line chart for selected regions
        fig7 = px.line(filtered7, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig7 = px.bar(filtered7, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig7)
else:
    st.write("Please select a district to view the data")

st.subheader("Residence income for people living in the districts of North East of England")
# now loading and displaying data for residence earners
df8 = northeast_residence_district # assigning residence earnings to df

df8 = df8.reset_index() # resetting the index
df8 = df8.rename(columns={df8.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df8_long = df8.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions8 = df8_long['region'].unique()

# lets user choose columns
selected_regions8 = st.multiselect("Select a region:", list(regions8), key="page3_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type8 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page3_second_type2')

# so charts only appear after options are selected
if selected_regions8:
    # filtering data to only include selected regions
    filtered8 = df8_long[df8_long['region'].isin(selected_regions8)]
    
    if chart_type8 == 'Line Chart':
        # creates a line chart for selected regions
        fig8 = px.line(filtered8, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig8 = px.bar(filtered8, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig8)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")



st.write("Page 3")