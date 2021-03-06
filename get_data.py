#!/usr/bin/env python

from __future__ import print_function
from bs4 import BeautifulSoup
import requests
import codecs


def get_stage_results(stage):
	r = requests.get('http://www.letour.fr/le-tour/2013/us/'+ stage + '00/classement/bloc-classement-page/ITG.html')
	
	soup = BeautifulSoup(r.text)

	with open(stage+'.txt' , 'a') as f:
		for tr in soup.find('tbody').find_all('tr'):
			rank = tr.find('td').text
			country = tr.find('span').text
			rider_link = tr.find_all('a')[0]['href']
			rider = tr.find_all('a')[0].text
			rider_no = tr.find('td', attrs={'class' : 'col_3'}).text
			team_link = tr.find_all('a')[1]['href']
			team = tr.find_all('a')[1].text
			total_time = tr.find('td', attrs={'class' : 'col_5'}).text
			gap = tr.find('td', attrs={'class' : 'col_5'}).findNextSibling('td').text
  		
			parsed = rank + "|" + country + "|" + rider_link + "|" + rider + "|" + rider_no + "|" + team_link + "|" + team + "|" + gap + "|" + total_time
	
			print( parsed.encode('ascii', 'ignore'), file=f)

for i in range(1,16):
	get_stage_results(str(i))
