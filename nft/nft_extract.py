import requests
import streamlit as st
import plost
import datetime
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *



def nft_home():
    

    Defi_title = '<p style="font-family:Courier; color:green; font-size: 20px;">Non-fungible tokens (NFTs) give you ownership of artwork, music, videos and other online collectibles. They exist on blockchains, the innovative technology that underlies cryptocurrencies like Bitcoin..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header("What Is a NFT Marketplace")

    top_trend = '<p style="font-family:Courier; color:white; font-size: 20px;">An NFT marketplace is a digital platform for buying and selling NFTs. These platforms allow people to store and display their NFTs plus sell them to others for cryptocurrency or money. Some NFT marketplaces also allow users to mint their NFTs on the platform itself.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    
    # response = requests.request("GET", 'https://ipfs.infura.io/ipfs/QmUtodXmwzG7apQAw6qJQjwZ1ozX5ZXJSCgy8MXcLCp5AV')
    # with open("db/NFT_Market/NFT_Markets_Volume.db", "wb") as f:
    #     f.write(response.content)

    data = connect('db/NFT_Market/NFT_Markets_Volume.db')
    st.markdown('#')
    line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'global_volume', 'Global_Volume')
    st.markdown('#')
    st.subheader("OPENSEA Marketplace")

    line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'os_volume', 'Opensea_Volume')
    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'os_vol_tx', 'Opensea_Volume_Txs')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'os_txs', 'Opensea_Txs')
    with col2:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'os_vol_user', 'Opensea_Volume_Users')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'os_users', 'Opensea_Users')
    
    st.markdown('#')
    st.subheader("LOOKSRARE Marketplace")

    line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'lr_volume', 'Looksrare_Volume')
    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'lr_vol_tx', 'Looksrare_Volume_Txs')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'lr_txs', 'Looksrare_Txs')
    with col2:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'lr_vol_user', 'Looksrare_Volume_Users')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'lr_users', 'Looksrare_Users')
    
    st.markdown('#')
    st.subheader("X2Y2 Marketplace")

    line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'x2y2_volume', 'X2Y2_Volume')
    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'x2y2_vol_tx', 'X2Y2_Volume_Txs')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'x2y2_txs', 'X2Y2_Txs')
    with col2:
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'x2y2_vol_user', 'X2Y2_Volume_Users')
        line_chart(data, 'NFT_Markets_Volume', 'time_unit', 'x2y2_users', 'X2Y2_Users')

    





    