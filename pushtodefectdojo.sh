#!/bin/sh

time=$(date +'%Y-%m-%d')        
sudo curl --location --request POST 'http://52.14.192.9:8080/api/v2/import-scan/' \
--header 'Authorization: Token a1c2e4b944e0ba004336bccc9ec5dd2fcfdba1b2' \
--form 'engagement="2"' \
--form 'verified="true"' \
--form 'active="true"' \
--form 'lead="1"' \
#--form tags=$BUILD_NUMBER \
--form scan_date=$date \
--form 'scan_type="Detect-secrets Scan"' \
--form 'minimum_severity="Info"' \
--form 'skip_duplicates="true"' \
--form 'close_old_findings="false"' \
--form 'file=@"gitsecret_report.json"'

