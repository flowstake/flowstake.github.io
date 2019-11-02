---
layout: default
---

## Hashrun - Blockchain SportsBook - [Proof of Activity](https://explore.xyo.network/#/explore/LastKnowLocation?publicKey=15msPzGS6HGEhefc1rVyz2xa2PcWxVonDSgySh49PAczVJbwoko14QvXMPZ3ymcyqSwjVsVE8TsXUTiPwFaTD6HjS1a&amount=100)
> - [flowstake.webflow.io](https://flowstake.webflow.io)
> - [github.com/flowstake/hashrun](https://flowstake.github.io/hashrun)

## Activity Staking XYO & EOS Blockchain Networks
- Public, Immutable, Activity Records
- Public Activity Data - Hash Addressed Location Signatures
- Handshakes Intersections into Timestamped, Trackpoints verifing Proof of Human Work

### Proof of Stake - Smart Contract 
> - Hybrid Proof of Stake / Proof of Activity
> - Escrow Time Release Proof of Activity Smart Contract
> - Activity Timestamp Verified on the Blockchain Network

### Proof of Activity - Validators 
- Proof of Activity as a Stake - P2P Validators
- To ensure reputable activity data, each node must validate completed activities (x) as transactions to secure network.
- Operate a validator node to stake the network
- Hashes are stored using the XYO Proof of Origin protocol
- Validator nodes create bound witnesses and stake the longest chain of events
- Key value storage smart contract on EOS Platform 

## EOS.IO - Delegated Proof of Stake Blockchain
> - [https://developers.eos.io](developers.eos.io)
> - [https://github.com/EOSIO/eos](github.com/eosio)
> - Smart contract key value storage, for cross platform immutable, persistant & activity records. 
> - Open-source blockchain software protocol that provides developers & entrepreneurs to build high performance applications.

### XYO Network - Proof of Origin Protocol
- [explore.xyo.network/#/dashboard/](https://explore.xyo.network/#/dashboard)
- [developers.xyo.network/docs/](https://developers.xyo.network/docs/en/explore-getting-started/)
- [Install Official Client to use XYO](https://github.com/XYOracleNetwork)

- Turn your devices into a Sentinel, Bridge, Archivist or Diviner
- Network Hashing together Timestamps & Trackpoints.
- Decentralized network of devices that anonymously collect and validate geospatial data.
- Cryptographic geospacical handshakes, generating hashes from bound witnesses.
- Built upon a decentralized network of devices that anonymously collect and validate geospatial data, or data with a geographic component. At the center of it all sits one of the most exciting new cryptocurrencies that incentivizes the ecosystem - The XYO Token.

## Proof of Activity as Stake - POS
> - Utilizing Blockchain technology to create a timestamped record of activity.
> - Proof of Activity as Stake - hash, validate & stake the longest chain of activity transactions.
> - Each activity is a node, bounding witnesses, timestamping runtime & last known location to validate proof of activity. 

## Problem to Solve
### Purpose Of Our Hackathon Project:

- Reduce Tribalism and Encourage Interoperability within the Blockchain Ecosystem by using leading chainlayers EOS and XYO to visualize and share valid spatial data. 

### Distributed Athletic Community - DAC
> - Distributed Athletic Community
> - Generate Performance Records
> - Immutable Data Storage & Persistanc
 
#### Applications for DAO and DACs

* https://developers.eos.io/eosio-home/docs/installing-the-contract-development-toolkit
* https://developers.eos.io/eosio-home/docs/data-persistence
* Enable EOS based DAOs and DACs to visualize relevant spatial and activity data of the human or autonomous actors within the DAO/DAC using data from XYO verified witness activity. 

### BACKEND UTILITY
> * Write a script that uses the XYO protocol to generate GPS coordinates / hash addressed content to put into the EOS chain
> * $BASH script that can run locally on our machines
> * Build with EOS PoS / XYO Bound Witnessing
> * EOS Data Persistance

### FRONT END APP VIEWS
* Deploying with XYO swift SDK on iPhone 7
* https://developers.xyo.network/docs/en/SDK-Core-Swift/
* Then we will use the data from the GPS coordinates over a series of trackpoints to complete “proof of origin + proof of human work = proof of activity”
* Effectively we can use the XYO sdk (COIN app) to display the front end
* We can Query the XYO chain and send that into EOS testnet
*   Verify / attest identity, record / hash activity data, digitally sign hashes for activity validation. 
*   Distributed activity attestations & sync activity metrics into blockchain.
*   Staking contract for verified activity via smart contract.

## XYO.NETWORK 

### Install Mobile Application 
* Android Devices - Google Play Store
* [https://play.google.com/store/apps/details?id=network.xyo.app&hl=en_US](play.google.com/stores/network.xyo.app)
* Apple Devices - Apple App Store
* [https://apps.apple.com/us/app/xyo-network/id1453770624](apps.apple.com/us/app/xyo-network)

### XYO GraphQL Query

Searching the XYO network for location of users
Creating cryptographic handshakes 

#### Entering a Query

Enter all queries described in this guide into this field on the dashboard page

#### Block Hash Query

* The hash query retrieves block contents from the block hash provided.
* Enter the query hash:BLOCK_HASH
* Information included in the contents

* Previous Hash
* Public Key (of previous hash)
* Rssi (of previous hash)
* Index (of previous hash)
* GPS
* BlockBytes
* Lat and Long Query

The near query retrieves blocks near GPS point provided.
Enter the query near:LAT,LNG

#### Recent Query

* The recent query gets n recent blocks.
* Enter the query recent:LIMIT (integer value - example typed as 01)
* This is a dynamic query that will change since blocks are continuously created
* You will see your query value in the lower left corner of the map view.
* This is an exmaple after a recent:030 query

#### Where Query

* The where query gets the last known blocks from a device public key
* Enter the query where:PUBLIC_KEY
*where:15msPzGS6HGEhefc1rVyz2xa2PcWxVonDSgySh49PAczVJbwoko14QvXMPZ3ymcyqSwjVsVE8TsXUTiPwFaTD6HjS1a


#### Tracking Public Key 

Public Key - Bound Witness
* Enter the query Last Known Location
* https://explore.xyo.network/#/explore/LastKnowLocation?publicKey=15msPzGS6HGEhefc1rVyz2xa2PcWxVonDSgySh49PAczVJbwoko14QvXMPZ3ymcyqSwjVsVE8TsXUTiPwFaTD6HjS1a&amount=100

#### Chain Query

* Enter the query chain:PUBLIC_KEY
* The chain query retrieves the latest bound witness from an origin chain and current reward data for the chain

#### Smart Contract Key Value Storage 

* You can also see the rewards that this chain has earned (this is if this chain participated in answering queries from a diviner)
* The data down the chain graphically represents index values, rssi, the devices that bound witnessed on the block.

#### Geohash Query

* The geohash query gets known blocks from the geohash provided
* Enter the query geohash:GEOHASH

### Blocks Query

* The blocks query retrieves random n blocks
* Enter the query blocks:LIMIT (integer value - example typed as 01)

### Available queries offered

* Chain Segment
* Intersection
* Geohash
* Time
* Page
* Last Known Location

## EOS - Delegated Proof of Stake Blockchain

> - [https://developers.eos.io](developers.eos.io)
> - [https://github.com/EOSIO/eos](github.com/eosio)

## EOS - [Setting Up your Development Environment](https://developers.eos.io/eosio-home/docs/getting-the-software)

> - [https://developers.eos.io/eosio-home/docs/setting-up-your-environment](https://developers.eos.io/eosio-home/docs/setting-up-your-environment)

### Step 1: Install Binaries 

- Use pre-built binaries. For you to get started as quickly as possible this is the best option. Building from source is an option but will set you back an hour or more and you may encounter build errors.
- The below commands will download binaries for respective operating systems.

#### Mac OS X Brew Install: Shell
```bash
brew tap eosio/eosio
brew install eosio
```

#### Ubuntu 18.04 Debian Package Install: Shell
```bash
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio_1.7.0-1-ubuntu-18.04_amd64.deb
sudo apt install ./eosio_1.7.0-1-ubuntu-18.04_amd64.deb
```

#### Ubuntu 16.04 Debian Package Install: Shell
```bash
wget https://github.com/EOSIO/eos/releases/download/v1.7.0/eosio_1.7.0-1-ubuntu-16.04_amd64.deb
sudo apt install ./eosio_1.7.0-1-ubuntu-16.04_amd64.deb
```

### Step 2: Setup a development directory, stick to it.
You're going to need to pick a directory to work from, it's suggested to create a contracts directory somewhere on your local drive.
```bash
mkdir contracts
cd contracts
```

### Step 3: Enter your local directory below.
Get the path of that directory and save it for later, as you're going to need it, you can use the following command to get your absolute path.
```bash
pwd
```
Enter the absolute path to your contract directory below, and it will be inserted throughout the documentation to make your life a bit easier. This functionality requires cookies

### 



### EOS - Key Value Storage & Data Persistance

- [https://github.com/flowstake/eosio.contracts](https://github.com/flowstake/eosio.contracts)

### EOS - Smart Contracts 

- [contract/eosio.token/](https://github.com/flowstake/eosio.contracts/blob/master/contracts/eosio.token/include/eosio.token/eosio.token.hpp)
- [contract/eosio.system/](https://github.com/flowstake/eosio.contracts/tree/master/contracts/eosio.system) 


#### Deploy EOS Wallets 

```bash
cleos wallet create --to-console

"/usr/local/Cellar/eosio/1.8.5/opt/eosio/bin/keosd" launched
Creating wallet: default
Save password to use in the future to unlock this wallet.
Without password imported keys will not be retrievable.
"PW5Hwj71vw3gYFSdYs2fKFALMvdActDoRqDomRSFEQFYUtR3RM68g"
```

#### Open EOS Wallets

```bash
cleos wallet open
cleos wallet list
```

#### Unlock EOS Wallets

```bash
* cleos wallet unlock
```

#### Create EOS Wallets

```bash
cleos wallet create_key
```

#### Import EOS Wallets

```bash
cleos wallet import
enter the eosio development key provided below
5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3
```

### Create EOS account

```bash

cleos create account eosio token {public-OwnerKey} {public-ActiveKey}
cleos create account eosio hashrun EOS5BZi9LEKHhNSa8qV9vZczYJkYgVuQzFgX5YNmKM6hP5Ku9dEBb PW5Hwj71vw3gYFSdYs2fKFALMvdActDoRqDomRSFEQFYUtR3RM68g
```

#### Get EOS account from Testnet

```bash
cleos get account hashrun
```

### EOS Smart Contract Deployment 

* - [contract/eosio.token/](https://github.com/flowstake/eosio.contracts/blob/master/contracts/eosio.token/include/eosio.token/eosio.token.hpp)

#### Step 1: Build directory & navigatation

```bash
mkdir sportsbook
cd sportsbook
```

#### Step 2: Create and open a new file

```bash
touch sportsbook.cpp
```

### Step 3: Deploy [Smart Contract - Sportsbook](https://flowstake.webflow.io/)

```c++
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("sportsbook")]] sportsbook : public eosio::contract {
  public:
       
  private: 
  
};
```

#### Step 3: Write an Extended Standard Class and Include EOSIO

```c++
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("sportsbook")]] sportsbook : public eosio::contract {
  public:
       
  private: 
  
};
```
#### Step 4: Create The Data Structure for the Table

```c++
struct person {};
```

```c++
struct person {
 name key; 
};
```

```c++
struct person {
 name key;
 std::string first_name;
 std::string last_name;
 std::string hash:BLOCK_HASH;
 std::string chain:PUBLIC_KEY;
 std::string where:PUBLIC_KEY
 std::string geohash:GEOHASH;
 std::string near:LAT,LNG;
 
 uint64_t primary_key() const { return key.value;}
};
```
#### Step 5: Configure the Multi-Index Table

```c++
#include <eosio/eosio.hpp>

using namespace eosio;

class [[eosio::contract("sportsbook")]] sportsbook : public eosio::contract {

  public:

  private:
    struct [[eosio::table]] person {
      name key;
      std::string first_name;
      std::string last_name;
      std::string hash:BLOCK_HASH;
      std::string chain:PUBLIC_KEY;
      std::string where:PUBLIC_KEY
      std::string geohash:GEOHASH;
      std::string near:LAT,LNG;

      uint64_t primary_key() const { return key.value;}
    };
  
    typedef eosio::multi_index<"people"_n, person> hash_index;
};
```

##### FlowStake 2019 
