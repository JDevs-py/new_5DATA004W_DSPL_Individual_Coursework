import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("London")
st.subheader("Median house prices in London districts")

# Loading the datasets
ldn_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_ldn_median_houseprice_transposed.csv', index_col = 0)
ldn_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_ldn_median_residence_transposed.csv', index_col = 0)

df5 = ldn_price_district

df5 = df5.reset_index() # resetting the index
df5= df5.rename(columns={df5.columns[0]: 'year'}) # changing the index name
df5_long = df5.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions5 = df5_long['region'].unique()

# to let user select or remove regions from region column
selected_regions5 = st.multiselect("Select a region:", list(regions5), key='page2_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type5 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page2_chart_selection')

# so that chart only appears if options are selected
if selected_regions5:
    # filtering data to only include selected regions
    filtered5 = df5_long[df5_long['region'].isin(selected_regions5)]
    
    if chart_type5 == 'Line Chart':
        # creates a line chart for selected regions
        fig5 = px.line(filtered5, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig5 = px.bar(filtered5, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig5)
else:
    st.write("Please select a region to view the data")

st.subheader("Residence income for residence living in the districts of London")
# now loading and displaying data for residence earners
df6 = ldn_residence_district # assigning residence earnings to df

df6 = df6.reset_index() # resetting the index
df6 = df6.rename(columns={df6.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df6_long = df6.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions6 = df6_long['region'].unique()

# lets user choose columns
selected_regions6 = st.multiselect("Select a region:", list(regions6), key="page2_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type6 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page2_second_type2')

# so charts only appear after options are selected
if selected_regions6:
    # filtering data to only include selected regions
    filtered6 = df6_long[df6_long['region'].isin(selected_regions6)]
    
    if chart_type6 == 'Line Chart':
        # creates a line chart for selected regions
        fig6 = px.line(filtered6, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig6 = px.bar(filtered6, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig6)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")





st.write("Page 2")