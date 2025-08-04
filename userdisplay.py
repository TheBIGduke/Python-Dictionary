import json

f = open('output.json')
data = json.load(f)
for i in data ['emp_details']:
    print(i)

f.close()