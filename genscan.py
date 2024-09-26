#! /usr/bin/env python

import subprocess, re, os, time, random
from def_dftscan import dft_sub_om, dft_write_om
from methods import rung_3, rung_4, sel, test
import argparse


# Generates a list of input files with selected DFT functions given a vanilla qchem input
# syntax:
# run the following command from your input directory:
# genscan.py vanilla_qc.in locale
# locale = 'cluster' for running computations in the cluster
# locale = 'box' for running in box

parser = argparse.ArgumentParser()
parser.add_argument('mol_in', type=str, help="Vanilla qchem input for dft_scan")
parser.add_argument('locale', type=str, help="User locale", choices=['box', 'cluster'], default='box')

args = parser.parse_args()

methods = sel

dft_write_om(args.mol_in, methods)
#dft_sub_om(args.mol_in, methods, args.locale)

