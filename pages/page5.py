import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("South East of England")
st.subheader("Median house prices of districts in South East of England")

southeast_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_southeast_median_houseprice_transposed.csv', index_col = 0)
southeast_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_southeast_median_residence_transposed.csv', index_col = 0)

df11 = southeast_price_district

df11 = df11.reset_index() # resetting the index
df11= df11.rename(columns={df11.columns[0]: 'year'}) # changing the index name
df11_long = df11.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions11 = df11_long['region'].unique()

# to let user select or remove regions from region column
selected_regions11 = st.multiselect("Select a region:", list(regions11), key='page5_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type11 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page5_chart_selection')

# so that chart only appears if options are selected
if selected_regions11:
    # filtering data to only include selected regions
    filtered11 = df11_long[df11_long['region'].isin(selected_regions11)]
    
    if chart_type11 == 'Line Chart':
        # creates a line chart for selected regions
        fig11 = px.line(filtered11, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig11 = px.bar(filtered11, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig11)
else:
    st.write("Please select a district to view the data")

st.subheader("Residence income for residence living in the districts of South East of England")
# now loading and displaying data for residence earners
df12 = southeast_residence_district # assigning residence earnings to df

df12 = df12.reset_index() # resetting the index
df12 = df12.rename(columns={df12.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df12_long = df12.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions12 = df12_long['region'].unique()

# lets user choose columns
selected_regions12 = st.multiselect("Select a region:", list(regions12), key="page5_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type12 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page5_second_type2')

# so charts only appear after options are selected
if selected_regions12:
    # filtering data to only include selected regions
    filtered12 = df12_long[df12_long['region'].isin(selected_regions12)]
    
    if chart_type12 == 'Line Chart':
        # creates a line chart for selected regions
        fig12 = px.line(filtered12, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig12 = px.bar(filtered12, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig12)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")

st.write("Page 5")