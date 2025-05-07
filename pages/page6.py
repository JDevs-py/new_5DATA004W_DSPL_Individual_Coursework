import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("South West of England")
st.subheader("Median house prices in South west districts")

southwest_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_southwest_median_houseprice_transposed.csv', index_col = 0)
southwest_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_southwest_median_residence_transposed.csv', index_col = 0)

df13 = southwest_price_district

df13 = df13.reset_index() # resetting the index
df13= df13.rename(columns={df13.columns[0]: 'year'}) # changing the index name
df13_long = df13.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions13 = df13_long['region'].unique()

# to let user select or remove regions from region column
selected_regions13 = st.multiselect("Select a region:", list(regions13), key='page6_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type13 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page6_chart_selection')

# so that chart only appears if options are selected
if selected_regions13:
    # filtering data to only include selected regions
    filtered13 = df13_long[df13_long['region'].isin(selected_regions13)]
    
    if chart_type13 == 'Line Chart':
        # creates a line chart for selected regions
        fig13 = px.line(filtered13, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig13 = px.bar(filtered13, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig13)
else:
    st.write("Please select a district to view the data")

st.subheader("Residence income for residence living in the districts of South west of England")
# now loading and displaying data for residence earners
df14 = southwest_residence_district # assigning residence earnings to df

df14 = df14.reset_index() # resetting the index
df14 = df14.rename(columns={df14.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df14_long = df14.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions14 = df14_long['region'].unique()

# lets user choose columns
selected_regions14 = st.multiselect("Select a region:", list(regions14), key="page6_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type14 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page6_second_type2')

# so charts only appear after options are selected
if selected_regions14:
    # filtering data to only include selected regions
    filtered14 = df14_long[df14_long['region'].isin(selected_regions14)]
    
    if chart_type14 == 'Line Chart':
        # creates a line chart for selected regions
        fig14 = px.line(filtered14, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig14 = px.bar(filtered14, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig14)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")


st.write("Page 6")