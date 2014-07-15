#!/usr/bin/env python

import json
from collections import Counter

people_list = json.load(open('fake_peeps.json', 'r'))

ages = [p['age'] for p in people_list]

average_age = sum(ages) / len(ages)
print "The average age of folks in this motley crew is " + str(average_age) + "."

genders = [p['gender'] for p in people_list]

num_females = genders.count('female')
print "There are " + str(num_females) + " chicks in this group."

num_males = genders.count('male')
print "There are " + str(num_males) + " dudes in this group."