#! /usr/bin/env python
# Function definitions for dft scan


import subprocess, re, os, time, random


def nmethod(g, method):
    """Write new method to qc_in string g adds dispersion correction"""
    tmp = method.split('-')
    print method, tmp

    if any('d3bj' in s for s in tmp):
        n_method = '\n\tmethod ' + method.replace("-d3bj", "") + "\n\t dft_d d3_bj"
        g = re.sub('\s+method.*', n_method, g)
    elif any('d30' in s for s in tmp):
        n_method = '\n\tmethod ' + method.replace("-d30", "") + "\n\tdft_d d3_zero"
        g = re.sub('\s+method.*', n_method , g)
    else:
        n_method = '\n\tmethod ' + method 
        g = re.sub('\s+method.*', n_method, g)
    return g

def nbasis(g, basis):
    """Write new basis to qc_in string g"""
    n_basis = 'basis ' + basis
    g = re.sub('basis.*', n_basis, g)
    return g

def dft_write(mol_in, method_list, basis_list):
    """For a vanilla input, write input for given list of methods and bases"""
    mol = mol_in.split('.')[0]
    
    for method in method_list:
        for basis in basis_list:
            f = open(mol_in)
            g = f.read()
            f.close()

            qc_in = mol + '_' + method + '_' + basis + '.in'
            ostream = open(qc_in, 'w')
            g = nmethod(g,method)
            g = nbasis(g, basis)
            ostream.write(g)
            ostream.close()

def dft_write_om(mol_in, method_list):
    """For a vanilla input, write input for only for given list of methods"""
    mol = mol_in.split('.')[0]
    
    for method in method_list:

        f = open(mol_in)
        g = f.read()
        f.close()

        qc_in = mol + '_' + method + '.in'
        ostream = open(qc_in, 'w')
        g = nmethod(g,method)
            #g = nbasis(g, basis)
        ostream.write(g)
        ostream.close()

            
def dft_sub(mol_in, method_list, basis_list, locale):
    """Submit jobs for given list of methods and bases in a box or the cluster"""
    mol = mol_in.split('.')[0]
    for method in method_list:
        for basis in basis_list:
            qc_in = mol + '_' + method + '_' + basis + '.in'
            qc_out = mol + '_' + method + '_' + basis + '.out'
            
            if locale=='box':
                subprocess.call("qchem -nt 4 " + qc_in + " " + qc_out, shell = True)
            elif locale =='cluster':
                subprocess.call("submitSLURM --save -t openmp -p 32 " + qc_in, shell = True)
            else:
                print "Invalid locale, job not submitted"


def dft_sub_om(mol_in, method_list, locale):
    """Submit jobs for given list of methods (only) in a box or the cluster"""
    mol = mol_in.split('.')[0]
    for method in method_list:

        qc_in = mol + '_' + method + '.in'
        qc_out = mol + '_' + method + '.out'
            
        if locale=='box':
            subprocess.call("qchem -nt 4 " + qc_in + " " + qc_out, shell = True)
        elif locale =='cluster':
            subprocess.call("submitSLURM -t openmp -p 32 -l time=7:00:00 " + qc_in, shell = True)
        else:
            print "Invalid locale, job not submitted"

