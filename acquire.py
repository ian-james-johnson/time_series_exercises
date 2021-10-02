import numpy as np
import pandas as pd
import os

# Used to obtain information from websites
import requests

# Website that we are getting data from:
# https://python.zgulde.net/api/v1/items


#1
# Using the code from the lesson as a guide and the REST API from https://python.zgulde.net/api/v1/items as we did in the lesson, 
# create a dataframe named items that has all of the data for items.

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


while endpoint:
    # get the response
    response = request.get(base_url + endpoint).json()['payload']
    # iterates our endpoint through the loop
    endpoint = response['next_page']
    # get the data and add it to pages
    pages += response['sales']

