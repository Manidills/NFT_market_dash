import streamlit as st
import plost
import datetime
from metrics import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def nft_home():
    st.markdown('#')

    Defi_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">Non-fungible tokens (NFTs) give you ownership of artwork, music, videos and other online collectibles. They exist on blockchains, the innovative technology that underlies cryptocurrencies like Bitcoin..</p>'
    st.markdown(Defi_title, unsafe_allow_html=True)

    st.markdown('#')

    st.header("What Is a NFT Marketplace")

    top_trend = '<p style="font-family:Courier; color:blue; font-size: 20px;">An NFT marketplace is a digital platform for buying and selling NFTs. These platforms allow people to store and display their NFTs plus sell them to others for cryptocurrency or money. Some NFT marketplaces also allow users to mint their NFTs on the platform itself.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('How Do NFT Marketplaces Work')

    top_trend = '<p style="font-family:Courier; color:white; font-size: 25px;">When you create an account with an NFT marketplace, you can browse through all their available options for sale. You can also add a payment method, and some require you to link a crypto wallet to pay with crypto, while others allow you to use a credit card.Some sites let you buy NFTs directly for a fixed price, while others will use an auction.If you complete the transaction, the NFT marketplace will record it on its blockchain showing the change of ownership.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)


    #data = connect('db/defi.db')

    





    