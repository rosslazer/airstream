import grouper

#Take the group and compile stats
#Key => {gross sum, quantity}
posting_stats = dict()

for posting in grouper.postings:
	if 'county' in posting['location']:
        	county = posting['location']['county']
        	if county in posting_stats:
                	posting_stats[county][1] += 1
        	else:
                	posting_stats[county] = [0, 1]
