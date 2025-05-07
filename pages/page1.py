import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("East Midlands")
st.subheader("Median house prices for districts in East Midlands region")

# Loading the datasets
eastmid_price_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5a_eastmid_median_houseprice_transposed.csv', index_col = 0)
eastmid_residence_district = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/5b_eastmid_median_residence_transposed.csv', index_col = 0)

df3 = eastmid_price_district

df3 = df3.reset_index() # resetting the index
df3= df3.rename(columns={df3.columns[0]: 'year'}) # changing the index name
df3_long = df3.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions3 = df3_long['region'].unique()

# to let user select or remove regions from region column
selected_regions3 = st.multiselect("Select a region:", list(regions3), key='page1_multi_selection') 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type3 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='page1_chart_selection')

# so that chart only appears if options are selected
if selected_regions3:
    # filtering data to only include selected regions
    filtered3 = df3_long[df3_long['region'].isin(selected_regions3)]
    
    if chart_type3 == 'Line Chart':
        # creates a line chart for selected regions
        fig3 = px.line(filtered3, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig3 = px.bar(filtered3, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig3)
else:
    st.write("Please select a district to view the data")

st.subheader("Residence income for residence living in the districts of the East Midlands region")
# now loading and displaying data for residence earners
df4 = eastmid_residence_district # assigning residence earnings to df2

df4 = df4.reset_index() # resetting the index
df4 = df4.rename(columns={df4.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df4_long = df4.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions4 = df4_long['region'].unique()

# lets user choose columns
selected_regions4 = st.multiselect("Select a region:", list(regions4), key="page1_second_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type4 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'page1_second_type2')

# so charts only appear after options are selected
if selected_regions4:
    # filtering data to only include selected regions
    filtered4 = df4_long[df4_long['region'].isin(selected_regions4)]
    
    if chart_type4 == 'Line Chart':
        # creates a line chart for selected regions
        fig4 = px.line(filtered4, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig4 = px.bar(filtered4, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig4)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a district to view the data")


st.write("Page 1")