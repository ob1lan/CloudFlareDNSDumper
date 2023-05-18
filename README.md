# CloudFlareDNSDump
[![Pylint](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/pylint.yml/badge.svg)](https://github.com/ob1lan/CloudFlareDNSDumper/actions/workflows/pylint.yml)
## Purpose
This Python script uses the CloudFlare API to first get all DNS zones IDs, and then export all DNS records for all zones.
## Usage
Simply clone this repo, install Pandas, add your API Authorization Bearer into the headers.txt file and then execute the script.
```shell
git clone https://github.com/ob1lan/CloudFlareDNSDump.git
pip install pandas
python cloudflare_dns_dumper.py
```
## To Do
- Error handling and logging
