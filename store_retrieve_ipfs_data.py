import sqlite3
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
    


def store_nft_image(image):
    
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
