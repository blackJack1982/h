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
  
  # Replace YOUR_WEB_URL with the URL of a website you own or control
