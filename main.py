import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image
from opensea.opensea_extract import opensea_extract
from nft.nft_extract import nft_home
from looksrare.looksrare_extract import looksrare_extract



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
        ('NFT','Opensea', 'looksrare','x2y2'))

     
st.header(option)


if option == 'NFT':
  nft_home()

elif option == 'Opensea' :
  opensea_extract()

elif option == 'looksrare' :
  looksrare_extract()







