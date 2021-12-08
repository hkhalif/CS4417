#!/usr/bin/env python

import sys
import os
from math import log10,sqrt

D=10.0
for l in sys.stdin:
    l = l.strip()
    wf,nNm=l.split('\t',1)
    n,N,m=nNm.split(' ',2)
    n=float(n)
    N=float(N)
    m=float(m)
    tfidf= (n/N)*log10(D/m)
    print '%s\t%s' % (wf,tfidf)

        
