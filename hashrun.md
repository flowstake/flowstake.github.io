---
layout: default
---

## Activity Staking Blockchain Network
> - Public, Immutable, Activity Records
> - Public Activity Data Hashed into XYO Proof of Origin protocol
> - Geospacical Attestations, Digital Signatures Hashes from Bound Witnesses 
> - Proof of Origin protocol on XYO Network Hashing together Timestamps & Trackpoints
> - [explore.xyo.network/#/dashboard/](https://explore.xyo.network/#/dashboard)
> - [developers.xyo.network/docs/](https://developers.xyo.network/docs/en/explore-getting-started/)

## Hashrun - Proof of Origin
> - [github.com/flowstake/hashrun](https://github.com/flowstake/hashrun)
> - [github.com/flowstake/readme](https://github.com/flowstake/flowstake.github.io/blob/master/README.md)
> - [github.com/flowstake](https://github.com/flowstake)


## Proof of Activity as Stake
> - Utilizing Blockchain technology to create a timestamped record of activity.
> - Proof of Activity as Stake - hash, validate & stake activity transactions.
> - Each activity is a node, staking timestamps, runtime & last known location to validate proof of activity. 

### Problem to Solve
#### Purpose Of Our Hackathon Project:

* Reduce Tribalism and Encourage Interoperability within the Blockchain Ecosystem by using leading chainlayers EOS and XYO to visualize and share valid spatial data. 
 
#### Applications for DAO and DACs

Enable EOS based DAOs and DACs to visualize relevant spatial and activity data of the human or autonomous actors within the DAO/DAC using data from XYO verified witness activity. 

### BACKEND UTILITY
Write a script that uses the XYO protocol to generate GPS coordinates / hash addressed content to put into the EOS chain

* $BASH script that can run locally on our machines
* Build with EOS PoS / XYO Bound Witnessing


### FRONT END APP VIEWS
* Deploying with XYO swift SDK on iPhone 7
* https://developers.xyo.network/docs/en/SDK-Core-Swift/

* Then we will use the data from the GPS coordinates over a series of trackpoints to complete “proof of origin + proof of human work = proof of activity”
* Effectively we can use the XYO sdk (COIN app) to display the front end
* We can Query the XYO chain and send that into EOS testnet

*   Verify / attest identity, record / hash activity data, digitally sign hashes for activity validation. 
*   Distributed activity attestations & sync activity metrics into blockchain.
*   Staking contract for verified activity via smart contract.

### Proof of Stake - Smart Contract 
> - Hybrid Proof of Stake / Proof of Activity
> - Escrow Time Release Proof of Activity Smart Contract
> - Activity timestamp verified on the blockchain network

### Proof of Activity - Validators 
- Proof of Activity as a Stake - P2P Validators
- To ensure reputable activity data, each node must validate completed activities (x) as transactions to secure network.
- Operate a validator node to stake the network
- Hashes are stored using the XYO Proof of Origin protocol
- Validator nodes create bound witnesses and stake the longest chain of events

### XYO Network - Proof of Origin Protocol
- Built upon a decentralized network of devices that anonymously collect and validate geospatial data, or data with a geographic component. At the center of it all sits one of the most exciting new cryptocurrencies that incentivizes the ecosystem - The XYO Token.

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

Enter the query where:PUBLIC_KEY

#### Tracking Public Key 

Public Key - Bound Witness

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


