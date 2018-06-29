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
print '                                            Version: 0.5  '
print '                                       Author: @zard_sec  '
####
#####



#!/usr/bin/env python 
import time, json, requests

# Original form >> curl 'https://www.purplemet.com/api/analysis' -H 'origin: https://www.purplemet.com' -H 'accept-encoding: gzip, deflate, br' -H 'accept-language: en-US,en;q=0.9' -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36' -H 'content-type: application/x-www-form-urlencoded; charset=UTF-8' -H 'accept: */*' -H 'referer: https://www.purplemet.com/' -H 'authority: www.purplemet.com' -H 'x-requested-with: XMLHttpRequest' -H 'dnt: 1' --data 'url=http://fb.com' --compressed

# Query result >> curl https://www.purplemet.com/api/analysis/d12ed580-760d-11e8-b324-5908eea5870b

# Shorter form >> curl 'https://www.purplemet.com/api/analysis' -H 'x-requested-with: XMLHttpRequest' --data 'url=http://fb.com' --compressed

print '==============================================================='
print 'Input domain'
#dom = raw_input("Please input the domain to query: ")

#print 'Make HTTP REQUEST to PurpleMet API'
response = requests.post('https://www.purplemet.com/api/analysis', 
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded'

    },
    cookies={

    },
    data='url=http://fb.com'
    #data=dom

) 

obj = json.dumps(response.json())
#demo = json.dumps(obj)
print obj 

task_id = json.loads(obj)['task']

#print 'Task[\'1\'] =', task_id['task']
print '\nWaiting for query.. \n' 
time.sleep(10)

#print 'Make HTTP GET to query the previous task'

r = requests.get('https://www.purplemet.com/api/analysis/'+task_id)
print r.content

#retry_limit = 5




