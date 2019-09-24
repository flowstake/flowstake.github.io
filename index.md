---
layout: default
---

## Flowstake - Blockchain Activity Network

> - Proof of Activity transactions on the Flowstake blockchain
> - [github.com/flowstake](https://github.com/flowstake)

## Activity Consensus Mechanism
 
- Mechanism for data analysis & activity validation. 
- Blockchain network to generating Proof of Activity transactions.
- [Upload Strava activity (.tcx / .gpx / .fit)](https://support.strava.com/hc/en-us/articles/223297187-How-to-get-your-Activities-to-Strava).


## Proof of Activity as Stake

> - Utilizing Blockchain technology to create a record of activity.
> - Proof of Activity as Stake - validate, sign & activity transactions.
> - Generate block rewards for 'mining' activity. 


### Problem to Solve

*   Validate identity, record activity & upload activity metrics. 
*   Generate digital transaction & sync activity metrics into blockchain.
*   Staking contract for verified activity via smart contract.


### Technology Layers

| Blockchain   | Consensus Mechanism          | Link |
|:-------------|:-----------------------------|:-------|
| PoW          | Proof of Work                |  [Read](https://en.bitcoin.it/wiki/Proof_of_work)  |
| PoS          | Proof of Stake               |  [Read](https://en.bitcoin.it/wiki/Proof_of_Stake)  |
| DPoS         | Delegated Proof of Stake     |  [Read](https://docs.bitshares.org/en/master/technology/dpos.html)  |
| PoA          | Proof of Activity            |  [Read](https://eprint.iacr.org/2014/452.pdf)  |
| PoA          | Proof of Authority           |  [Read](https://en.wikipedia.org/wiki/Proof_of_authority)   |

* * *

### Blockchain Proof of Work Consensus Mechanism 
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
#### replaceChain.js
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
#### chain_http.js
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
