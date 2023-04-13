import pandas as pd
import psycopg2
import os
from environs import Env

env = Env()
# Load environment variables from .env file
env.read_env()

# Define the connection parameters
conn_params = {
    "host": env.str("host"),
    "database": env.str("database"),
    "user": env.str("user"),
    "password": env.str("password"),
}

#connect and fetch products table
def connect_to_pdts():
    ''' this function connects to the table and fetches 
    the latest avalable info from the table products'''
    # Connect to the database
    conn = psycopg2.connect(**conn_params)

    # Define your SQL query
    sql_query = "SELECT * FROM products"

    # Load data into a pandas DataFrame
    df = pd.read_sql(sql_query, conn)

    # Close the database connection
    conn.close()
    return df 

# connect, update and fetch table
def update_pdts(product_name,price,expiry_date,num_of_items,num_items):
    ''' this function updates the products table with new product information 
    added into the fridge'''
    # Connect to the database
    conn = psycopg2.connect(**conn_params)
    # create a cursor object
    cur = conn.cursor()
    # define the SQL statement to insert data into the products table
    sql = "INSERT INTO products (product, price, expiry_date, create_date, number_of_items) VALUES (%s, %s, %s, NOW(), %s)"

    # create a list of tuples containing the values to insert into the products table
    values_list = [(product_name[i], price[i], expiry_date[i], num_of_items[i]) for i in range(num_items)]

    # execute the SQL statement to insert data into the products table
    cur.executemany(sql, values_list)


    # values_list = [product_name,price,expiry_date,num_of_items]

    # # iterate over the list and execute the SQL query for each set of values
    # for values in values_list:
    #     cur = conn.cursor()
    #     cur.execute("INSERT INTO products (product, price, expiry_date, create_date, number_of_items) VALUES (%s, %s, %s, NOW(), %s)", values)

# commit the changes to the database
    conn.commit()
    conn.close()
    return 'Success'

def delete_products_by_slno(slno_list):
    # Open a connection to the database
    conn = psycopg2.connect(**conn_params)
    # Create a cursor object
    cur = conn.cursor()
    
    # Delete rows based on the slno column
    for slno in slno_list:
        cur.execute("DELETE FROM products WHERE slno = %s", (slno,))
    
    # Commit the changes to the database
    conn.commit()
    
    # Close the cursor and connection
    cur.close()
    conn.close()

    
def color_df(val):
    if val < pd.Timestamp.today().date():
        color  = 'red'
    else :
        color = 'lightgreen'
    return f'background-color: {color}'
