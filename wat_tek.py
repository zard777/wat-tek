##
### 
####
print '                   __               __          __        '
print '  __  _  _______ _/  |_           _/  |_  ____ |  | __    '
print '  \ \/ \/ /\__  \     _\  ______  \   __\/ __ \|  |/ /    '
print '   \     /  / __ \|  |   /_____/   |  | \  ___/|    <     '
print '    \/\_/  (____  /__|             |__|  \___  >__|_ \    '
print '                \/                           \/     \/    '
print '                                                          '
print '                                            Version: 0.7  '
print '                                       Author: @zard_sec  '
####
#####


#!/usr/bin/env python 
import sys, time, json, requests

print '==============================================================='

raw_domain = raw_input("Input domain (example: google.com): ")

print '\n[+] Make HTTP REQUEST'
response = requests.post('https://www.purplemet.com/api/analysis', 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded'

    },
    cookies={

    },
    data='url=http://'+raw_domain
    
) 

obj = json.dumps(response.json())
#demo = json.dumps(obj)
#print obj 

task_id = json.loads(obj)['task']

t_sleep = 5 

print '\n[+] Waiting for query.. '


ask_status = 'RUNNING'
flag = True 

while (flag):  
    r = requests.get('https://www.purplemet.com/api/analysis/'+task_id)
    check_status = json.loads(r.content)['status']
    if check_status == 'DONE': 
        break
    t_sleep += 5 



#print 'Make HTTP GET to query the previous task'

print '\n[+] Result \n'
print r.content

 
#if (json.loads(r.content)['msg'] != 'Collecting data...')
#print r.content
#else 



