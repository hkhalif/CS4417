import sys
count=0
for l in sys.stdin:
	l = l.strip()
	words = l.split()
	word, count = l.split('\t',1)
	print '%s\t%s' % (word,count)
