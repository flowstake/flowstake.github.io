### [FlowStake](https://flowstake.github.io/) + [Hashrun](https://flowstake.github.io/hashrun) - Activity Staking Blockchain Network
* Public, Immutable, Activity Records
* Public Activity Files Hashed into IPFS protocol
* Proof of Activity as Stake Consensus Mechanism
* Trustless, Geospatial, Smart Contracts

## Proof of Activity 

Data ownership, Content addressed storage, Hash addressed Activity Trackpoints
IPFS has given the users the power of content-addressed storage.
IPFS protocol generates secure & reliable records for proof of activity.
Compiling trackpoints of GPS & accelerometer data from sensors on mobile & wearable devices.
Parsing activity data into distributed encrypted ledgers with Blockchain technology.

Proof of Activity Smart Contract - Staking proof of activity events into escrow smart contracts with time based release to prove consistent, recoccuring runtime / activity on timechain. Trackpoint metrics analyze 1 minute segments - analyzing data for Max Accelration, Max Speed & Activity Duration

-  Proof of Activity as a Stake - Validators
    * To ensure network consensus & valid activity data, each node must process transactions to secure network activity.
    * Activity timestamp hash verified on the blockchain network
    * Operate a validator node to stake the network 
    * Validator nodes verify proof of activity IPFS timestamps

- Hashing and Encrypting Activity Real Time
    - Requirements - Trackpoint Data
    - Smart Contract - Mining Activity to Generate Blocks
        - Throughput Requirements for Sigining Activity Live - 1 min / 60 seconds - (60 tracepoints)
        - Live Active Validator - 1 hour / 60 mins / 3600 seconds (3,600 transactions)
        - Live Active Validator - 24 hours / 1440 minutes / 86,400 seconds (86,400 transactions) 

- Token Generation Event - Network Protocol Generates Tokens for Verified Activity Time
- Proof of Activity - Token Generation Event as a result of hybrid computational networks, recording and encrypting activity information, second per second track points.
- Proving human activity to stake reputation on the Proof of Activity as a Stake network.
- Hashing activity from sports tracking apps into IPFS.
- Parsing activity data & digitally signing it into the network.
    
## Linux / Ubuntu 18.04 Installation 
### Install Resources - Development Tools

### [IPFS.io](https://ipfs.io)
* [Download IPFS for your platform](https://dist.ipfs.io/#go-ipfs)
* macOS and Linux
* After downloading, untar the archive, and move the ipfs binary somewhere in your executables $PATH using the install.sh script:

```bash
$ tar xvfz go-ipfs.tar.gz
$ cd go-ipfs
$ ./install.sh
```
### [Install Rustup](https://rustup.rs/)
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup target add wasm32-unknown-unknown
```
### [CasperLabs Tech Spec](https://techspec.casperlabs.io)
* [CasperLabs/CasperLabs](https://github.com/CasperLabs/CasperLabs)
* [Installation Documentation](https://github.com/CasperLabs/CasperLabs#documentation)
* [Installing the CasperLabs Node](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/INSTALL.md)
* [Building the CasperLabs Node](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/BUILD.md)
* [Creating Keys](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/KEYS.md)
* [Running the CasperLabs Node](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/NODE.md)
* [Deploying Contracts](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/CONTRACTS.md)
* [Querying](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/QUERYING.md)
* [Contributing](https://github.com/CasperLabs/CasperLabs/blob/dev/CONTRIBUTING.md)
* [Useful Diagrams](https://github.com/CasperLabs/CasperLabs/blob/dev/docs/DIAGRAMS.md)

### Generate Account / Faucet Tokens
* [clarity.casperlabs.io](https://clarity.casperlabs.io/#/)
* [capserlabs dockerhub](https://hub.docker.com/u/casperlabs)
* [devnet-graphql.casperlabs.io](http://devnet-graphql.casperlabs.io:40403/graphql)
* [explorer.casperlabs.io](https://explorer.casperlabs.io/#/blocks)

### Proof of Activity as a Stake - Key Value Storage
* [casperlabs-kv-storage](https://github.com/zie1ony/casperlabs-kv-storage)
* This is an example of a simple string-base key-value smart contract and it's usage.
#### Step 1 - Compile smart contracts.
```bash
$ cargo build --release
```
#### Step 2 - Save value under a key.
* Make sure to run scripts in the root directory!
```bash
./scripts/put.sh "Proof of Activity" "QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"
Deployed with hash 29d06b2368fe3b4f137eb6875bd0c8643f61cf6e2f1bb081f672792bcd954d61
```

#### Step 3 - Check the value. 
```bash
$ ./scripts/get.sh "Proof of Activity"
```
* Value of the counter should be QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk.

#### Step 4 - GraphQL

You can check the value of the counter using devnet's GraphQL console: https://devnet-graphql.casperlabs.io
Go to and then:
* Check latest block hash in
```bash
query {
  dagSlice(depth: 1) {
      blockHash
  }
}
```

#### Step 5 - Get public key of your account
* Make sure to run scripts in the CasperLabs root directory!
```bash
$ cat keys/key.public.hex.key
$ 64d0c86f888e925731cae4398c6ea86d26a14e2574e70b36bd4eeaec3a292cde
```

#### Step 6 - Query / Check the counter value.
* [devnet-graphql.casperlabs.io](http://devnet-graphql.casperlabs.io:40403/graphql)
* Put block hash under blockHashBase16Prefix and your public key under keyBase. 
* Put your key in pathSegments like in the example.
```bash
# Proof of Activity - IPFS Hash & Casper Key Value Storage
query {
  globalState(
    blockHashBase16Prefix: "f6836d87da9f9efc7a5fe7707f894f7be225e8e19cbf61954a2870c58bdbb966"
    StateQueries: [
      {
        keyType: Address
        keyBase16: "64d0c86f888e925731cae4398c6ea86d26a14e2574e70b36bd4eeaec3a292cde"
        pathSegments: ["QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"]
      }
    ]
  ) {
    value {
      __typename
      ... on IntValue {
        int: value
      }
    }
  }
}
```

#### FLOWSTAKE TO DO LIST

1. API pull request from Strava for Athlete Activity with API Key 
Rate Limits - 	600 requests every 15 minutes, 30000 daily	

2.Export Activity / Create Subscription with Webhooks, cURL, Httpie or Postman.
* Webhook Events API - http://developers.strava.com/docs/webhooks/
* Webhook Example - https://developers.strava.com/docs/webhookexample/
* Make a Postman or cURL request to subscribe to a webhook.
* Strava Playground - https://developers.strava.com/playground/
* Strava Playground Activities - https://developers.strava.com/playground/#/Activities/getActivityById/
* To use the Playground, go to https://www.strava.com/settings/api and change your “Authorization Callback Domain” to developers.strava.com. 
* [Strava API](https://www.strava.com/settings/api)
* [Strava Activity Data](https://www.strava.com/activities/2744688834)
* [Export GPX](https://www.strava.com/activities/2744688834/export_gpx)
* [Export TCX](https://www.strava.com/activities/2744688834/export_tcx)

3. Generate Hash Addressed Proof of Activity with IPFS 
* [IPFS Hash  QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk](https://ipfs.io/ipfs/QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk)
```bash
ipfs add Proof_of_Activity_as_a_Stake.gpx
added QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk Proof_of_Activity_as_a_Stake.gpx
48.27 KiB / 48.27 KiB [==========================] 100.00%
```
4. Write Hash into CASPER - DAG Blockchain 
```bash
flowstake@flowstake:~/casperlabs-kv-storage$ ./scripts/put.sh "activity" "QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"
Deployed with hash a096d6917bccc6df9f102f951e5ce68a3db15d49791405a6e28f557c7d6cbaa5
```
5. Reference Activity Hashes with Blocks on CasperLabs DAG / BlockChain
```bash
$ ./scripts/get.sh "Proof of Activity"
```
* Value of the counter should be QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk.

6. GraphQL Query for Proof of Activity Blocks
Write your query or mutation here
```bash
# Proof of Activity - IPFS & Casper Key Value Storage
query {
  globalState(
    blockHashBase16Prefix: "f6836d87da9f9efc7a5fe7707f894f7be225e8e19cbf61954a2870c58bdbb966"
    StateQueries: [
      {
        keyType: Address
        keyBase16: "64d0c86f888e925731cae4398c6ea86d26a14e2574e70b36bd4eeaec3a292cde"
        pathSegments: ["QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"]
      }
    ]
  ) {
    value {
      __typename
      ... on IntValue {
        int: value
      }
    }
  }
}
```
* Flowstake Public Key - Base(16)
* 74172b5a649058a6b6048b7a1d1d527369ce20b1f7a2d262836bdc9889582689

### Extra Resources  & Development Tools 

#### [Strava API Settings](https://www.strava.com/settings/api)

* [Share Activity Route](https://www.strava.com/routes/22211617)
* [IPFS Hash  QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd](https://ipfs.io/ipfs/QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd)
* [CasperLabs GraphQL Devnet](http://devnet-graphql.casperlabs.io:40403/graphql)
* [GraphQL](https://graphql.org/learn)
* [PHP Library for parsing running GPS activities (.TCX .GPX .PWX .CSV)](https://github.com/flowstake/Waddle)

### [Install httpie](https://httpie.org)
* Local Installation - macOS Mojave 10.14.4
On macOS, HTTPie can be installed via Homebrew (recommended):
```bash
$ brew install httpie
==> Downloading https://homebrew.bintray.com/bottles/httpie-1.0.3.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/24/2436432e8ee1efe7f6c19c501af35aba453dabe3b9a9f88bed4e22a795bc6d1c?__gda__=exp
######################################################################## 100.0%
==> Pouring httpie-1.0.3.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/httpie/1.0.3: 946 files, 11.0MB
```

Below is an example request to the Strava API using HTTPie, along with sample response headers for a successful and rate-limited request:

Example request
```bash
$ http 'https://www.strava.com/api/v3/athlete' \
    'Authorization:Bearer d4cc0724eed83ffddcb8715d7fd83d3588724cc5'
```

### Docker Runtime Container
* Install [Docker for MacOS](https://docs.docker.com/docker-for-mac/install/)
* Docker Container 
* Docker Pull Commands
```bash
$ docker pull casperlabs/client
$ docker pull casperlabs/buildenv
$ docker pull casperlabs/grpcwebproxy
$ docker pull casperlabs/node
$ docker pull casperlabs/execution-engine
$ docker pull casperlabs/explorer
$ docker pull casperlabs/key-generator
```

### Related Research Concepts
* [Point of Interest](https://en.wikipedia.org/wiki/Point_of_interest)
* [Proof of Activity](http://netecon.seas.harvard.edu/NetEcon14/Papers/Bentov_netecon14.pdf)
* [Cryptographic Hash Function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
* [Garmin XML Schemas](https://www8.garmin.com/xmlschemas/index.jsp#/web/docs/xmlschemas)
* [GPS Exchange Format](https://en.wikipedia.org/wiki/GPS_Exchange_Format)
