# CloudFlareDNSDump
[![Pylint](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/pylint.yml/badge.svg)](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/pylint.yml) 
[![CodeQL](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/codeql.yml/badge.svg)](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/codeql.yml) 
[![Bandit](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/bandit.yml/badge.svg)](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/bandit.yml) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://raw.githubusercontent.com/ob1lan/Abandoned_S3_Bucket_Takeover/main/LICENSE)
## Purpose
This Python script uses the CloudFlare API to first get all DNS zones IDs, and then export all DNS records for all zones.
## Usage
Simply clone this repo, install Pandas, add your API Authorization Bearer into the headers.txt file and then execute the script.
```shell
git clone https://github.com/ob1lan/CloudFlareDNSDump.git
pip install pandas
python cloudflare_dns_dumper.py
```
This will get through all the DNS zones you have access to, and then exports all (sub)domains into those files:
- results.json
- results.csv
## To Do
- Error handling and logging
