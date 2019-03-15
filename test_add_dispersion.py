#! /usr/bin/env python

import subprocess, re, os, time, random



# f = open("h2.in")
# g = f.read()
# print g


methods = ['b3lyp-d3bj', 'm06-l-d30', 'b3lyp']

for method in methods:
    print method
    tmp = method.split('-')
    print tmp
    f = open("h2.in")
    g = f.read()
    f.close()
    print g

    if any('d3bj' in s for s in tmp):
        n_method = 'method ' + method.replace("-d3bj", "") + "\n\t dft_d d3_bj"
        g = re.sub('method.*', n_method, g, flags = re.IGNORECASE)
    elif any('d30' in s for s in tmp):
        n_method = 'method ' + method.replace("-d30", "") + "\n\tdft_d d3_zero"
        g = re.sub('method.*', n_method , g, flags = re.IGNORECASE)
    else:
        n_method = 'method ' + method 
        g = re.sub('method.*', n_method, g, flags=re.IGNORECASE)
    print g
