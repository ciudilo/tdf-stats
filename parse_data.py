
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
			rider =  row['rider']
                        table[rider].append(gap)

init_dict()

for i in range(1,16):
	put_gaps(str(i)+'.txt')

print table
