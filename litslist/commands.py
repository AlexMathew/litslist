"""
Includes execution logic for the commands
"""

import os
import csv
import random

def run_create(count):
	file_list = [filename for filename in os.listdir('.') if os.path.isfile(filename)]
	sets = {}
	for filename in file_list:
		content = open(os.path.join(os.curdir, filename)).read().split('\n')
		random.shuffle(content)
		sets[filename[:filename.index('.')].title()] = content
	if not os.path.exists('Lists'):
		os.mkdir('Lists')
	csvfile = open(os.path.join(os.curdir, 'Sets.csv'), 'w')
	csvwriter = csv.DictWriter(csvfile, sets.keys())
	csvwriter.writeheader()
	break_point = count
	for i in xrange(count):
		try:
			f = open(os.path.join(os.curdir, 'Lists', str(i+1) + '.txt'), 'w')
			file_content = ''
			csv_content = dict()
			for category, category_list in sets.items():
				file_content += (category + ' -- ' + category_list[i] + '\n')
				csv_content[category] = category_list[i]
			f.write(file_content)
			csvwriter.writerow(csv_content)
			f.close()
		except IndexError:
			break_point = i
			break
	csvfile.close()
	try:
		for category, category_list in sets.items():
			f = open(os.path.join(os.curdir, 'Remaining_' + category + '.txt'), 'w')
			file_content = "\n".join(category_list[break_point:])
			f.write(file_content)
			f.close()
	except NameError, e:
		print e
		pass
	return
