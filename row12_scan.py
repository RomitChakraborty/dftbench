#! /usr/bin/env python

import subprocess, re, os, time, random
from elements import *


for element in period_12:
    #print element

    f = open('h2.in')
    g = f.read()
    f.close()

    qc_in = element + "2.in"
    qc_out = element + "2.out"
    ostream = open(qc_in, 'w')
    el_string = element + " "
    print el_string
    g = re.sub("H\s+",el_string , g)
    ostream.write(g)
    ostream.close()
    if args.locale=='box':
        subprocess.call("qchem -nt 4 " + qc_in + " " + qc_out, shell = True)
    elif args.locale=='cluster':
        subprocess.call("submitSLURM -t openmp -p 12 " + qc_in, shell = True)
