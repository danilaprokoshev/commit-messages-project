import json

c_data_file = open('flask_commit_messages.json')
c_data = json.load(c_msgs_file)
c_data_file.close()

for commit in c_data:
    print(commit['subject'])

s = 'please answer my question'
if len(s) <= 50:
    print 'Good summary line'
else:
    print 'Summary line length may be less'

import re

for i, line in enumerate(content):
    print line if not (re.match('\r?\n', line)) else pass

if line in ['\n', '\r\n']:
    print 'Blank line is here, good'
else:
    print 'There is no blank line'
    
p = re.compile('[a-zA-z]*ed')
m = p.match(commit)
print m
if m:
    print "It's no good"

