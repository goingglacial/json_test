import json

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
print average_age
print "The average age of fake folks is " + str(average_age) + "."

female_count = 0
male_count = 0
for dictionary["gender"] in data_decoded:
    if [dictionary["gender"]] == "female":
        female_count = female_count + 1
    else:
        male_count = male_count + 1
print female_count
print male_counts