#! /usr/bin/env python

# Romit Chakraborty
# Head-Gordon group

basis_list = ['sto-2g', 'sto-3g', 'sto-6g', '3-21g', '4-31g', '6-31g','6-311g','g3large', 'g3mp2large', 'sv', 'cc-pvtz','vtz', 'pc-1','def2-svp', 'ugbs']

# Structured basis sets

pople = ['sto-2g', 'sto-3g', 'sto-6g', '3-21g', '4-31g', '6-31g','6-311g','g3large', 'g3mp2large']
dunning = ['sv', 'sv*', 'sv(d,p)', 'dz','dz+', 'dz++', 'dz*', 'dz**', 'dz(d,p', 'tz', 'tz+', 'tz++', 'tz*', 'tz**', 'tz(d,p)']
dunning_cc = ['cc-pvdz', 'cc-pvtz', 'cc-pvqz', 'cc-pv5z', 'cc-cpvdz', 'cc-cpvtz', 'cc-cpvqz','cc-cpv5z',]
dunning_aug = ['aug-'+ i  for i in dunning_cc]
ahlrichs = ['tzv','vdz', 'vtz']

a = ['pc', 'pcJ', 'pcS']
b = ['0', '1', '2', '3', '4']

jensen = [i + '-' + j for i in a for j in b]
karlsruhe = ['def-msvp', 'def2-sv(p)', 'def2-svp', 'def2-svpd', 'def2-tzvp', 'def2-tzvpp', 'def2-tzvpd', 'def2-tzvppd', 'def2-qzvp', 'def2-qzvpp','def2-qzvppd', 'ugbs' ]



# for j in [2,3,6]:
#     "STO{}(.,+)G(d, p)".format(j)


#     for m in ['d', '2d', '3d', '2df']:

# j   311(k+, l+)G(m, n)


# Bases supported for first row transitional elements

b_row1t = ['sto-3g', 'sto-6g', '3-21g', '6-31g','6-31g(d,p)', 'g3large', '6-31(+,+)g(3d,3p)', 'vdz', 'vtz', 'def-msvp', 'def2-sv(p)', 'def2-svp', 'def2-svpd', 'def2-tzvp', 'def2-tzvpp', 'def2-tzvpd', 'def2-tzvppd', 'def2-qzvp', 'def2-qzvpp','def2-qzvppd', 'ugbs' ]

# all 

t1_bas = ['def2-svp', 'def2-tzvp', 'ugbs'] 
b_all = pople + dunning_cc + dunning_aug + ahlrichs + jensen + karlsruhe
print len(b_all)
