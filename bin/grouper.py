#This function will group by county and return new object with county and posting
import json
import urllib
import requests

postings = { }



page = 0

for x in range(0, 3):

	page = 0

	r = requests.get('http://search.3taps.com/?auth_token=bfab94b0cc726e2bb24123a0c3babd7d&text=airstream' + '&page=' + str(page) + '&tier='+ str(x))
	counties = r.json()
	if counties['success']:
		page = counties['next_page']
		postings =  counties['postings']
		init_tier = counties['next_tier']
	else:
		break

	while page != 0:
		page += 1
		r = requests.get('http://search.3taps.com/?auth_token=bfab94b0cc726e2bb24123a0c3babd7d&text=airstream' + '&page=' + str(page) + '&tier=' + str(x))
		counties = r.json()
		if counties['success']:
			page = counties['next_page']
			postings =  postings + counties['postings']
		else:
			break

