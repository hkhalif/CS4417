from operator import itemgetter 
import sys
c =0
c_word = None
word = None
for line in sys.stdin:
	line= line.strip()
	word, count = line.split('\t',1)
	try:
		count = int(count)
	except ValueError:
		continue
	if count == 1:
		c +=1
print '%s\t%s' % ("No. of brigrams which Unique", c)
	
