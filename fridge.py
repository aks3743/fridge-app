import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from  support.connect_to_db import connect_to_pdts
from support.connect_to_db import update_pdts, delete_products_by_slno

tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Update items", "Expired",'Delete Data'])

with tab1:
    st.title("🍱:blue[My fridge Summary] 🧊")


    df = connect_to_pdts()
    df['cost'] = df['price']*df['number_of_items']

    # Define KPI values


    item_count = df['number_of_items'].sum()
    kpi2 = df[df['expiry_date'] == pd.Timestamp.today().date()]['number_of_items'].sum()
    kpi3 = df[(df['expiry_date'] > pd.Timestamp.today().date()) & (df['expiry_date'] <= pd.Timestamp.today().date() + pd.Timedelta(days=7))]['number_of_items'].sum()
    kpi4 = df['cost'].sum()
    # Create a layout with three columns
    col1, col2, col3,col4 = st.columns(4)

    # Display KPI values in separate containers
    with col1:
        st.metric(label="#Items", value=item_count)

    with col2:
        st.metric(label="#Expiring today", value=kpi2)

    with col3:
        st.metric(label="Expiring in a week", value=kpi3)
    with col4:
        st.metric(label="Money in fridge £", value=kpi4)
    

    # Visualization 1: Bar chart of number of items by product
    st.write("## Number of Items by Product")
    fig1 = px.bar(df, x='product', y='number_of_items', color='product', height=400)
    st.plotly_chart(fig1)

    # Visualization 3: Pie chart of products by expiry date
    labels = df['product']
    values = df['number_of_items']
    st.write("## Products by Expiry Date")
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3,textinfo= 'label+percent')])
    st.plotly_chart(fig3)

    # Visualization 2: Line chart of prices by product
    st.write("## Prices by Product")
    fig2 = px.bar(df, x='expiry_date', y='price', color='product', height=400)
    st.plotly_chart(fig2)
    #tabular view
    st.table(df[['product','price','expiry_date','number_of_items','cost']])


with tab2:
    st.title(':green[Add new items to inventory] 🆕 🍇🍷🌿🍅🍓🐟🍗')
    product_name,price,expiry_date,num_of_items = [],[],[],[]
    num_items = st.number_input("Number of items to add", min_value=1, step=1, key="num_items")
    for i in range(num_items):
        product_name.append( st.text_input(f"Product {i+1} name", key=f"product_name_{i}"))
        price.append( float(st.number_input(f"Price for {product_name[i]}", key=f"price_{i}")))
        expiry_date.append(st.date_input(f"Expiry date for {product_name[i]}", key=f"expiry_date_{i}"))
        num_of_items.append(st.number_input(f"Number of items for {product_name[i]}", min_value=1, step=1, key=f"num_of_items_{i}"))

    values_list = [product_name,price,expiry_date,num_of_items]
    sb = st.button(label = 'Submit new items',on_click=update_pdts,args=[product_name,price,expiry_date,num_of_items,num_items])
    if sb:
        # st.experimental_rerun()
        st.success('Data has been updated')

    # st.write(values_list)


    with tab3:
        st.title('🚫 :red[Summary of Expired items] 💀 ')
        df2 =  df[df['expiry_date'] <= pd.Timestamp.today().date()]
        # st.table(df2)
        item_counte = df2['number_of_items'].sum()
        kpi5 = df2[df2['expiry_date'] == pd.Timestamp.today().date()- pd.Timedelta(days=7)]['number_of_items'].sum()
        kpi6 = df2[(df2['expiry_date'] < pd.Timestamp.today().date()) & (df['expiry_date'] <= pd.Timestamp.today().date() - pd.Timedelta(days=7))]['number_of_items'].sum()
        kpi7 = df2['cost'].sum()
        # Create a layout with three columns
        col1, col2, col3,col4 = st.columns(4)

        # Display KPI values in separate containers
        with col1:
            st.metric(label="#Items", value=item_counte)

        with col2:
            st.metric(label="#Expired yesterday", value=kpi5)

        with col3:
            st.metric(label="Expired last week", value=kpi6)
        with col4:
            st.metric(label="Money lost in fridge £", value=kpi7)
        st.table(df2[['product','price','expiry_date','number_of_items','cost']])


        # Visualization 2: Line chart of prices by product
        st.write("## Prices by Product")
        fig = px.line(df2, x='expiry_date', y='price', color='product', height=400)
        st.plotly_chart(fig)


with tab4:
    st.title('🚨 Remove unwanted data 🚨')
    st.table(df[['slno','product','price','expiry_date']])
    # with st.sidebar:
    selected_rows = st.multiselect("Select slno from table to delete", df["slno"])
    st.write(selected_rows)
    # When the delete button is pressed, call the delete_products_by_slno function
    st.warning(':fire: you are about to delete data, proceed with caution ',icon="⚠️")
    if st.button("Delete"):
        delete_products_by_slno(selected_rows)
        st.experimental_rerun()
        st.success("Selected rows deleted!")