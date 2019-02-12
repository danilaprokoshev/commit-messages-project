import json
import re

c_data_file = open('flask_commit_messages.json')
c_data = json.load(c_data_file)
c_data_file.close()


count_length = 0.00
count_length_over50 = 0.00
for commit in c_data:
    print(commit['subject'])
    if len(commit['subject']) <= 50:
        count_length += 1
    else:
        count_length_over50 += 1

print "Percentage of good subject's length: ", count_length / (count_length + count_length_over50) * 100
print "Percentage of bad subject's length: ", count_length_over50 / (count_length + count_length_over50) * 100


count_capit = 0.00
count_not_capit = 0.00
for commit in c_data:
    if (commit['subject'])[0].isupper():
        count_capit += 1
    else:
        count_not_capit += 1

print "Percentage of subject lines with capitalizing: ", count_capit / (count_capit + count_not_capit) * 100
print "Percentage of subject lines without capitalizing: ", count_not_capit / (count_capit + count_not_capit) * 100


p = re.compile('#[a-zA-Z0-9_]*')
count_tickets = 0.00
count_wout_tickets = 0.00
for commit in c_data:
    #m = p.findall(commit['subject']) - find coincidences and print it as list
    #print m
    o = p.search(commit['subject'])
    if o is not None:
        count_tickets += 1
    else:
        count_wout_tickets += 1
print "Ticket frequency, %: ", count_tickets / (count_tickets + count_wout_tickets)


q_add = re.compile('add+ed', re.IGNORECASE)
r_add = re.compile('add+s', re.IGNORECASE)
count_add = 0.00
count_added = 0.00
count_add_ = 0.00
count_add_s = 0.00
for commit in c_data:
    ed = q_add.search(commit['subject'])
    if ed:
        count_add += 1
    else:
        count_added += 1
    s = r_add.search(commit['subject'])
    if s:
        count_add_ += 1
    else:
        count_add_s += 1
print "Added/Adds frequency, %: ", (count_add + count_add_) / (count_add + count_added) * 100


q_fix = re.compile('fix+ed', re.IGNORECASE)
r_fix = re.compile('fix+es', re.IGNORECASE)
count_fix = 0.00
count_fixed = 0.00
count_fix_ = 0.00
count_fix_es = 0.00
for commit in c_data:
    ed_fix = q_fix.search(commit['subject'])
    if ed_fix:
        count_fix += 1
    else:
        count_fixed += 1
    s_fix = r_fix.search(commit['subject'])
    if s_fix:
        count_fix_ += 1
    else:
        count_fix_es += 1
print "Fixed/Fixes frequency, %: ", (count_fix + count_fix_) / (count_fix + count_fixed) * 100


link = re.compile('url', re.IGNORECASE)
count_url = 0.00
count_wout_url = 0.00
for commit in c_data:
    #l = link.findall(commit['subject']) - find coincidences and print it as list
    #print l
    l = link.search(commit['subject'])
    if l:
        count_url += 1
    else:
        count_wout_url += 1
print "URL frequency, %: ", count_url / (count_url + count_wout_url) * 100

