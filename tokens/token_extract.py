from common_data import nft_token, nft_trans
import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image

from common.connect import *



def token_extract():
    with st.form("form1", clear_on_submit=True): 
        values = ['ethereum', 'polygon']
        window_ANTICOR = st.selectbox('Blockchain_ID', values)
        title = st.text_input('Contract_address')
        token_add = st.text_input('Token_ID')

        submit = st.form_submit_button("Submit")

    if submit:
        st.title("Token Portfolio")
        nft_details = nft_token(window_ANTICOR,title,token_add)
       
        col1, col2 = st.columns((2,2))

        with col1:
            st.subheader("Contract Metadata")
            st.write(nft_details['contract'])
            st.markdown("#")
            st.subheader("NFT Metadata")
            st.write(nft_details['nft'])
        with col2:
            st.subheader("Marketplace")
            st.image('https://www.freelogovectors.net/wp-content/uploads/2022/01/opensea-logo-freelogovectors.net_.png', width=400)
            st.markdown("***")
            st.markdown("#")
            st.markdown("#")
            st.markdown("#")
            st.markdown("#")
            st.markdown("#")
            st.markdown("#")
            st.markdown("#")
            st.subheader("NFT")
            st.image(nft_details['nft']['cached_file_url'], width=400)
        st.markdown("#")
        st.subheader("NFT Sales Transactions")
        nft_tran = nft_trans(window_ANTICOR,title,token_add)
        st.dataframe(nft_tran)



    

   
