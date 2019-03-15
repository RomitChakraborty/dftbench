#! /usr/bin/env python

import subprocess, re, os, time, random
#from dft_scan import *
# First row light elements

period_1 = ['H', 'He']
period_2 = ['Li', 'Be' , 'C', 'N', 'O', 'F', 'Ne']
period_3 = ['Na', 'Mg', 'Al' , 'Si', 'P', 'S', 'Cl', 'Ar']
period_4 = ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr']

group_1 = ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
group_2 = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
group_3 = ['B', 'Al', 'Ga', 'I', 'Tl']
group_4 = ['C', 'Si', 'Ge', 'Sn', 'Pb']
group_5 = ['N', 'S', 'As', 'Sb', 'Bi']
group_6 = ['O', 'S', 'Se', 'Te', 'Po']
group_7 = ['F', 'Cl', 'Br', 'I', 'At']
group_8 = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn']

#subprocess.call("source ~/.qcsetup", shell = True)

period_12 = period_1 + period_2

#print g

# for element in period_12:
#     print element

#     f = open('h2.in')
#     g = f.read()
#     f.close()

#     qc_in = element + "2.in"
#     qc_out = element + "2.out"
#     ostream = open(qc_in, 'w')
#     el_string = element + " "
#     print el_string
#     g = re.sub("H\s+",el_string , g)
#     ostream.write(g)
#     ostream.close()
#     if args.locale=='box':
#         subprocess.call("qchem -nt 4 " + qc_in + " " + qc_out, shell = True)
#     elif args.locale=='cluster':
#         subprocess.call("submitSLURM -t openmp -p 12 " + qc_in, shell = True)
