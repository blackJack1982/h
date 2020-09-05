# potential steps: logs, internet history, phones (location history etc.), hard drives (recovery if erased?), memory (RAM) => analysis and recovery.

import hashlib
 
file1 = open('oldfile.txt','r').read().strip().strip('-').encode('utf-8')
file2 = open('newfile.txt','r').read().strip().strip('-').encode('utf-8')
 
hash1 = hashlib.md5(file1).hexdigest()
hash2 = hashlib.md5(file2).hexdigest()
 
if(hash1 == hash2):
  print('Duplicate file found!')
else:
  print('The file is not a match')
 
 


oldfile.txt

No one will find this


newfile.txt

----No one will find this----


# Remediation: regular backups, audit trails (reports), access logging
