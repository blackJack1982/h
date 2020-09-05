
  # Replace YOUR_WEB_URL with the URL of a website you own or control

import requests
 
response = requests.get('YOUR_WEB_URL')
 
if(response.status_code == 200):
  response = requests.get('YOUR_WEB_URL/admin.php')
  print('Request success!')
 
  if(response.status_code == 200):
    print('Vulnerable site')
  else:
    print('Not a vulnerable site')
else:
  print('Request failure')
  
# Remediation: honeypots (trap => cataloguing or disabling via invalid data/redirection/reverse attack);firewall with a delibarate slowdown;
# message and traffic masking (e.g. nginx instead of apache) => make sure on legimate use does not get hammered by illegitimate use;
# target testing tools
