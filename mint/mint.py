import json
import tempfile
import requests
from PIL import Image
from store_retrieve_ipfs_data import get_ipfs_image, get_nft_storage, nft_storage_store, store_nft_image_ipfs
import streamlit as st
from tempfile import NamedTemporaryFile

def easy_mint(name, description, wallet_address, image):

    file = open(image, 'rb')

    query_params = {
        "chain": "rinkeby",
        "name": name,
        "description": description,
        "mint_to_address": wallet_address
    }

    response = requests.post(
        "https://api.nftport.xyz/v0/mints/easy/files",
        headers={"Authorization": "f6ce3372-a928-4947-8f50-87649f60cee2"},
        params=query_params,
        files={"file": file}
    )

    return response.json()

def mint():
    st.subheader("MINT THE SUMMARY IMAGE AS NFT")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])

    if image_file:
        temp_file = NamedTemporaryFile(delete=False)
        temp_file.write(image_file.getvalue())
        if image_file is not None:
            with st.form("form2", clear_on_submit=False): 
                name = st.text_input('Name')
                description = st.text_input('Description')
                wallet_address = st.text_input('Mint_address')
                submit = st.form_submit_button("Submit")

            if submit:
                mint_image = easy_mint(name,description,wallet_address,temp_file.name)
                st.write(mint_image)
                st.markdown("#")
                st.subheader("IPFS Stored URL")
                if mint_image['response'] == 'OK':
                    store_nft = store_nft_image_ipfs(temp_file.name)
                    st.write(store_nft['ipfs_url'])
                    st.markdown("#")
                    st.subheader("Minted Image")
                    get_ipfs_image(store_nft['ipfs_url'])
                    if store_nft:
                        tfile = tempfile.NamedTemporaryFile(mode="w+")
                        json.dump(store_nft, tfile)
                        tfile.flush()
                        nft_meta = nft_storage_store(tfile.name)
                        st.markdown("#")
                        st.subheader("Retrive Stored Data from NFT Storage")
                        retrive_data = get_nft_storage(nft_meta['value']['cid'])
                        st.info(retrive_data)
                        st.write(store_nft)

