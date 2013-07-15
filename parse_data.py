#!/usr/bin/env python

import csv

columns = ['rank','country','rider_link','rider','rider_no','team_link','team','gap','total_time']
table = {}

def init_dict():
	with open('1.txt') as csvfile:
		csvreader = csv.DictReader(csvfile, fieldnames=columns, delimiter='|')
		for row in csvreader:
			rider =  row['rider']
			table[rider] = []

def put_gaps(filename):
        with open(filename) as csvfile:
                csvreader = csv.DictReader(csvfile, fieldnames=columns, delimiter='|')
                for row in csvreader:
                        gap = row['gap'].replace("+","").replace("'", "").replace(" ", "").replace("h","")
			gap = parse_number(gap)
			rider =  row['rider']
                        table[rider].append(gap)
def parse_number(num_str):
	num_str = num_str.strip()
	if len(num_str) > 0:
		num_str = str(int(num_str))
	else:
		num_str = '0'

	return num_str


def write_result():
	with open('itg.csv', 'a') as csvresult:
		csvwriter = csv.writer(csvresult, delimiter=',')
		csvwriter.writerow(['Rider'] + range(1,16))
		for key in table:
			csvwriter.writerow([key] + table[key])

init_dict()

for i in range(1,16):
	put_gaps(str(i)+'.txt')

write_result()

print table
