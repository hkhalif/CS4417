import sys
for l in sys.stdin:
	filenamežsys.stdin.name
	l = l.strip()
	words = l.split()
	for word in words:
		print '%s\t%s' % (word+","+filename,1)
