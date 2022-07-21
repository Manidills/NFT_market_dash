

<!-- PROJECT LOGO -->

<br />
<div align="center">
   <a href="https://ibb.co/JzrQbZJ"><img src="https://i.ibb.co/JzrQbZJ/Add-a-little-bit-of-body-text.png" "></a> 
  <h3 align="center">NFT CONSOLE</h3>
   <summary>DEPLOYED URL -> https://manidills-nft-market-dash-main-a4o57e.streamlitapp.com</summary>
</div>


<!-- TABLE OF CONTENTS -->
<details>
 
  <summary>Table of Contents</summary>
  <ol>
    
    <li>
      
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Usage">Application Insights</a></li>
    <li><a href="#API">API's </a></li>
    <li><a href="#ProjectLink">Project Link</a></li>
    <li><a href="#Acknowledgments">Acknowledgments</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

NFT Console is the NFT portfolio and data analytics application, that help to understand NFT marketplace's,collections, tokens and wallet analytics. That support ethereum and polygon blockchain's.

### Features
* NFT_Markets
     ```js
    1.NFT Global volume
    2.Opensea volume over time
    3.Opensea volume txs over time
    4.Opensea volume users over time
    5.Opensea txs over time
    6.Opensea users over time
    7.Looksrare volume over time
    8.Looksrare volume txs over time
    9.Looksrare volume users over time
    10.Looksrare txs over time
    11.Looksrare users over time
    12.X2y2 volume over time
    13.X2y2 volume txs over time
    14.X2y2 volume users over time
    15.X2y2 txs over time
    16.X2y2 users over time
   
   ```

* POAP
    ```js
    ( DATA RETRIEVE FROM IPFS HTTP CLIENT via [https://github.com/ipfs-shipyard/py-ipfs-http-client] )
      
    1.POAP wallet counts mainnet
    2.POAP wallet counts xdai
    3.POAP monthly mints mainnet
    4.POAP monthly mints xdai
    5.POAP top wallets txs mainnet
    6.POAP top wallets txs xdai
    7.Opensea poap total usd
    8.Opensea poap number of traders
    9.Opensea poap number of buyers
    10.Opensea poap number of sellers
    11.Opensea poap top buyers
    12.Opensea poap top sellers
    13.Opensea poap top events
    14.Opensea poap most traded
    15.Opensea poap sale distributions
    16.Opesea daily stats
    ```
    
* Collection's
    ```js 
    1.Collection stats ( Top contracts )
    2."one_day_volume"
    3."one_day_change"
    4."one_day_sales"
    5."one_day_average_price"
    6."seven_day_volume"
    7."seven_day_change"
    8."seven_day_sales"
    9."seven_day_average_price"
    10."thirty_day_volume"
    11."thirty_day_change"
    12."thirty_day_sales"
    13."thirty_day_average_price"
    14."total_volume"
    15."total_sales"
    16."total_supply"
    17."total_minted"
    18."num_owners"
    19."average_price"
    20."market_cap"
    21."floor_price"
    22.Contract Sale Transactions
    ```
* Token's
     ```js 
    1.Contract Metadata
    2.NFT Metadata
    3.NFT Sales Transactions
    4.NFT Image
    5.NFT Analytics Details
    6.NFT Estimated Price
    ```
    
* Wallets
    ```js
    1.NFT's Created By The Wallet
    2.Contract's owned by Wallet
    3.Token's Balance
    4.Historical Portfolio Value Over Time
    5.NFT's owned by Wallet
    6.NFT Sales On ETH
    7.Top 5 NFT's with metadata
    ```
      
* Summary
    ```js
    WORDCLOUD IMAGE WITH SUMMARY
    1.Most used contract
    2.Most used token
    3.Total balance
    4.Most used NFT contract type
    5.Most interacted address
    6.TOP NFT collection
    7.Verified or not
    8.Highest NFT buy
    9.Most NFT holding collection
    MANY more !!!!!!!!!!!

    ```
      
* Mint
    ```js
    MINT THE SUMMARY IMAGE ON "WALLET SUMMARY COLLECTION" ( POLYON CHAIN )
    1. Upload image
    2. IPFS URL  ( NFT PORT IPFS UPLOAD )
    3. NFT METADATA ( NFT STORAGE )
    ```



Website link : <summary>[NFT Console](https://manidills-nft-market-dash-main-a4o57e.streamlitapp.com/)</summary>



<p align="right">(<a href="#top">back to top</a>)</p>


### Built With
* <h1>IPFS (store_retrieve_ipfs_data.py)</h1>

1. https://github.com/ipfs-shipyard/py-ipfs-http-client

The IPFS python client used to store and retrieve the database's. Frequntly from the api's data's are stored as a database and moved to IPFS. In a meanwhile ipfs hash and database details stored as local DB.While moving the tabs to analytics page it retrieve the data from IPFS by passing the IPFS hash.

Store data to IPFS
```js
    api = ipfsApi.Client(host='https://ipfs.infura.io', port=5001)
    new_file = api.add(DB)
```
Retrieve data
```js
   response = requests.request("GET", f'https://ipfs.infura.io/ipfs/{ipfs hash}')
    with open("DB", "wb") as f:
        f.write(response.content)
 ```       
        
2. NFTPORT IPFS UPLOAD (https://docs.nftport.xyz/docs/nftport/b3A6Njg1NTI0MTY-upload-a-file-to-ipfs)

Minted wallet collection's NFT images are stored to IPFS via nftport api 

Store NFT data
```js
   requests.post(
        "https://api.nftport.xyz/v0/files",
        headers={"Authorization": '!!!!!'},
        files={"file": file}
    )
```
Retrieve NFT data

```js
   st.image(ipfs_link,width = 500) ( stremalit function retrieve the IPFS URL data )
```

3. NFT Storage UPLOAD (https://github.com/nftstorage/python-client/blob/main/docs/NFTStorageAPI.md#store)

NFT Storage used to store the wallet collections NFT Metadata and wallet infomation. Its really meant to store NFT data's and seems great ( HIghly recommended for NFT metadata )

Store data

```js
   host = "https://api.nft.storage"
   api_response = api_instance.store(body, _check_return_type=False)
   
 ```
Retrieve data

```js
     host = "https://api.nft.storage"
    api_response = api_instance.status(cid,_check_return_type=False)
```


* <h1>POLYGON (mint.py)<h1>
1.NFT console support both polygon and ethereum , we can find analytics for any polygon collection and wallet's

2.WALLET SUMMARY COLLECTION"S was minted on POLYGON CHAIN, each nft minted by people was store in POLYGON CHAIN via nftport easy mint api.

```js 
   query_params = {
        "chain": "Polygon",
        "name": name,
        "description": description,
        "mint_to_address": wallet_address
    }

   response = requests.post(
        "https://api.nftport.xyz/v0/mints/easy/files",
        headers={"Authorization": "****"},
        params=query_params,
        files={"file": file}
    )
```

* <h1>NFTPORT (common_data.py)</h1>

The analytics data was collected via NFT PORT API's, NFTPORT providing solid apis that more enough to build NFT dashboard very easily. 

NUMBER OF APIS USED 

```js
1.https://api.nftport.xyz/v0/transactions/stats/{address}
2.https://api.nftport.xyz/v0/transactions/nfts/{address}
3.https://api.nftport.xyz/v0/nfts/{address}/{token}
4.https://api.nftport.xyz/v0/transactions/nfts/{address}/{token}
5.https://api.nftport.xyz/v0/accounts/creators/{address}
6.https://api.nftport.xyz/v0/accounts/{address}
7.https://api.nftport.xyz/v0/accounts/contracts/{address}
8.https://api.nftport.xyz/v0/mints/easy/files
9.https://api.nftport.xyz/v0/files
```

* <h1>COVALENT (common_data.py)</h1>

Most the NFT Marketplaces data's and POAP related data was collected vis COVALENT apis, adding on that wallet balance and portfolio data's are directly avilable from there apis. That very helpful for creating a chart's.

```js
1.https://api.covalenthq.com/v1/1/nft_market/?key=ckey_eb29565e970e4b46930dca374df (old)
2.https://api.covalenthq.com/v1/1/address/{address}/balances_v2/?quote-currency=USD&format=JSON&nft=false&no-nft-fetch=false
3.https://api.covalenthq.com/v1/1/address/{address}/portfolio_v2/?quote-currency=USD&format=JSON
4.https://api.covalenthq.com/v1/1/tokens/{address}/nft_transactions/{token}/?quote-currency=USD&format=JSON
```

* <h1>POAP (POAP.py)</h1>

1. Analytics dashboard for POAP tokens on mainnet and xdai.
2. POAP tokens analytics on opensea platform ( DO check for intersting numbers )





<h2>**** BIG shout out for COVALENT, NFTPORT, IPFS, POLYGON and POAP for amazing work.</h2>




