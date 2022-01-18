import json
import requests
import sys

#url = 'http://3.135.238.207:8080/api/v2/findings?limit=1000'
url = 'http://3.135.238.207:8080/finding?test_import_finding_action__test_import=&title=&component_name=&component_version=&date=&cve=&last_reviewed=&last_status_update=&mitigated=&test__engagement__version=&test__version=&status=&active=unknown&verified=unknown&duplicate=&is_mitigated=&out_of_scope=unknown&false_p=unknown&risk_accepted=unknown&has_component=unknown&has_notes=unknown&file_path=&unique_id_from_tool=&vuln_id_from_tool=&service=&param=&payload=&risk_acceptance=&has_finding_group=unknown&tags=&test__tags=147&test__engagement__tags=&test__engagement__product__tags=&tag=&not_tags=&not_test__tags=&not_test__engagement__tags=&not_test__engagement__product__tags=&not_tag=&o='

headers = {'content-type': 'application/json',
           'Authorization': 'Token 04a3f27e413800d03838d1d5ac9c5dcdb91e672b'}
r = requests.get(url, headers=headers, verify=True)# set verify to False if ssl cert is self-signed
#print (r.json())
#y=json.loads(r.json())
test_txt = r.json()
count=0
for i in range(len(test_txt['results'])):
 count+=1
 #print (test_txt['results'][i]['found_by'])

 if (test_txt['results'][i]['severity']) == 'High' or (test_txt['results'][i]['severity']) == 'Medium' and (test_txt['results'][i]['found_by']) == 19:

    print('severity is High/Medium so pipeline terminated')
    # print(count)
    exit(1)

 else:
    print('there are no high/medium found so pipeline continue' )
    continue

print(count)
