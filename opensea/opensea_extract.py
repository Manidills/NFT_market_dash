import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image

from common.connect import *



def opensea_extract():
    st.markdown('#') 
    top_trend = '<p style="font-family:Courier; color:violet; font-size: 25px;">Polygon is a cutting-edge platform. It integrates the best of Ethereum and sovereign blockchains into a fully functional multi-chain system. While it is less expensive and faster to use, it does not affect the Ethereum platform’s security and interoperability. As a result, an increasing number of developers are using it to build high-quality decentralized exchanges (DEXes) on top of the Polygon network. Here is a polygon DEXs stats.</p>'
    st.markdown(top_trend, unsafe_allow_html=True)

    st.markdown('#') 

    st.header('Opensea Stats')

   
