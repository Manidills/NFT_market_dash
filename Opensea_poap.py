import requests
import plost
import ipfsApi
import datetime
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *
from store_retrieve_ipfs_data import retrieve_table_data
import streamlit as st



def Opensea_poap():
    

    Defi_title = '<p style="font-family:Courier; color:green; font-size: 20px;">POAP is a new way of keeping a reliable record of life experiences.Each time they take part on an event, POAP collectors get a unique badge that is supported by a cryptographic record.These badges are Non Fungible Tokens (NFT) and open a whole new world of possibilities..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')
    
    retrieve_table_data('POAP')

    data = connect('db/POAP/POAP.db')
    st.markdown('#')

    col1, col2 = st.columns((2,2))

    with col1:
        line_chart(data, 'POAP_Wallet_Counts_Mainnet', 'mindate', 'walletcount', 'POAP_Wallet_Counts_Mainnet')
        line_chart(data, 'POAP_Monthly_Mints_Mainnet', 'date_trunc', 'mints', 'POAP_Monthly_Mints_Mainnet')
        st.dataframe(table(data, 'POAP_Leaderboard_Mainnet'))
    with col2:
        line_chart(data, 'POAP_Wallets_Over_Time_XDAI', 'day', 'walletcount', 'POAP_Wallets_Over_Time_XDAI')
        line_chart(data, 'POAP_Monthly_Mints_XDAI', 'date_trunc', 'mints', 'POAP_Monthly_Mints_XDAI')
        st.dataframe(table(data, 'POAP_Leaderboard_XDAI'))

    st.markdown('#')
    st.subheader('POAPs on OpenSea (2020(APR) - 2021(NOV))')

    line_chart(data, 'Opensea_poap_daily_stats', 'date', 'total_usd', 'Opensea_poap_total_usd')

    line_chart(data, 'Opensea_poap_daily_stats', 'date', 'num_trades', 'Opensea_poap_num_trades')

    line_chart(data, 'Opensea_poap_daily_stats', 'date', 'num_unique_buyers', 'Opensea_poap_num_unique_buyers')

    line_chart(data, 'Opensea_poap_daily_stats', 'date', 'num_unique_sellers', 'Opensea_poap_num_unique_sellers')

    st.markdown('#')
    col1, col2 = st.columns((2,2))

    with col1:
        st.subheader('Opensea_poap_top_buyers')
        st.dataframe(table(data, 'Opensea_poap_top_buyers'))
        st.subheader('Opensea_poap_top_events')
        st.dataframe(table(data, 'Opensea_poap_top_events'))
    with col2:
        st.subheader('Opensea_poap_top_sellers')
        st.dataframe(table(data, 'Opensea_poap_top_sellers'))
        st.subheader('Opensea_poap_most_traded')
        st.dataframe(table(data, 'Opensea_poap_most_traded'))
    
    st.markdown('#')
    bar_chart(data, 'Opensea_poap_distribution_of_secondary_sale', 'sale_value_bucket', 'num_sales_within_range', 'Opensea_poap_distribution_of_secondary_sale')
    st.markdown('#')
    st.subheader('Opensea_poap_daily_stats')
    st.dataframe(table(data,'Opensea_poap_daily_stats'))
    
    

    