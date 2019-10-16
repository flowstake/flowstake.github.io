---
layout: default
---

## Activity Staking Blockchain Network
> - Public, Immutable, Activity Records
> - Public Activity Data Hashed into IPFS protocol
> - [github.com/flowstake](https://github.com/flowstake)

## Proof of Activity as Stake
> - Utilizing Blockchain technology to create a timestamped record of activity.
> - Proof of Activity as Stake - hash, validate & stake activity transactions.
> - Each activity is a node, staking runtime to validate proof of activity. 

### Problem to Solve
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
- Hashes are stored using the IPFS protocol
- Validator nodes verify and stake activity transactions

### Proof of Activity - IPFS Trusted Timestamping
> - IPFS protocol generates secure & reliable records for proof of activity. 
> - Compiling GPS + Activity trackpoints & accelerometer data from sensors on mobile & wearable devices. 
> - Parsing activity data into hashes recorded on distributed encrypted ledgers with Blockchain technology.

### Proof of Activity - IPFS Activity Hashing 
> - Hashing activity from sports tracking apps into IPFS.
> - Proving human activity from peers & validators across the network.
> - Building activity reputation consistently on the PoA as Stake network. 

### Proof of Activity - Staking Smart Contract
- Smart Contract - Proof of Activity as a Stake Time Release Escrow 
- Token Generation Event - Network Protocol Generates Tokens for Validating Activity Time, Activity Hash Trackpoint Data
- Smart contract token staking into escrow time based contract to prove activity to the network on every 24hrs.
- Analyzing data for Max Acceleration, Max Speed & Activity Duration
- Trackpoint metrics analyze 1 minute segments

> - Throughput requirements for live records - 1 min / 60 seconds - (60 tracepoints)
> - Live Active Validator - 1 hour / 60 mins / 3600 seconds (3,600 transactions)
> - Live Active Validator - 24 hours / 1440 minutes / 86,400 seconds (86,400 transactions)

* Proof of Activity - Token Generation Event as a result of hybrid computational networks, recording and encrypting activity information, second per second track points.

### Development Tools & Resources 

* [IPFS Hash QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd](https://ipfs.io/ipfs/QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd)
* [PHP Library for parsing running GPS activities (.TCX .GPX .PWX .CSV)](https://github.com/flowstake/Waddle)
* [CasperLabs](https://casperlabs.io)
* [CasperLabs Devnet](http://devnet-graphql.casperlabs.io:40403/graphql)
* [CasperLabs Explorer](https://explorer.casperlabs.io/#/explorer)
* [GraphQL](https://graphql.org/)

### Concepts

* [Cryptographic_hash_function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
* [Distributed_hash_table](https://en.m.wikipedia.org/wiki/Distributed_hash_table)
* [Trusted_timestamping](https://en.wikipedia.org/wiki/Trusted_timestamping)
* [Tragedy of the commons](https://en.wikipedia.org/wiki/Tragedy_of_the_commons)
* [Point of Interest](https://en.wikipedia.org/wiki/Point_of_interest)
* [Proof of Activity](http://netecon.seas.harvard.edu/NetEcon14/Papers/Bentov_netecon14.pdf)
* [Cryptographic Hash Function](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
* [Garmin XML Schemas](https://www8.garmin.com/xmlschemas/index.jsp#/web/docs/xmlschemas)
* [GPS Exchange Format](https://en.wikipedia.org/wiki/GPS_Exchange_Format)

### Data Source / Activity Information Schema

#### Strava API References 

- [Strava Developers](https://developers.strava.com)
- [Strava API](https://www.strava.com/settings/api)
- [Getting Started Guide](https://developers.strava.com/docs/getting-started)
- [API Documentation](https://developers.strava.com/docs/reference)
- [Create & Manage Your App](https://strava.com/settings/api)
- [Explore the API Playground](https://developers.strava.com/playground)
- [Libraries](https://developers.strava.com/docs/#client-code)
- [/#api-Activities](http://developers.strava.com/docs/reference/#api-Activities)
- [/#api-Athletes](http://developers.strava.com/docs/reference/#api-Athletes)
- [/#api-Routes](http://developers.strava.com/docs/reference/#api-Routes)

- [Retrieve Activity Data](https://www.strava.com/activities/2744688834)
- [Export_GPX](https://www.strava.com/activities/2744688834/export_gpx)
- [Export_TCX](https://www.strava.com/activities/2744688834/export_tcx)
- [Share Activity Route](https://www.strava.com/routes/22211617)
- [Upload Strava activity (.tcx / .gpx / .fit)](https://support.strava.com/hc/en-us/articles/223297187-How-to-get-your-Activities-to-Strava).

#### Garmin Training Center XML Format - (.TCX / .GPX / .FIT) 

> - Training Center XML (TCX) is a data exchange format introduced in 2007 as part of Garmin's Training Center product. The XML is similar to GPX since it exchanges GPS tracks, but treats a track as an Activity rather than simply a series of GPS points. TCX provides standards for transferring heart rate, running cadence, bicycle cadence, calories in the detailed track. It also provides summary data in the form of laps.
> - [Training Center XML](https://en.wikipedia.org/wiki/Training_Center_XML)
> - [Garmin XML Schemas](https://www8.garmin.com/xmlschemas/)

### Technology Layers

| Blockchain   | Consensus Mechanism          | Link |
|:-------------|:-----------------------------|:-------|
| PoW          | Proof of Work                |  [Read](https://en.bitcoin.it/wiki/Proof_of_work)  |
| PoS          | Proof of Stake               |  [Read](https://en.bitcoin.it/wiki/Proof_of_Stake)  |
| DPoS         | Delegated Proof of Stake     |  [Read](https://docs.bitshares.org/en/master/technology/dpos.html)  |
| PoA          | Proof of Activity            |  [Read](https://eprint.iacr.org/2014/452.pdf)  |
| PoA          | Proof of Authority           |  [Read](https://en.wikipedia.org/wiki/Proof_of_authority)   |

* * *

### Sourcing Activity Data with Javascript

Exporting Activity Manually as (.TCX / .GPX)
* Source Activity Strava Profile
* https://www.strava.com/activities/2744688834
* Exporting Strava Activity in the .TCX format 
* https://www.strava.com/activities/2744688834/export_tcx
* Exporting Strava Activity in the .GPX format 
* https://www.strava.com/activities/2744688834/export_gpx

## Accessing Strava API

```bash
// Bashing cURL
curl -X GET "https://www.strava.com/api/v3/activities/2780342099?include_all_efforts=true" -H "accept: application/json" -H "authorization: Bearer cb5467187bfa67b219cb6359c0bb86a0499fccc3"
// Http Request 
$ http GET "https://www.strava.com/api/v3/activities/2780342099?include_all_efforts=" "Authorization: Bearer cb5467187bfa67b219cb6359c0bb86a0499fccc3"
```
* [$ http GET "https://www.strava.com/api/v3/activities/2780342099](./http_GET.md)
```
// Recommended to Build in Docker container 
```

## Docker Runtime Container

* Install Docker for MacOS
* Run Docker Pull Commands
```bash 
$ docker pull casperlabs/client
$ docker pull casperlabs/grpcwebproxy
$ docker pull casperlabs/node
$ docker pull casperlabs/execution-engine
$ docker pull casperlabs/client
```

## Key Value Storage

This is an example of a simple string-base key-value smart contract and it's usage.

## Requirements
#### Install Rust
```bash 
$ brew install rust
```

#### Install IPFS
```bash 
$ tar xvfz go-ipfs.tar.gz
$ cd go-ipfs
$ ./install.sh
```

#### Upload Data / Files to IPFS 
```bash
$ ipfs add Proof_of_Activity_as_a_Stake.gpx
$ added QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk Proof_of_Activity_as_a_Stake.gpx
```
# Usage

## Step 1 - Compile smart contracts.
```bash
$ cargo build --release
```

## Step 2 - Save value under a key.
Make sure to run scripts in the root directory!
```bash
$ ./scripts/put.sh "Activity Hash" "QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"
```

## Step 3 - Check the value.
```bash
$ ./scripts/get.sh "Activity Hash"
```
Value of the counter should be `QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk`.

## Step 4 - Update the value.
```bash
$ ./scripts/put.sh "Activity Hash" "QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk"
```

## Step 5 - Check the value again.
```bash
$ ./scripts/get.sh "Activity Hash"
```
Value of the counter should be `QmV65a2mcsNt7V4LDekgAtLaLn8Eptc9L9yKVH2XSYc6Fk`.

## GraphQL
You can check the value of the counter using devnet's GraphQL console:
https://devnet-graphql.casperlabs.io

Go to and then:

### Check latest block hash in 
```
query {
  dagSlice(depth: 1) {
      blockHash
  }
}
```

### Get public key of your account
```bash
$ cat keys/key.public.hex.key
```

### Check the counter value.
Put block hash under `blockHashBase16Prefix` and your public key under `keyBase`. Put your key in `pathSegments` like in the example.
```
query {
  globalState(
    blockHashBase16Prefix: "96720f16a215b5e55f1a7475256370f48efa932248b7bcd633d29413a5c1f033"
    StateQueries: [
      {
        keyType: Address
        keyBase16: "64d0c86f888e925731cae4398c6ea86d26a14e2574e70b36bd4eeaec3a292cde"
        pathSegments: ["answer"]
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


### Proof of Work - Blockchain Consensus Mechanism 
##### Block.js
```js
// Javascript code from [Block.js]
class Block {
    constructor(index, previousHash, timestamp, data, hash) {
        this.index = index;
        this.previousHash = previousHash.toString();
        this.timestamp = timestamp;
        this.data = data;
        this.hash = hash.toString();
    }
}
```
##### calculateHash.js
```js
// Javascript code from [calculateHash.js]
var calculateHash = (index, previousHash, timestamp, data) => {
    return CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
};
```
##### generateNextBlock.js
```js
// Javascript code from [generateNextBlock.js]
var generateNextBlock = (blockData) => {
    var previousBlock = getLatestBlock();
    var nextIndex = previousBlock.index + 1;
    var nextTimestamp = new Date().getTime() / 1000;
    var nextHash = calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData);
    return new Block(nextIndex, previousBlock.hash, nextTimestamp, blockData, nextHash);
};
```
##### blockchainarray.js
```js
// Javascript code from [blockchainarray.js]
var getGenesisBlock = () => {
    return new Block(0, "0", 1465154705, "my genesis block!!", "816534932c2b7154836da6afc367695e6337db8a921823784c14378abed4f7d7");
};

var blockchain = [getGenesisBlock()];
```
##### isValidNewBlock.js
```js
// Javascript code from [isValidNewBlock.js]
var isValidNewBlock = (newBlock, previousBlock) => {
    if (previousBlock.index + 1 !== newBlock.index) {
        console.log('invalid index');
        return false;
    } else if (previousBlock.hash !== newBlock.previousHash) {
        console.log('invalid previoushash');
        return false;
    } else if (calculateHashForBlock(newBlock) !== newBlock.hash) {
        console.log('invalid hash: ' + calculateHashForBlock(newBlock) + ' ' + newBlock.hash);
        return false;
    }
    return true;
};
```
##### replaceChain.js
```js
// Javascript code from [replaceChain.js]
var replaceChain = (newBlocks) => {
    if (isValidChain(newBlocks) && newBlocks.length > blockchain.length) {
        console.log('Received blockchain is valid. Replacing current blockchain with received blockchain');
        blockchain = newBlocks;
        broadcast(responseLatestMsg());
    } else {
        console.log('Received blockchain invalid');
    }
};
```
##### chain_http.js
```js
// Javascript code from [nativechain_http.js]
var initHttpServer = () => {
    var app = express();
    app.use(bodyParser.json());

    app.get('/blocks', (req, res) => res.send(JSON.stringify(blockchain)));
    app.post('/mineBlock', (req, res) => {
        var newBlock = generateNextBlock(req.body.data);
        addBlock(newBlock);
        broadcast(responseLatestMsg());
        console.log('block added: ' + JSON.stringify(newBlock));
        res.send();
    });
    app.get('/peers', (req, res) => {
        res.send(sockets.map(s => s._socket.remoteAddress + ':' + s._socket.remotePort));
    });
    app.post('/addPeer', (req, res) => {
        connectToPeers([req.body.peer]);
        res.send();
    });
    app.listen(http_port, () => console.log('Listening http on port: ' + http_port));
};
```

### Blockchain Diagram

![Blockchain](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Bitcoin_Transaction_Visual.svg/1200px-Bitcoin_Transaction_Visual.svg.png)

### About

<dl>
<dt>Project</dt>
<dd>Flowstake</dd>
<dt>Developed</dt>
<dd>2019</dd>
<dt>Location</dt>
<dd>Global</dd>
<dt>Contact</dt>
<dd>Flowstake@gmail.com</dd>
</dl>

```
Flowstake - 2019
```
