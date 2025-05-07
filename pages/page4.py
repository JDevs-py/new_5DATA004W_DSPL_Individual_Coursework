import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("North West of England")
st.subheader("Median house prices of districts in North West of England")

northwest_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_northwest_median_houseprice_transposed.csv', index_col = 0)
northwest_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_northwest_median_residence_transposed.csv', index_col = 0)

df9 = northwest_price_district

df9 = df9.reset_index() # resetting the index
df9= df9.rename(columns={df9.columns[0]: 'year'}) # changing the index name
df9_long = df9.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions9 = df9_long['region'].unique()

# to let user select or remove regions from region column
selected_regions9 = st.multiselect("Select a region:", list(regions9), key='page4_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type9 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page4_chart_selection')

# so that chart only appears if options are selected
if selected_regions9:
    # filtering data to only include selected regions
    filtered9 = df9_long[df9_long['region'].isin(selected_regions9)]
    
    if chart_type9 == 'Line Chart':
        # creates a line chart for selected regions
        fig9 = px.line(filtered9, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig9 = px.bar(filtered9, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig9)
else:
    st.write("Please select a district to view the data")

st.subheader("Residence income for residence living in the districts of North West of England")
# now loading and displaying data for residence earners
df10 = northwest_residence_district # assigning residence earnings to df

df10 = df10.reset_index() # resetting the index
df10 = df10.rename(columns={df10.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df10_long = df10.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions10 = df10_long['region'].unique()

# lets user choose columns
selected_regions10 = st.multiselect("Select a region:", list(regions10), key="page4_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type10 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page4_second_type2')

# so charts only appear after options are selected
if selected_regions10:
    # filtering data to only include selected regions
    filtered10 = df10_long[df10_long['region'].isin(selected_regions10)]
    
    if chart_type10 == 'Line Chart':
        # creates a line chart for selected regions
        fig10 = px.line(filtered10, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig10 = px.bar(filtered10, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig10)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")

st.write("Page 4")