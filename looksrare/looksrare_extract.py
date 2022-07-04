import streamlit as st
import plost
import datetime
from metrics import getdata
import pandas as pd
from pathlib import Path
import sqlite3
from sqlite3 import Connection
from common.connect import *


def looksrare_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">dYdX (DYDX) is a decentralized exchange platform for cryptocurrency margin trading for assets like BTC, ETH, SOL, DOT, and more. The bulk of dYdX crypto margin trading products reside atop the Ethereum blockchain. However, the exchange recently rolled out on Layer 2 for instantly settled, inexpensive trades..</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('LooksRare Stats')

    st.markdown('#') 

    


    