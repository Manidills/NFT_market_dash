from streamlit_option_menu import option_menu
from mint.mint_extract import mint_extract
from store_retrieve_ipfs_data import store_table_data
import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image
from tokens.token_extract import token_extract
from nft.nft_extract import nft_home
from wallet.wallet_extract import wallet_extract
from Opensea_poap import Opensea_poap
from collection_details.collection_extract import collection_extract
from mint.mint import mint
import time


st.set_page_config(
    page_title="NFT Console",
    layout="wide"
)

new_title = '<p style="font-family: Tangerine; text-align: center; color:white; font-size: 70px;">NFT Console</p>'
st.markdown(new_title, unsafe_allow_html=True)



option = option_menu("NFT Market Portfolio", ['NFT_Markets','POAP','Collections','Token', 'Wallet','Summary', 'Mint'], 
    icons=['house'], menu_icon="cast", default_index=0,  orientation="horizontal")
     
#store_table_data('db/POAP/POAP.db')

if option == 'NFT_Markets':
  nft_home()

elif option == 'POAP':
  store_table_data('db/POAP/POAP.db')
  Opensea_poap()

elif option == 'Collections':
  collection_extract()

elif option == 'Token':
  token_extract()

elif option == 'Wallet':
  wallet_extract()

elif option == 'Summary':
  mint_extract()

elif option == 'Mint':
  mint()








