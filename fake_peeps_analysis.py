import json
from collections import Counter

data_string = open('fake_peeps.json', 'r').read()
print data_string

data_decoded = json.loads(data_string)
print data_decoded

data_encoded = json.dumps(data_decoded)
print data_encoded

print data_decoded

# use data_decoded to find average age of folks
# in test json file
age_list = [dictionary["age"] for dictionary in data_decoded]
average_age = sum(age_list) / len(age_list)
# print average_age
print "The average age of fake folks is " + str(average_age) + "."

# calculate total number of people in json test file
count = 0
for dictionary["gender"] in data_decoded:
    count = count + 1
# print count
print "There are " + str(count) + " people in this motley crew."

# calculate totals for women and men in json test file
gender_list = [dictionary["gender"] for dictionary in data_decoded]
print gender_list

num_females = gender_list.count("female")
print num_females

num_males = gender_list.count("male")
print num_males



