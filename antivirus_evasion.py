# normally, antivirus seek for patterns/signatures in the binary/data files; evasion is done via:
# obfuscation (desguising code: sifting bits, changing order the things are evaluated: no pattern to be detectable by antivirus)
# compression (turning a smth into a different format so the antivirus is not looking for a compressed verion of it)
# encoding

import base64
 
# Writing the file
bytes = bytearray("print(dict(__import__('os').environ))",'utf-8')
 
base64string = base64.b64encode(bytes)
 
f = open('harmless.py','w')
 
f.write(base64string.decode('utf-8'))
 
 
# Reading the file
f = open('harmless.py', 'r')
 
eval(base64.b64decode(f.readline()).decode('utf-8'))

# Remediation: updated definition (e.g. signatures), no only antivirus (combo of logging/monitoring/alerting/firewall/physical security)
