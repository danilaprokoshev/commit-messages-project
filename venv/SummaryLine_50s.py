import json
c_data_file = open('flask_commit_messages.json')
c_data = json.load(c_msgs_file)
c_data_file.close()

for commit in c_data:
    print(commit['subject'])
    