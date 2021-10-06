import numpy as np
import pandas as pd
import os

# Used to obtain information from websites
import requests

# Website that we are getting data from:
# https://python.zgulde.net/api/v1/items



def get_items(cached=False):
    '''
    This function creates a request from the REST API and transforms the response into a pandas dataframe.
    Then it saves the dataframe as a local csv file.
    '''
    # If the cached parameter is false, or it there is no local csv file, then create a new dataframe from the database
    if cached == False or os.path.isfile('items.csv') == False:
        
        # Create an empty list that will be appended at each iteration
        items_list = []

        # Define the url where the data is kept
        base_url = "https://python.zgulde.net/api/v1/items"

        # Define the response from the request
        response = requests.get(base_url)

        # Convert the response to JSON
        data = response.json()

        # Define the number of pages
        n = data['payload']['max_pages']

        # Create a loop to iterate through each page
        for i in range(1, n+1):

            # Define the new url for the next page
            new_url = base_url+"?page="+str(i)

            # Define the response
            response = requests.get(new_url)

            # Convert the response to json
            data = response.json()

            # Create variable to current interations
            page_items = data['payload']['items']

            # Create variable to hold all iterations
            items_list += page_items

        # Create dataframe to hold items
        items = pd.DataFrame(items_list)

        # Save to csv
        items.to_csv('items.csv')

    else:
        # Get the data from local csv
        items = pd.read_csv('items.csv', index_col=0)




def get_stores(cached==False):
    if cached == False or os.path.isfil('stores.csv') == False:
        stores_list = []
        base_url = 'https://python.zach.lol/api/v1/stores'
        response = requests.get(base_url)
        data = response.json()
        n = data['payload']['max_pages']

        for i in range(1, n+1):
            new_url = base_url + '?page=' + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_stores = data['payload']['stores']
            stores_list += page_stores

        stores = pd.DataFrame(stores_list)
        stores.to_csv('stores.csv')

    else:
        stores = pd.read_csv('stores.csv', index_col=0)
    
    return stores



def get_sales(cached=False):
    # If cached is false or there is no local csv, then read from database
    if cached == False or os.path.isfile('sales.csv') == False:
        sales_list = []
        url = 'https://python.zach.lol/api/v1/sales'
        response = requests.get(url)
        data = response.json()
        n = data['payload']['page']

        for i in range(1, n+1):
            new_url = url + "?page=" + str(i)
            response = requests.get(new_url)
            data = response.json()
            page_sales = data['payload']['sales']
            sales_list += page_sales

        sales = pd.DataFrame(sales_list)
        sales.to_csv('sales.csv')

    else:
        sales = pd.read_csv('sales.csv', index_col = 0)

    return sales



def combine_df(cached=False):
    if cached == False
        # Get the data
        sales = get_sales(cached=True)
        stores = get_stores(cached=True)
        items = get_items(cached=True)

        # In sales, rename store to store_id and item to item_id
        sales.columns = ['item_id', 'sale_amount', 'sale_date', 'sale_id', 'store_id']

        # Join sales and stores
        sales_stores = pd.merge(sales, stores, how='inner', on='store_id')

        # Join items to sales_stores
        sales_stores_items = pd.merge(sales_stores, items, how='inner', on='item_id')

        # Save as local csv
        sales_stores_items.to_csv('sales_stores_items')

    else:
        # Read the file locally
        sales_stores_items = pd.read_csv('sales_stores_items.csv', index_col=0)
    
    return sales_stores_items



def get_power_data():
    base_url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
    power_df = pd.read_csv(base_url)
    return power_df







