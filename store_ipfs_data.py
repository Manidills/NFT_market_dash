import sqlite3
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
                Name VARCHAR(255) 
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

def store__data(link):
    api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
    new_file = api.add(link)
    name = new_file[0]['Name']
    hash_v = new_file[0]['Hash']
    create_table(hash_v,name)
    
