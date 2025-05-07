# pip install matplotlib and plotly in the terminal
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
# importing necessary libraries

pages = {
    "Page 1": "pages/page1.py",
    "Page 2": "pages/page2.py",
    "Page 3": "pages/page3.py",
    "Page 4": "pages/page4.py",
    "Page 5": "pages/page5.py",
    "Page 6": "pages/page6.py"
}
selected_page = st.sidebar.selectbox("Page selection", list(pages.keys()))
#exec(open(pages[selected_page]).read())

# title, header and caption of first dashboard
st.title("Changing housing affordability over the last 20 years")
st.subheader("House prices for selected regions")


# Loading the datasets
median_houseprice_region = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/1a_median_price_transposed.csv', index_col = 0)
median_residence_region = pd.read_csv('https://raw.githubusercontent.com/JDevs-py/new_5DATA004W_DSPL_Individual_Coursework/refs/heads/main/1b_median_residence_transposed.csv', index_col = 0)


df = median_houseprice_region # assigning loaded dataset as df 

df = df.reset_index() # resetting the index
df= df.rename(columns={df.columns[0]: 'year'}) # changing the index name
df_long = df.melt(id_vars='year', var_name='region', value_name='price') # Reshaping the dataframe

# creates list of unique regions
regions = df_long['region'].unique()

# to let user select or remove regions from region column
selected_regions = st.multiselect("Select a region:", list(regions), key="main_region_selection_1") 
# changed from , default=regions

# buttons that either display the chart as a line or bar chart
chart_type = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key='main_chart_type1')

# so that chart only appears if options are selected
if selected_regions:
    # filtering data to only include selected regions
    filtered = df_long[df_long['region'].isin(selected_regions)]
    
    if chart_type == 'Line Chart':
        # creates a line chart for selected regions
        fig = px.line(filtered, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        fig = px.bar(filtered, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line chart
    st.plotly_chart(fig)
else:
    st.write("Please select a region to view the data")

st.subheader("Residence income for selected regions")
# now loading and displaying data for residence earners
df2 = median_residence_region # assigning residence earnings to df2

df2 = df2.reset_index() # resetting the index
df2 = df2.rename(columns={df2.columns[0]:'year'}) # changing the index name

# reshaping dataframe similar to how previous dataframe was reshaped
df2_long = df2.melt(id_vars='year', var_name='region', value_name='price')

# creates a list of unique regions
regions2 = df2_long['region'].unique()

# lets user choose columns
selected_regions2 = st.multiselect("Select a region:", list(regions2), key="main_region_selection_2")

# user can change whether chart displayed is a line or bar chart
chart_type2 = st.radio("Chart type", ['Line Chart', 'Bar Chart'], key = 'main_chart_type2')

# so charts only appear after options are selected
if selected_regions2:
    # filtering data to only include selected regions
    filtered2 = df2_long[df2_long['region'].isin(selected_regions2)]
    
    if chart_type2 == 'Line Chart':
        # creates a line chart for selected regions
        fig2 = px.line(filtered2, x='year', y='price', color='region', markers=True, labels={'year': 'Year', 'price': 'House Price (£)', 'region': 'Region'})
    else:
        # creates a bar chart for selected regions
        fig2 = px.bar(filtered2, x='year', y='price', color='region', barmode='group', labels={'price': 'House Price (£)', 'year': 'Year'})

    # displays a line or bar chart depending on if condition satisfied
    st.plotly_chart(fig2)
else:
    # displays a message if the user has not chosen a column
    st.write("Please select a region to view the data")




