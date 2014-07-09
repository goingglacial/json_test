import json
from pprint import pprint

data_string = open('test_peeps.json', 'r').read()
print data_string

data = json.loads(data_string)
print data

