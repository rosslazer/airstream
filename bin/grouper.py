#This function will group by county and return new object with county and posting
import json
import urllib
import requests

######################################################
#           DEVELOPMENT MODE set to TRUE             #
#           PRODUCTION MODE set to FALSE             #
######################################################
in_development = False

if in_development == True:
	n = 1
else:
	n = 3

postings = { }

page = 0

for x in range(0, n):

	page = 0

	r = requests.get('http://search.3taps.com/?auth_token=bfab94b0cc726e2bb24123a0c3babd7d&text=airstream&has_price=1&retvals=id,account_id,source,category,category_group,location,external_id,external_url,heading,body,timestamp,expires,language,price,currency,images,annotations,status' + '&page=' + str(page) + '&tier='+ str(x))
	counties = r.json()
	if counties['success']:
		page = counties['next_page']
		postings =  counties['postings']
		init_tier = counties['next_tier']
	else:
		break

	while page != 0:
		page += 1
		r = requests.get('http://search.3taps.com/?auth_token=bfab94b0cc726e2bb24123a0c3babd7d&text=airstream&has_price=1&retvals=id,account_id,source,category,category_group,location,external_id,external_url,heading,body,timestamp,expires,language,price,currency,images,annotations,status' + '&page=' + str(page) + '&tier=' + str(x))
		counties = r.json()
		if counties['success']:
			page = counties['next_page']
			postings =  postings + counties['postings']
		else:
			break

