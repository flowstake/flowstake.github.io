---
layout: default
---

## Flowstake - Blockchain Activity Network

> - Stake activity transactions on the Flowstake blockchain

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

### Blockchain Consensus Mechanism 

```js
// Javascript code from ### Block.js
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

```js
// Javascript code from ### calculateHash.js 
var calculateHash = (index, previousHash, timestamp, data) => {
    return CryptoJS.SHA256(index + previousHash + timestamp + data).toString();
};
```

```js
// Javascript code from ### generateNextBlock.js 
var generateNextBlock = (blockData) => {
    var previousBlock = getLatestBlock();
    var nextIndex = previousBlock.index + 1;
    var nextTimestamp = new Date().getTime() / 1000;
    var nextHash = calculateHash(nextIndex, previousBlock.hash, nextTimestamp, blockData);
    return new Block(nextIndex, previousBlock.hash, nextTimestamp, blockData, nextHash);
};
```

* * *

### Blockchain Diagram

![Blockchain](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Bitcoin_Transaction_Visual.svg/1200px-Bitcoin_Transaction_Visual.svg.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### About

<dl>
<dt>Project</dt>
<dd>Flowstake</dd>
<dt>Developed</dt>
<dd>2019</dd>
<dt>Location</dt>
<dd>Global</dd>
</dl>


```
Flowstake - 2019
```
