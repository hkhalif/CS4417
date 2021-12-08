import sys
bigrams=[]
l=sys.stdin.read()
l=l.strip()
l=l.split()
bigrams.extend([(l[i-1], l[i]) for i in range (1, len(l))])
for bigram in bigrams:
	print '%s\t%s' % (bigram[0]+","+bigram[1],1)
