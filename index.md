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
* [CasperLabs Explorer] - https://explorer.casperlabs.io/#/explorer
* [GraphQL] - https://graphql.org/

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

- [developers.strava](http://developers.strava.com/docs/reference/)
- [/#api-Activities](http://developers.strava.com/docs/reference/#api-Activities)
- [/#api-Athletes](http://developers.strava.com/docs/reference/#api-Athletes)
- [/#api-Routes](http://developers.strava.com/docs/reference/#api-Routes)
- [Strava API](https://www.strava.com/settings/api)
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

### Sourcing Activity Data
// Javascript GET /activities/{id}
```js
var StravaApiV3 = require('strava_api_v3');
var defaultClient = StravaApiV3.ApiClient.instance;

// Configure OAuth2 access token for authorization: strava_oauth
var strava_oauth = defaultClient.authentications['strava_oauth'];
strava_oauth.accessToken = "YOUR ACCESS TOKEN"

var api = new StravaApiV3.ActivitiesApi()

var id = 789; // {Long} The identifier of the activity.

var opts = { 
  'includeAllEfforts': true // {Boolean} To include all segments efforts.
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.getActivityById(id, opts, callback);
```
#### Source Activity Strava Profile
* https://www.strava.com/activities/2744688834
#### Exporting Strava Activity in the .TCX format 
* https://www.strava.com/activities/2744688834/export_tcx
#### Exporting Strava Activity in the .GPX format 
* https://www.strava.com/activities/2744688834/export_gpx

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
