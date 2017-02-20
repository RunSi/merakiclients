# merakiclients

The object of this script is to retrieve from the Meraki Dashboard API
known clients from devices on a given network.

The Meraki Dashboard API key and the Network ID need to be added to the
meraki_ini.cnf file.

API KEY
In order to gain API access then on the Meraki Dashboard go to 
Organization settings and select API access at the bottom of the page.
Once activated got to 'My Profile'  Under API access select
'Generate API Key'


NETWORK ID
The code does not yet support the automatic retrieval of Network ID.
In order to obtain network ID either use curl on the command line or
Postman in order to retrieve.

Step 1
Retrieve Organization ID

curl -L -H 'X-Cisco-Meraki-API-Key:KEY’ -X GET -H 'Content-Type: application/json' 
'https://dashboard.meraki.com/api/v0/organizations'

With organization ID enter the following

curl -L -H 'X-Cisco-Meraki-API-Key:<KEY>’ -X GET -H 'Content-Type: application/json' 
'https://dashboard.meraki.com/api/v0/organizations/<ORG ID>/networks'

DEPENDENCIES
This script relies on several external modules to be installed on your Python 3.X
installation.

From pip install the following

Flask
Netaddr
Requests
