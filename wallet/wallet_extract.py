
from common_data import balance, historical_portfolio, nft_token, nft_trans, wallet_contract_owned, wallet_nft_created, wallet_nft_owned
import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image

from common.connect import *



def wallet_extract():
    with st.form("form2", clear_on_submit=True): 
        values = ['ethereum', 'polygon']
        window_ANTICOR = st.selectbox('Blockchain_ID', values)
        wallet_add = st.text_input('Wallet_Address')

        submit = st.form_submit_button("Submit")
    
    if submit:
        st.subheader("NFT's Created By The Wallet")
        nft_c = wallet_nft_created(window_ANTICOR, wallet_add)
        st.write(list(nft_c['nfts'])[:10])
        st.markdown("#")
        st.subheader("Contract's owned by Wallet")
        nft_con = wallet_contract_owned(window_ANTICOR, wallet_add)
        st.markdown("#")
        st.write(nft_con)
        st.markdown("#")
        st.subheader("Token's Balance")
        st.dataframe(balance(wallet_add))
        st.markdown("#")
        st.subheader("Historical Portfolio Value Over Time")
        st.dataframe(historical_portfolio(wallet_add))
        st.markdown("#")
        st.subheader("NFT's owned by Wallet")
        nft_o = wallet_nft_owned(window_ANTICOR, wallet_add)
        st.write(list(nft_o)[:10])
        try:
            st.subheader("Top 5 NFT's")
            col1, col2 = st.columns((2,2))

            cached_files = [i['cached_file_url'] for i in list(nft_o)]
            cached_files = [x for x in cached_files if x is not None][:5]
            meta = [i['metadata'] for i in list(nft_o)]
            meta = [x for x in meta if x is not None][:5]
        
            try:
                for i,j in zip(cached_files,meta):
                    with col1:
                        st.image(i, width = 300)
                    with col2:
                        #st.markdown("#")
                        st.write(j, width =300)
            except:
                pass
        except:
            st.subheader("NFT's owned by Wallet")
            st.write(list(nft_o)[:10])


