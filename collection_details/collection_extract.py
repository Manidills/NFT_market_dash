import streamlit as st
import plost
import datetime
import pandas as pd
from pathlib import Path
from common_data import  api, contract_stats, contract_trans




def collection_extract():
    
    
    
    with st.form("form1", clear_on_submit=True): 
        values = ['ethereum', 'polygon']
        window_ANTICOR = st.selectbox('Blockchain_ID', values)
        title = st.text_input('Contract_address')

        submit = st.form_submit_button("Submit")

    

    
    if submit:

        st.header("Collection Portfolio")
      
        contract_stat = contract_stats(window_ANTICOR, title)
        
       
        #st.dataframe(df)
        col1, col2 = st.columns((2,2))

        with col1:
            try:
              st.write(contract_stat['statistics'])
            except:
              st.info("Not Found")
            
            
        with col2:
            st.subheader("Marketplace")
            st.image('https://www.freelogovectors.net/wp-content/uploads/2022/01/opensea-logo-freelogovectors.net_.png', width=400)

        st.markdown("#")
        st.subheader("Contract Sale Transactions")
        try:
            st.dataframe(contract_trans(window_ANTICOR, title))
        except:
            st.info("Data Not Found")
        
        
    else:
        st.header("Collections_Stats")
        st.header("#")
        df = api()
        st.dataframe(df)
