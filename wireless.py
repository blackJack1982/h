

from subprocess import call
 
call(['/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport','-s'])
 
# For Linux
# You will have to run your python command with sudo
# call(['iwlist', 'wlan0', 'scan'])



# Rogue Access Point to look into

#Remediation: No advertising SSID(weak, yet a part), Isolated Networks, Change of Default Configuration (! ==> trafic sniffing, compromising etc.)
# address filtering or authorized machines only(MAC), WPA2 (protocol for credentials check) 
