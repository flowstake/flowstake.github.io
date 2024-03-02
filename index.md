### [FlowStake v1](https://flowstake.github.io/v1) + [Hashrun](https://flowstake.github.io/hashrun) - Activity Staking Blockchain Network

## Flowstake V2
* Activity Staking Network with Public, Immutable, Activity Records
* Data ownership with Hash addressed activity
* Hashed Timelock Smart Contracts
* Proof of Activity as Stake 
* PoS Activity Ledger

Creating a proof of stake (PoS) activity ledger involves documenting the various transactions and activities within a PoS blockchain network. Below, is an outline simplified ledger format for tracking PoS activities:

### PoS Activity Ledger

1. **Date and Time:** Record the date and time of each activity.

2. **Block Number:** Specify the block number associated with the activity.

3. **Validator/Public Key:** Identify the validator or public key involved in the activity.

4. **Transaction Type:** Describe the type of transaction or activity. This could include:

* **Staking:** Depositing tokens into the PoS network for validation rights.
* **Reward Distribution:** Distributing rewards to validators for validating blocks.
* **Unstaking:** Withdrawing tokens from the PoS network.
* **Slashing:** Penalty for validators failing to follow the consensus rules.

5. **Transaction Details:**
* For staking: Record the amount of tokens staked.
* For reward distribution: Record the amount of rewards distributed.
* For unstaking: Record the amount of tokens unstaked.
* For slashing: Record the penalty amount.

6. **Validator Status:** Indicate the status of the validator after the activity.
* **Active:** Validator is actively participating in block validation.
* **Inactive:** Validator is temporarily inactive, perhaps due to unstaking or penalties.
* **Slashed:** Validator has been penalized for malicious behavior.

7. **Remarks/Notes:** Include any additional information or notes regarding the transaction or validator status. 

### Sample PoS Activity Ledger:

| Date & Time       |	Block Number  |	Validator/Public Key |	Transaction Type      |	Transaction Details	     | Validator Status   |	Remarks/Notes            |
|:------------------|:----------------|:---------------------|:-----------------------|:-------------------------|:-------------------|:-------------------------|
| 2024-03-01 12:00  |	10567	      | ABC123...            | Staking	              | 1000 FST tokens	         |     Active	      | Staked by Validator 1    |
| 2024-03-02 08:30  |	10580	      | XYZ789...            | Reward Distribution	  | 50 FST tokens	         |     Active	      | Rewards for Block 10568  |
| 2024-03-03 10:45  |	10600	      | DEF456...            | Unstaking	          | 500 FST tokens	         |     Inactive	      | Unstaked by Validator 2  |
| 2024-03-05 14:20  |	10610	      | GHI789...            | Slashing	              | 20 FST tokens	         |     Slashed	      | Penalty for Validator 3  |

* This ledger format helps to maintain a transparent record of PoS activities, including staking, rewards, unstaking, and slashing, providing insights into the network's operation and validator behavior. Additionally, it facilitates auditing and analysis of the PoS blockchain network.

### Hashed Timelock Contract (HTLC) 
* Hashed Timelock Contract (HTLC) is a transactional agreement used to produce conditional payments. A payment wherein the receiver is required to acknowledge the receipt of payment before a predetermined time or a preset deadline.

### Threshold Signature
* Threshold cryptography, is a cryptosystem that protects information by encrypting it and distributing it among a cluster of fault-tolerant computers. The message is encrypted using a public key, and the corresponding private key is shared among the participating parties. With a threshold cryptosystem, in order to decrypt an encrypted message or to sign a message, several parties (more than some threshold number) must cooperate in the decryption or signature protocol.

### Threshold signature scheme (TSS)
* Threshold signature scheme is a method for generating a single digital signature from multiple signers.

### Hashed Timelock Contract + (HTLC) 
* Hashed Timelock Activity Contract (HTLC) is a transactional agreement used to automatically unlock transfers via threshold signature. 

#### **Validators** - Proof of Activity as a Stake
* Validators - To ensure network consensus & validation of activity data, each node must process transactions to secure network activity.
    * Activity timestamp hash verified on the blockchain network
    * Operate a validator node to stake the network 
    * Validator nodes verify proof of activity with attestation signature, timestamp validation / node validation

#### Hashing and Encrypting Activity Real Time
* Requirements - Trackpoint Timestamp Data
    * Attesting Activity to Generate Blocks
    * Block Requirements for Signing Activity Live
        * 1 min / 60 seconds - (60 trackpoints)
        * 1 Hour Validator - 1 hour / 60 mins / 3600 seconds (3,600 timestamp signatures)
        * 1 Day Validator - 24 hours / 1440 minutes / 86,400 seconds (86,400 timestamp signatures) 

### Requirements for Flowstake Smart Contracts
* Proof of Identity Attestation / Validation
    * Use ZK Proofs to Attest to Identity for Activities (Drivers License + Passport)
* Proof of Activity Attestation
    * Activity attestation, digital threshold signatures syncronized with validators nodes. 
* 1 Trackpoint per Second with 1:1 Sync recording at minimum of 1 TPS
   * GPS Trackpoints
   * Heartbeat Data
   * Proof of Activity Attestation Signature 

### Smart Contracts for Flowstake 
* Stakeholders interacting with smart contract 
    * Flowstake - non-profit organization beneficiary of donations
    * Renat     - developer and deployer of smart contract, running the flowstake challenge
    * Donors    - participants and contributors
    * Oracle    - bridge data from GPS + attestation to smart contract
    * Hacker    - malicious party

#### Smart Contract Lifecycle
* Lifecycle of the smart contract along its states. This type of application is known as a state machine: it moves from one state to the next, with specific actions being possible only at certain states. The allowed states are the following:
* **Ongoing Activity:** the contract is open to all donations, while Flowstake and Party public state the challenge.
* **Completed / Accomplished:** the smart contract learned from the Oracle that Party successfully ran the challenge. Flowstake can thus withdraw all donations. No additional donations are possible. This is the end state of the smart contract if the challenge is not successful.
* **Failed:**  the smart contract learned from the Oracle that Party did not manage to run the challenge. Donors can withdraw their donations. This is the end state of the smart contract if the challenge is not successful.

The state transitions are triggered via a call to the Oracle (leading to accomplished or failed state), and Flowstake to close the challenge after donations have been withdrawn.

#### Smart Contract State
* Donations lock
    * Impossible for donor to send ETH to smart contract during on-going challenge.
* Value lock
    * Impossible for Flowstake to withdraw all ETH after successful challenge, or withdraw individual donation after failed challenge
* Theft
    * Impossible for the hacker to withdraw all the ETH after successful challenge or to withdraw individua donations after a failed challenge
* Cheating 
    * Impossible for Flowstake, to with draw all the ETH donations if the challenge is not in a complete or failed state.
* Failing update smart contract state
    * Contract failed to update state
* Query the Oracle, 
    * Failing database query from oracle

#### Theshold Signatures

Threshold signatures can be included in the code to facilitate group attestation by allowing multiple parties to jointly sign a message or data point. Here's how you can integrate threshold signatures into your code:

1. **Choose a Threshold Signature Scheme:** Threshold signature scheme that suits Flowstake  requirements and security considerations. There are various threshold signature schemes available, including BLS (Boneh-Lynn-Shacham) threshold signatures, ECDSA (Elliptic Curve Digital Signature Algorithm) threshold signatures, and Schnorr threshold signatures.

2. **Implement Key Generation:** Generate the necessary keys for the threshold signature scheme. This involves distributing shares of the private key among participating parties while retaining the public key. The key generation process should ensure that the threshold number of parties is required to reconstruct the private key.

3. **Message Signing:** When a message or data point needs to be signed for group attestation, the threshold signature algorithm is executed. Each party holding a share of the private key contributes to the signature generation process. The signature is produced without revealing individual private keys.

4. **Signature Verification:** The generated threshold signature can be verified using the corresponding public key. The verification process ensures that the signature is valid and authenticates the group attestation.


### [flowstake/bls](https://github.com/flowstake/bls)

#### Here's a simplified example of how to implement threshold signatures using the BLS BLS (Boneh-Lynn-Shacham) threshold signature scheme in JavaScript using the @chainsafe/bls library:

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


### Data Oracle - For example .TCX files from Strava

Using IPFS (InterPlanetary File System) for hash-addressable content to record .TCX files from Strava is a viable option for ensuring data integrity and decentralized storage. Here's how you can go about it:

#### What is IPFS?
IPFS is a distributed system for storing and accessing files, websites, applications, and data. It works by creating a peer-to-peer network where each node stores a collection of hashed files. This means that files are addressed by their content, not by their location.

### Recording .TCX Files from Strava on IPFS:

#### 1. Generate .TCX Files from Strava:
Strava provides an API that allows you to fetch activity data, including .TCX files, for individual workouts. You would need to authenticate your requests using OAuth 2.0 and then use the appropriate endpoints to download the .TCX files for the desired activities.

#### 2. Install IPFS:
You'll need to install IPFS on your local machine or set up a node on a server. IPFS provides instructions for installation and configuration on their website.

#### 3. Add .TCX Files to IPFS:
Once you have the .TCX files downloaded, you can add them to IPFS using the **ipfs add** command. This command will generate a unique hash for each file and store it in the IPFS network.

```bash
ipfs add file.tcx
```

#### 4. Record Hashes:
Store the hashes generated by IPFS along with relevant metadata such as the activity type, date, and any other information you want to associate with the activity.

#### 5. Distribute Hashes:
You can then distribute these hashes through various means, such as storing them in a database, publishing them on a website, or sharing them through social media.

#### 6. Accessing .TCX Files:
To access the .TCX files stored on IPFS, users can use the hash provided to retrieve the content through IPFS gateways or by running their own IPFS node.

Benefits of Using IPFS:
* Decentralization: IPFS removes the reliance on centralized servers, making data more resilient and censorship-resistant.
* Data Integrity: Files stored on IPFS are immutable and tamper-evident since any change to the file content would result in a different hash.
* Content Addressing: Files are addressed by their content, meaning you can always retrieve the correct file as long as you have its hash.
* By using IPFS to record .TCX files from Strava, you ensure that your workout data is securely stored, easily accessible, and resistant to censorship or data tampering.

#### JSON Flowstake file format
* The .TCX file format used by Strava for activity data can be converted into JSON format. Here's a simplified example of how you might structure the data in JSON:
```JSON
{
  "activity": {
    "id_hash": "1234567890",
    "type": "running",
    "start_time": "2024-01-28T08:00:00",
    "total_time_seconds": 3600,
    "distance_meters": 10000,
    "calories": 500,
    "track_points": [
      {
        "time": "2024-01-28T08:00:00",
        "latitude": 40.7128,
        "longitude": -74.0060,
        "elevation": 10,
        "heart_rate": 150,
        "cadence": 160
      },
      {
        "time": "2024-01-28T08:05:00",
        "latitude": 40.7129,
        "longitude": -74.0061,
        "elevation": 15,
        "heart_rate": 155,
        "cadence": 162
      },
      ...
    ]
  }
}
```

### **Parse this .tcx file into JSON schema
* This JSON structure represents an activity with various attributes such as ID, type, start time, total time, distance, calories burned, and an array of track points with their respective data including time, latitude, longitude, elevation, heart rate, and cadence.

* To parse the .TCX file and extract relevant data points to populate this JSON structure. Depending on the complexity of your TCX file, you might need to handle additional attributes or nested structures.

* Parsing a .tcx file into JSON involves extracting relevant information from the XML-based .tcx format and converting it into a JSON structure. Here's a simplified example of how you might accomplish this using Python and the xml.etree.ElementTree module:

```python
import xml.etree.ElementTree as ET
import json

def parse_tcx_to_json(tcx_file):
    tree = ET.parse(tcx_file)
    root = tree.getroot()

    # Initialize dictionary to hold parsed data
    tcx_data = {
        "activity": {
            "id": root.find(".//Id").text,
            "type": root.find(".//Activity").attrib.get("Sport"),
            "track_points": []
        }
    }

    # Parse trackpoints
    trackpoints = root.findall(".//Trackpoint")
    for trackpoint in trackpoints:
        tp_data = {
            "time": trackpoint.find(".//Time").text,
            "position": {
                "latitude": float(trackpoint.find(".//LatitudeDegrees").text),
                "longitude": float(trackpoint.find(".//LongitudeDegrees").text),
                "elevation": float(trackpoint.find(".//AltitudeMeters").text)
            }
        }

        # Optional: Parse heart rate and cadence if available
        heart_rate = trackpoint.find(".//HeartRateBpm")
        if heart_rate is not None:
            tp_data["heart_rate"] = int(heart_rate.find(".//Value").text)

        cadence = trackpoint.find(".//Cadence")
        if cadence is not None:
            tp_data["cadence"] = int(cadence.text)

        tcx_data["activity"]["track_points"].append(tp_data)

    return tcx_data

if __name__ == "__main__":
    tcx_file = "your_tcx_file.tcx"
    json_data = parse_tcx_to_json(tcx_file)

    # Dump JSON data to a file
    with open("output.json", "w") as json_file:
        json.dump(json_data, json_file, indent=4)
```
* This script reads the .tcx file, extracts relevant data such as activity ID, type, trackpoints (including time, position, heart rate, and cadence if available), and structures it into a JSON format. Ensure you replace "your_tcx_file.tcx" with the path to your actual .tcx file.

* This code is a basic example and may need modifications depending on the structure of your .tcx file and the specific data you want to extract. Additionally, error handling and more complex parsing might be necessary for real-world applications.



### Extra Resources & Concepts

#### Theoretical Limitations of Performances 
* Running Speed & Acceleration
* Top speed of 43.99 kilometers per hour (27.33 miles per hour) Usain Bolt (2009) 
* Top speed of 10.44 meters per second 

##### Top Speed
* In 2009 Jamaican sprinter Usain Bolt set the world record in the 100-meter sprint at 9.58 seconds. 
 Speed is the arate at which an object (or person) moves through time. It is represented mathematically s speed = d/t (in which d is distance and t is time). Bolt’s speed during his world-record run was 10.44 meters per second, 37.58 kilometers per hour or 23.35 miles per hour.
* In 2011 Belgian scientists used lasers to measure Bolt’s performance in the different stages of a 100-meter race held in September that year. They found that, 67.13 meters into the race, Bolt reached a top speed of 43.99 kilometers per hour (27.33 miles per hour).

* Reputation Identity / Activity System

### Sources 

[Testing the Cryptorun smart contract: a tale of obsessive perfection](https://medium.com/@vanderstraeten.thomas/testing-the-cryptorun-smart-contract-a-tale-of-obsessive-perfection-84ded25f1636)
- [Threshold Signatures](https://eprint.iacr.org/2023/598#:~:text=Threshold%20signatures%20protect%20the%20signing,if%20signers%20have%20different%20weights)
- [Public Key Infastructure](https://en.wikipedia.org/wiki/Public_key_infrastructure)

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
