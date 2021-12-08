from operator import itemgetter 
import sys

c_word = None
c_count = 0 
word = None
for line in sys.stdin:
	line= line.strip()
	word, count = line.split('\t',1)
	try:
		count = int(count)
	except ValueError:
		continue
	if c_word == word:
		c_count +=count
	else:
		if c_word:
			print '%s\t%s' % (c_word, c_count)
		c_count = count
		c_word =word 
if c_word ==word:
	print '%s\t%s' % (c_word, c_count)
	
