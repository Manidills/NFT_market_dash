from common_data import balance, nft_token, nft_trans, wallet_contract_owned, wallet_nft_created, wallet_nft_owned
import streamlit as st
import datetime
from metrics import getdata
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import glob, random
from PIL import Image
from common.connect import *



def mint_extract():
    with st.form("form2", clear_on_submit=True): 
        wallet_add = st.text_input('Wallet_Address')
        submit = st.form_submit_button("Submit")

    if submit:
        values = []
        nft_c = wallet_nft_created('ethereum', wallet_add)
        values.append("'" + str(len(nft_c['nfts'])) + "'")
        nft_con = wallet_contract_owned('ethereum', wallet_add)
        try:
            list_of_nft_con = ['name', 'type', 'address','num_nfts_owned']
            for i in list_of_nft_con:
                if i == 'num_nfts_owned':
                    values.append("'" + str(int(nft_con['num_nfts_owned'].sum())) + "'")
                else:
                    values.append(nft_con.mode()[i][0])
        except:
            pass
        values.append("verified")
        bal = balance(wallet_add)
        list_of_bal = ['contract_name', 'contract_address', 'supports_erc', 'type', 'quote']
        try:
            for i in list_of_bal:
                if i == 'quote':
                    values.append("'" + str(int(bal[i].sum())) + "'")
                elif i == 'supports_erc':
                    values.append(bal.mode()[i][0][0])
                else:
                    values.append(bal.mode()[i][0])
        except:
            pass
        nft_o = wallet_nft_owned('ethereum', wallet_add)
        values.append("'" + str(len(nft_o)) + "'")
       


        file_path_type = ["mask/*.png"]
        images = glob.glob(random.choice(file_path_type))
        random_image = random.choice(images)
        twitter_mask = np.array(Image.open(random_image))
       
        unique_string=(" ").join(values)
        
        wordcloud = WordCloud(font_path='db/CabinSketch-Regular.ttf',width=800, height=400).generate(unique_string)
        fig, ax = plt.subplots(figsize=(20,10), facecolor='k')
        
        st.subheader("Wallet Summary Wordcloud")
        st.markdown("##")
        ax.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        st.pyplot(fig)

        img_fn = 'wordcloud.png'
        fig.savefig(img_fn)

        # Prepare file for download.
        dfn = 'wordcloud.png'
        with open(img_fn, "rb") as f:
            st.download_button(
                label="Download_Image",
                data=f,
                file_name=dfn,
                mime="image/png")
        

    