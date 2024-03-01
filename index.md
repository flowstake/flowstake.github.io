### [FlowStake v1](https://flowstake.github.io/v1) + [Hashrun](https://flowstake.github.io/hashrun) - Activity Staking Blockchain Network

## Flowstake V2
* Proof of Activity Staking Network with Public, Immutable, Activity Records
* Data ownership, Hash addressed activity, Immutable records
* Hashed Timelock Smart Contracts
* Proof of Activity as Stake 

### Hashed Timelock Contract (HTLC) 
* Hashed Timelock Contract (HTLC) is a transactional agreement used to produce conditional payments. A payment wherein the receiver is required to acknowledge the receipt of payment before a predetermined time or a preset deadline.

### Threshold Signature
* Threshold cryptography, is a cryptosystem that protects information by encrypting it and distributing it among a cluster of fault-tolerant computers. The message is encrypted using a public key, and the corresponding private key is shared among the participating parties. With a threshold cryptosystem, in order to decrypt an encrypted message or to sign a message, several parties (more than some threshold number) must cooperate in the decryption or signature protocol.

### Threshold signature scheme (TSS)
* Threshold signature scheme is a method for generating a single digital signature from multiple signers.

### Hashed Timelock Contract + Threshold Signature (HTLC + TSS) 
* Hashed Timelock Activity Contract (HTLC) is a transactional agreement used to automatically unlock transfers via threshold signature. 

### Realtime Activity Data Capture

- Recording GPS trackpoints & accelerometer data from sensors on mobile & wearable devices (watches / rings).
- Parsing activity data into trackpoints with threshold signatures built on distributed encrypted ledgers.
- Staking proof of activity events into proof of activity HTLC smart contract with release of staked funds to prove consistent, reoccuring runtime / activity on timechain. 
- Each trackpoint is required to be consecutiveliy recorded & encrypted into trackpoints, attested in 1 minute segments
    * Analyzing data for Max Accel, Max Speed & Activity Duration

####  Proof of Activity as a Stake - Validators
    * To ensure network consensus & validation of activity data, each node must process transactions to secure network activity.
    * Activity timestamp hash verified on the blockchain network
    * Operate a validator node to stake the network 
    * Validator nodes verify proof of activity with attestation signature, timestamp validation / node validation, 

#### Hashing and Encrypting Activity Real Time
    - Requirements - Trackpoint Timestamp Data
    - Smart Contract - Mining Activity to Generate Blocks
        - Block Requirements for Sigining Activity Live - 1 min / 60 seconds - (60 tracepoints)
        - 1 Hour Validator - 1 hour / 60 mins / 3600 seconds (3,600 transactions)
        - 1 Day Validator - 24 hours / 1440 minutes / 86,400 seconds (86,400 transactions) 

### Requirements for Flowstake Smart Contracts
* Reputable Identity & Performance
* Identity Attestation 
    - Use ZK Proofs to Attest to Identity (Drivers License + Passport)
* Activity Attestation
   - Activity attestation, digital threshold signatures syncronized with validators nodes. 
* 1 Trackpoint per Second with 1:1 Sync recording at minimum of 1 TPS
   * GPS Trackpoints
   * Heartbeat Data
   * Proof of Activity Attestation Signature 

### Smart Contracts for Flowstake 
    - Stakeholders interacting with smart contract 
        - Flowstake - non-profit beneficiary of dontations
        - Donors - participants and contributors
        - Bridge - bridge data from GPS + attestation to smart contract
        - Hacker - malicious party

#### Smart Contract Lifecycle
    - Ongoing Activity:
    - Completed / Accomplished:
    - Failed:

##### Smart Contract State
    - Donations lock
        - Impossible for donor to send ETH to smart contract during on-going challenge.
    - Value lock
        - Impossible for Flowstake to withdraw all ETH after successful challenge, or withdraw individual donation after failed challenge
    - Theft
        - Impossible for the hacker to withdraw all the ETH after successful challenge or to withdraw individua donations after a failed challenge
    - Cheating 
        - Impossible for Flowstake, to with draw all the ETH donations if the challenge is not in a complete or failed state.
    - Failing update
        - Query the bridge, 
    - Failing database query from bridge

#### Theshold Signatures

Threshold signatures can be included in the code to facilitate group attestation by allowing multiple parties to jointly sign a message or data point. Here's how you can integrate threshold signatures into your code:

1. Choose a Threshold Signature Scheme: Threshold signature scheme that suits Flowstake  requirements and security considerations. There are various threshold signature schemes available, including BLS (Boneh-Lynn-Shacham) threshold signatures, ECDSA (Elliptic Curve Digital Signature Algorithm) threshold signatures, and Schnorr threshold signatures.

2. Implement Key Generation: Generate the necessary keys for the threshold signature scheme. This involves distributing shares of the private key among participating parties while retaining the public key. The key generation process should ensure that the threshold number of parties is required to reconstruct the private key.

3. Message Signing: When a message or data point needs to be signed for group attestation, the threshold signature algorithm is executed. Each party holding a share of the private key contributes to the signature generation process. The signature is produced without revealing individual private keys.

4. Signature Verification: The generated threshold signature can be verified using the corresponding public key. The verification process ensures that the signature is valid and authenticates the group attestation.

#### Here's a simplified example of how to implement threshold signatures using the BLS threshold signature scheme in JavaScript using the @chainsafe/bls library:

### [flowstake/bls](https://github.com/flowstake/bls)

```javascript 
const { SecretKey, PublicKey, Signature } = require('@chainsafe/bls');

// Number of parties required for threshold signature
const threshold = 3;

// Generate secret keys for each party
const secretKeys = [];
for (let i = 0; i < threshold; i++) {
    secretKeys.push(SecretKey.fromKeygen());
}

// Aggregate secret keys to create a master secret key
const masterSecretKey = SecretKey.aggregate(secretKeys);

// Derive the corresponding public key
const publicKey = masterSecretKey.toPublicKey();

// Simulate message to be signed
const message = 'Group attestation message';

// Generate individual signatures from each party
const signatures = secretKeys.map(secretKey => Signature.sign(message, secretKey));

// Aggregate signatures to create a threshold signature
const thresholdSignature = Signature.aggregate(signatures);

// Verify the threshold signature using the public key
const isValid = thresholdSignature.verify(message, publicKey);

console.log('Threshold Signature:', thresholdSignature.toString());
console.log('Signature Verification:', isValid ? 'Valid' : 'Invalid');
```

* This code snippet demonstrates the key generation, message signing, and signature verification process using BLS threshold signatures. You can adapt this implementation to suit your specific requirements and integrate it into your application for group attestation purposes.


### Theoretical Limitations of Performances 
* Running Speed & Acceleration
* Top speed of 43.99 kilometers per hour (27.33 miles per hour) Usain Bolt (2009) 
* Top speed of 10.44 meters per second 

**Top Speed** 
- In 2009 Jamaican sprinter Usain Bolt set the world record in the 100-meter sprint at 9.58 seconds. 
 Speed is the arate at which an object (or person) moves through time. It is represented mathematically s speed = d/t (in which d is distance and t is time). Bolt’s speed during his world-record run was 10.44 meters per second, 37.58 kilometers per hour or 23.35 miles per hour.
- In 2011 Belgian scientists used lasers to measure Bolt’s performance in the different stages of a 100-meter race held in September that year. They found that, 67.13 meters into the race, Bolt reached a top speed of 43.99 kilometers per hour (27.33 miles per hour).


### Sources 
**Theoretical Limitations of Performances**
- https://eprint.iacr.org/2023/598#:~:text=Threshold%20signatures%20protect%20the%20signing,if%20signers%20have%20different%20weights

- https://en.wikipedia.org/wiki/Public_key_infrastructure

- Thomas Vanderstraeten
testing-the-cryptorun-smart-contract-a-tale-of-obsessive-perfection-84ded25f1636

-------------------

## Flowstake V1
* Public, Immutable, Activity Records
* Public Activity Files Hashed into IPFS protocol
* Proof of Activity as Stake Consensus Mechanism
* Trustless, Geospatial, Smart Contracts

### Proof of Activity v1

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


Both GPX (GPS Exchange Format) and TCX (Training Center XML) are file formats commonly used in the context of GPS and fitness-related activities to store and exchange data. These formats are used to represent information about tracks, waypoints, routes, and other related data gathered during activities like running, cycling, hiking, or any other outdoor pursuits.

### GPX (GPS Exchange Format):
XML-based Format: GPX is an XML-based format, which means it uses a structured markup language to store data in a human-readable and machine-readable way.

Compatibility: GPX is widely supported by various GPS devices, applications, and online platforms. It has become a standard format for exchanging GPS data.

Data Types: GPX files can contain information about waypoints (specific locations), tracks (sequences of points that make up a route), and routes (predefined paths). It can also include additional data such as timestamps, elevation, and more.

Open Standard: GPX is an open standard, which means that the specifications for the format are publicly available. This openness promotes interoperability and compatibility across different systems.

Example:

xml
```bash
<gpx version="1.1" creator="Some Application">
  <trk>
    <name>Example Track</name>
    <trkseg>
      <trkpt lat="37.1234" lon="-122.5678">
        <ele>1000</ele>
        <time>2023-11-03T12:00:00Z</time>
      </trkpt>
      <!-- Additional track points go here -->
    </trkseg>
  </trk>
</gpx>
```

### TCX (Training Center XML):
Specifically Designed for Fitness Data: TCX is a proprietary XML-based format developed by Garmin specifically for storing fitness-related data. It is commonly used for activities such as running, cycling, and other workouts.

Data Types: TCX files focus on fitness-related data, including information about laps, heart rate, speed, cadence, and power. It's more tailored to the needs of athletes and fitness enthusiasts.

Compatibility: While TCX is widely supported by Garmin devices and software, it may not be as universally recognized as GPX. However, many fitness applications and platforms can import and export TCX files.

Example:

xml
```bash
<TrainingCenterDatabase>
  <Activities>
    <Activity Sport="Running">
      <Lap StartTime="2023-11-03T12:00:00Z">
        <TotalTimeSeconds>3600</TotalTimeSeconds>
        <!-- Additional lap data goes here -->
      </Lap>
    </Activity>
  </Activities>
</TrainingCenterDatabase>
```
In summary, GPX is a more generic and widely adopted format for GPS data exchange, while TCX is specifically designed for fitness-related activities with a focus on data commonly associated with workouts and training. The choice between the two depends on the devices and applications you are using and their compatibility with each format. Many platforms and tools support both formats, allowing users flexibility in choosing the one that best fits their needs.
