#!/usr/bin/env python3
"""Uses the CloudFlare API to export all DNS records (domains & subdomains) for all zones.

Usage:
    ./cloudflare_dns_dumper.py

Author:
    Ob1lan - 09-MAY-2023
"""

import http.client
import json
import pandas as pd


# Create the connection object to CF API
conn = http.client.HTTPSConnection("api.cloudflare.com")

# Connection headers containing the credentials
with open('headers.txt', encoding="utf-8") as f:
    data = f.read()
    headers = json.loads(data)

# Request for the Zones
conn.request("GET", "/client/v4/zones", headers=headers)
res = conn.getresponse().read().decode("utf-8")
zones = [json.loads(res)]

# Create the empty dict object for the zone IDs
arrayzoneids = []

# Loop into the zones to get their IDs
for item in zones:
    results = item['result']
    for result in results:
        arrayzoneids.append(result['id'])

# Create the empty dict object for the records
arrayrecords = []

# Use every zone ID to get their DNS records into the dict
for item in arrayzoneids:
    conn.request("GET", "/client/v4/zones/" + item + "/dns_records", headers=headers)
    res = conn.getresponse().read().decode("utf-8")
    zonecontent = [json.loads(res)]
    for results in zonecontent:
        records = results['result']
        for element in records:
            record = {"type": element['type'], "name": element['name'], "value": element['content']}
            arrayrecords.append(record)

# Convert the dict object into a JSON object
jsonData = json.dumps(arrayrecords)

# Export results into JSON
with open("results.json", "w", encoding="utf-8") as outfile:
    outfile.write(jsonData)

# Export results into CSV
# df = pd.read_json(jsonData)
df = pd.DataFrame(data=pd.read_json(jsonData))
df.to_csv('results.csv', index=False)
