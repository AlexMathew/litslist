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
	for i in xrange(count):
		try:
			f = open(os.path.join(os.curdir, 'Lists', str(i+1) + '.txt'), 'w')
			file_content = ''
			for category, category_list in sets.items():
				file_content += (category + ' -- ' + category_list[i] + '\n')
			f.write(file_content)
			f.close()
		except IndexError:
			break_point = i
			break
	return
