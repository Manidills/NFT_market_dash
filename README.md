

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

The frameworks/libraries explicitly used in this project are

* [Python](python.org)
* [keras](https://keras.io/)
* [streamlit](https://streamlit.io/)
* [streamlit-aggrid](https://pypi.org/project/streamlit-aggrid/)
* [requests](https://docs.python-requests.org/en/latest/)
* sqlite


<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation

Follow these steps to install certain packages which is to be installed in this project also make your own 
API key from covalent to get access for data.

### Home page data is not complete ethereum data, we can take it as approx 

1. Get a free API Key from [covalent](https://www.covalenthq.com/)
2. Clone the repo
3. streamlit run main.py

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites

* altair==4.2.0
* keras==2.8.0
* numpy==1.22.1
* pandas==1.4.0
* pillow==9.0.1
* requests==2.22.0
* scikit_learn==1.0.2
* streamlit==1.4.0
* streamlit-aggrid
* sqlite




<!-- CONTRIBUTING -->
## API

We have used API's from covalent for listing transcation details, analayze and etc.


* COVALENTHQ API USED
```js

1.https://api.covalenthq.com/v1/1/address/{address}/transactions_v2/?key=key 
2.https://api.covalenthq.com/v1/1/transaction_v2/{hash}/?key=key 
3.https://api.covalenthq.com/v1/1/networks/aave_v2/assets/?quote-currency=USD&format=JSON&key=ckey_docs
```

Above apis are used to get transaction details for protocols that help to make seperate tables on sqlite.
## Acknowledgments

Would like to give credit to below teams for providing the API's
 

* [Covalent](https://www.covalenthq.com/)
* [ETL](https://github.com/blockchain-etl/ethereum-etl)
* [polygon ETL](https://github.com/blockchain-etl/polygon-etl)
* Filpsidecrypto // Dune


<p align="right">(<a href="#top">back to top</a>)</p>





