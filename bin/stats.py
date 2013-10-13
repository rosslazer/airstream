import grouper

#returns true if all needed fields are present
def isValid(posting):
	return posting['location'].has_key('county')

#Take the group and compile stats
#Key => {gross sum, quantity, average, state, county}
posting_stats = {}

max_val = 0
min_val = 0 
average = 0
count = 0

for posting in grouper.postings:
	if isValid(posting):
        	county = posting['location']['county']
		county_split = county.split('-')
		price = posting['price']
        	if county in posting_stats:
			posting_stats[county][0] += price
                	posting_stats[county][1] += 1
			count += 1
			average += price
			max_val = round(max(price, max_val), 2)
			min_val = round(min(price, min_val), 2)
        	else:
                	posting_stats[county] = [price, 1, 0, county_split[1], county_split[2]]

#Calculate averages
for key,value in posting_stats.items():
	posting_stats[key][2] = posting_stats[key][0] / posting_stats[key][1]
	posting_stats[key][2] = round(posting_stats[key][2], 2)
average = round((average / count), 2)

#For testing
for key,value in posting_stats.items():
	print posting_stats[key][3] + ' ' + posting_stats[key][4] + ': ' + str(posting_stats[key][2])

print 'Average: ' + str(average)
print 'Largest Price: ' + str(max_val)
print 'Smallest Price: ' + str(min_val)
