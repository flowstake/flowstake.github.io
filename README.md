### FlowStake / Hashrun - Activity Staking Blockchain Network
* Public, Immutable, Activity Records
* Public Activity Files Hashed into IPFS protocol
* Proof of Activity as Stake Consensus Mechanism
* Hybrid Proof of Stake / Proof of Activity

IPFS protocol generates secure & reliable records for proof of activity.
Compiling trackpoints of GPS & accelerometer data from sensors on mobile & wearable devices.
Parsing activity data into distributed encrypted ledgers with Blockchain technology.

Proof of Activity Smart Contract - Staking proof of activity events into escrow smart contracts with time based release to prove consistent, recoccuring runtime / activity on timechain. Trackpoint metrics analyze 1 minute segments - analyzing data for Max Accelration, Max Speed & Activity Duration

-  Proof of Activity as a Stake - Validators
    * To ensure network consensus & valid activity data, each node must process transactions to secure network activity.
    * Activity timestamp hash verified on the blockchain network
    * Operate a validator node to stake the network 
    * Validator nodes verify proof of activity IPFS timestamps

- Mining and Encrypting Activity Real Time
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
    
    
## Resources - Development Tools

### Docker Runtime Container

* Install [Docker for MacOS](https://docs.docker.com/docker-for-mac/install/)
* Docker Pull Commands
$ docker pull casperlabs/client
$ docker pull casperlabs/buildenv
$ docker pull casperlabs/grpcwebproxy
$ docker pull casperlabs/node
$ docker pull casperlabs/execution-engine
$ docker pull casperlabs/explorer
$ docker pull casperlabs/key-generator

### Strava API - https://www.strava.com/settings/api
    
#### Local Installation - macOS Mojave 10.14.4
On macOS, HTTPie can be installed via Homebrew (recommended):

* $ brew install httpie
==> Downloading https://homebrew.bintray.com/bottles/httpie-1.0.3.mojave.bottle.tar.gz
==> Downloading from https://akamai.bintray.com/24/2436432e8ee1efe7f6c19c501af35aba453dabe3b9a9f88bed4e22a795bc6d1c?__gda__=exp
######################################################################## 100.0%
==> Pouring httpie-1.0.3.mojave.bottle.tar.gz
🍺  /usr/local/Cellar/httpie/1.0.3: 946 files, 11.0MB

Below is an example request to the Strava API using HTTPie, along with sample response headers for a successful and rate-limited request:

Example request

$ http 'https://www.strava.com/api/v3/athlete' \
    'Authorization:Bearer d4cc0724eed83ffddcb8715d7fd83d3588724cc5'
 
HTTP/1.1 200 OK
Cache-Control: max-age=0, private, must-revalidate
Connection: keep-alive
Content-Encoding: gzip
Content-Type: application/json; charset=utf-8
Date: Tue, 15 Oct 2019 05:06:16 GMT
ETag: W/"4c2a3238f8480def275c8d6b6633bf4d"
Referrer-Policy: strict-origin-when-cross-origin
Status: 200 OK
Transfer-Encoding: chunked
Vary: Origin
Via: 1.1 linkerd
X-Content-Type-Options: nosniff
X-Download-Options: noopen
X-FRAME-OPTIONS: DENY
X-Permitted-Cross-Domain-Policies: none
X-RateLimit-Limit: 600,30000
X-RateLimit-Usage: 1,1
X-Request-Id: 595c898e-dd45-47b6-b310-576be98dd2a9
X-XSS-Protection: 1; mode=block

{
    "badge_type_id": 0,
    "city": "Providence",
    "country": "United States",
    "created_at": "2015-09-19T03:59:51Z",
    "firstname": "Renat",
    "follower": null,
    "friend": null,
    "id": 11405488,
    "lastname": "Razumov",
    "premium": false,
    "profile": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/11405488/3777188/5/large.jpg",
    "profile_medium": "https://dgalywyr863hv.cloudfront.net/pictures/athletes/11405488/3777188/5/medium.jpg",
    "resource_state": 2,
    "sex": "M",
    "state": "Rhode Island",
    "summit": false,
    "updated_at": "2019-10-15T02:26:50Z",
    "username": null
}

    
Resources - Development Tools  Example Activity w/ Heatbeat Data 
* Strava API - https://www.strava.com/settings/api
* Retrieve Activity Data - https://www.strava.com/activities/2744688834
* Export GPX - https://www.strava.com/activities/2744688834/export_gpx
* Export TCX - https://www.strava.com/activities/2744688834/export_tcx
* Share Activity Route - https://www.strava.com/routes/22211617
* IPFS Hash  QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd
* IPFS.io - https://ipfs.io/ipfs/QmPfUsyaYuQpDfXKUeHczn7wZ5MUWrDDmQVwsBvVKFamnd
* PHP Library for parsing running GPS activities (.TCX .GPX .PWX .CSV) - https://github.com/flowstake/Waddle
* CasperLabs - http://devnet-graphql.casperlabs.io:40403/graphql
* GraphQL - https://graphql.org/learn

Concepts
* Point of Interest - https://en.wikipedia.org/wiki/Point_of_interest
* Proof of Activity - http://netecon.seas.harvard.edu/NetEcon14/Papers/Bentov_netecon14.pdf
* Cryptographic Hash Function - https://en.wikipedia.org/wiki/Cryptographic_hash_function
* Garmin XML Schemas https://www8.garmin.com/xmlschemas/index.jsp#/web/docs/xmlschemas
* GPS Exchange Format - https://en.wikipedia.org/wiki/GPS_Exchange_Format
