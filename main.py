import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image
from tokens.token_extract import token_extract
from nft.nft_extract import nft_home
from wallet.wallet_extract import wallet_extract



import time


st.set_page_config(
    page_title="NFT_Market Dash",
    layout="wide"
)


new_title = '<p style="font-family: Arial, Helvetica, sans-serif; text-align: center; color:#FFFFFF; font-size: 60px;">NFT_Market Dash</p>'
st.markdown(new_title, unsafe_allow_html=True)

with st.sidebar:
    option = st.radio(
        'Select sponsors',
        ('NFT_Markets','Token', 'wallet','Mint'))

     
st.header(option)


if option == 'NFT_Markets':
  nft_home()

elif option == 'Token' :
  token_extract()

elif option == 'Wallet' :
  wallet_extract()







