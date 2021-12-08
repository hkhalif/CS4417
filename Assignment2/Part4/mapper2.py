#!/usr/bin/env python

import sys


for l in sys.stdin:
    l = l.strip()
    wordfilename,count=l.split('\t',1)
    word,filename=wordfilename.split(' ',1)
    z=word+' '+count;
    print '%s\t%s' % (filename, z)
  
