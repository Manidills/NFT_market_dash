import json
import requests
import pandas as pd
import streamlit as st


def api():
        url = f"https://api.covalenthq.com/v1/1/nft_market/?key=ckey_eb29565e970e4b46930dca374df"
        response = requests.request("GET", url)
        if response.status_code ==200:
            data = response.json()
            data = data['data']['items']
            df = pd.DataFrame(data)
            df.drop(['volume_wei_24h', 'volume_quote_24h','avg_volume_wei_24h','avg_volume_quote_24h'],axis=1, inplace=True)
            return df
        else:
            st.info("Data Not Found")

def balance(address):
        url = f"https://api.covalenthq.com/v1/1/address/{address}/balances_v2/?quote-currency=USD&format=JSON&nft=false&no-nft-fetch=false&key=ckey_eb29565e970e4b46930dca374df"
        response = requests.request("GET", url)
        if response.status_code ==200:
            data = response.json()
            data = data['data']['items']
            df = pd.DataFrame(data)
            return df
        else:
            st.info("Data Not Found")
def historical_portfolio(address):
        url = f"https://api.covalenthq.com/v1/1/address/{address}/portfolio_v2/?quote-currency=USD&format=JSON&key=ckey_eb29565e970e4b46930dca374df"
        response = requests.request("GET", url)
        if response.status_code ==200:
            data = response.json()
            data = data['data']['items']
            df = pd.DataFrame(data)
            return df
        else:
            st.info("Data Not Found")

def get_nft_trans(address, token):
        url = f"https://api.covalenthq.com/v1/1/tokens/{address}/nft_transactions/{token}/?quote-currency=USD&format=JSON&key=ckey_eb29565e970e4b46930dca374df"
        response = requests.request("GET", url)
        if response.status_code ==200:
            data = response.json()
            data = data['data']['items']
            df = pd.DataFrame(data)
            return df
        else:
            st.info("Data Not Found")

def contract_stats(chain, address,):
    url = f"https://api.nftport.xyz/v0/transactions/stats/{address}"
    payload = {
        "chain": str(chain)
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:

        data = response.json()

        return data
    else:
        st.info("Data Not Found")

def contract_trans(chain, address):
    url = f"https://api.nftport.xyz/v0/transactions/nfts/{address}"
    payload = {
        "chain": str(chain),
        "type":"sale"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:

        data = response.json()
        data = data['transactions']
        df = pd.DataFrame(data)
        return df
    else:
        st.info("Data Not Found")

def nft_token(chain, address, token):
    url = f"https://api.nftport.xyz/v0/nfts/{address}/{token}"
    payload = {
        "chain": str(chain)
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:

        data = response.json()

        return data
    else:
        st.info("Data Not Found")


def nft_trans(chain, address, token):
    url = f"https://api.nftport.xyz/v0/transactions/nfts/{address}/{token}"
    payload = {
        "chain": str(chain),
        "type":"sale"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:

        data = response.json()
        data = data['transactions']
        df = pd.DataFrame(data)
        return df
    else:
        st.info("No Sales yet")

def wallet_nft_created(chain,address):
    url = f"https://api.nftport.xyz/v0/accounts/creators/{address}"
    payload = {
        "chain": str(chain),"include":"metadata"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:

        data = response.json()
        #st.write(data)
        #data = pd.DataFrame.from_dict(data['nfts'], orient='columns')
        return data
    else:
        st.info("Data Not Found")

def wallet_nft_owned(chain,address):
    url = f"https://api.nftport.xyz/v0/accounts/{address}"
    payload = {
        "chain": str(chain),"include":"metadata"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:
       
        data = response.json()
        try:
            data = data['nfts']
            df = pd.DataFrame(data)
            st.dataframe(df)
            return df
        except:
            
            return data

        
    else:
        st.info("Data Not Found")

def wallet_contract_owned(chain,address):
    url = f"https://api.nftport.xyz/v0/accounts/contracts/{address}"
    payload = {
        "chain": str(chain),"type": "owns_contract_nfts"
    }

    headers = {
        'Content-Type': "application/json",
        'Authorization': "f6ce3372-a928-4947-8f50-87649f60cee2"
        }

    response = requests.request("GET", url,  params=payload, headers=headers)
    if response.status_code ==200:
       
        data = response.json()
        data = data['contracts']
        df = pd.DataFrame(data)
        return df

        
    else:
        st.info("Data Not Found")
