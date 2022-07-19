import sqlite3
import time
import nft_storage
from nft_storage.api import nft_storage_api
from nft_storage.model.error_response import ErrorResponse
from nft_storage.model.upload_response import UploadResponse
from nft_storage.model.unauthorized_error_response import UnauthorizedErrorResponse
from nft_storage.model.forbidden_error_response import ForbiddenErrorResponse
from pprint import pprint
import pandas as pd
import streamlit as st
import requests
import ipfsApi

def create_table(hash_v,name):
    connection_obj = sqlite3.connect('ipfs.db')
 
# cursor object
    cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS ipfs")
    
    # Creating table
    table = """ CREATE TABLE ipfs (
                Hash VARCHAR(255) ,
                Name STRING(255) 
            ); """
    
    cursor_obj.execute(table)
    cursor_obj.execute("INSERT INTO ipfs values(?, ?)", (str(hash_v), str(name)))
    
    print("Data Inserted in the table: ")
    data=cursor_obj.execute('''SELECT * FROM ipfs''')
    for row in data:
        print(row)
    
    # Commit your changes in the database    
    connection_obj.commit()
    
    # Closing the connection
    connection_obj.close()

def store_table_data(link):
    api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
    new_file = api.add(link)
    name = 'POAP'
    hash_v = new_file[0]['Hash']
    create_table(hash_v,name)

def retrieve_table_data(link):
    data = sqlite3.connect('ipfs.db')
    query = f"SELECT Hash from ipfs where Name = '{link}'"
    df = pd.read_sql(query, con=data)
    val = df['Hash'][0]
    response = requests.request("GET", f'https://ipfs.infura.io/ipfs/{val}')
    with open("db/POAP/POAP.db", "wb") as f:
        f.write(response.content)
    


def store_nft_image_ipfs(image):
    
    file = open(image, "rb")
    #Store on IPFS
    response = requests.post(
        "https://api.nftport.xyz/v0/files",
        headers={"Authorization": 'f6ce3372-a928-4947-8f50-87649f60cee2'},
        files={"file": file}
    )

    return response.json()

def get_ipfs_image(ipfs_link):
    st.image(ipfs_link,width = 500)

def nft_storage_store(file):
    # Defining the host is optional and defaults to https://api.nft.storage
    # See configuration.py for a list of all supported configuration parameters.
    configuration = nft_storage.Configuration(
        host = "https://api.nft.storage"
    )

    configuration = nft_storage.Configuration(
    access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDE0RkY4NTU4MzVGMDYwZDBCRTk0ZWQyOTBjNTdiODE1YTE5MjQxNUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1NzU2OTU4ODQxOSwibmFtZSI6Ik1BTklESUxMUyJ9.idaK-qJVyOb8WKP1cD0yddE8UJX4zRpBKtX-QqN49fU'
)
    with nft_storage.ApiClient(configuration) as api_client:
    # Create an instance of the API class
        api_instance = nft_storage_api.NFTStorageAPI(api_client)
        body = open(file, 'rb') # file_type | 

        # example passing only required values which don't have defaults set
        try:
            # Store a file
            api_response = api_instance.store(body, _check_return_type=False)
            return(api_response)
        except nft_storage.ApiException as e:
            st.info("Exception when calling NFTStorageAPI->store: %s\n" % e)

def get_nft_storage(cid_):
    configuration = nft_storage.Configuration(
    host = "https://api.nft.storage"
)
    configuration = nft_storage.Configuration(
        access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDE0RkY4NTU4MzVGMDYwZDBCRTk0ZWQyOTBjNTdiODE1YTE5MjQxNUQiLCJpc3MiOiJuZnQtc3RvcmFnZSIsImlhdCI6MTY1NzU2OTU4ODQxOSwibmFtZSI6Ik1BTklESUxMUyJ9.idaK-qJVyOb8WKP1cD0yddE8UJX4zRpBKtX-QqN49fU'
    )


    with nft_storage.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = nft_storage_api.NFTStorageAPI(api_client)
        cid = cid_ # str | CID for the NFT

        # example passing only required values which don't have defaults set
        try:
            # Get information for the stored file CID
            api_response = api_instance.status(cid,_check_return_type=False)
            return(api_response)
        except nft_storage.ApiException as e:
            print("Exception when calling NFTStorageAPI->status: %s\n" % e)