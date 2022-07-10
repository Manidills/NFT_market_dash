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
            try:st.write(nft_details['contract'])
            except:pass
            st.markdown("#")
            st.subheader("NFT Metadata")
            try:st.write(nft_details['nft'])
            except:pass
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
            try:st.image(nft_details['nft']['cached_file_url'], width = 400)
            except:pass
        st.markdown("#")
        st.subheader("NFT Sales Transactions")
        nft_tran = nft_trans(window_ANTICOR,title,token_add)
        est_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).mean()
        sum_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).sum()
        min_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).min()
        max_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).max()
        median_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).median()
        #mode_value = nft_tran['price_details'].apply(lambda x: x["price_usd"]).mode()
        st.success(f"Estimated Value To Buy This NFT :${est_value}")
        st.write(f"Total_Sum: ${sum_value}")
        st.write(f"Min_value: ${min_value}")
        st.write(f"Max_value: ${max_value}")
        st.write(f"Median_value: ${median_value}")
        st.markdown("#")
        # st.subheader("Token Transactions")
        try:st.dataframe(nft_tran)
        except:pass

        



    

   
