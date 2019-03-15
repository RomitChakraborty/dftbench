#! /usr/bin/env python

# Romit Chakraborty
# Head-Gordon Group

method_list = ['b97-d3', 'b97-d3bj', 'revpbe', 'revpbe-d3bj', 'blyp', 'blyp-d3bj', 'pbe', 'b97m-rv', 'm06-l', 'tpss', 'b3lyp','b3lyp-d3bj',   'wb97x-v','wb97x-d3', 'wb97x-d', 'revpbe0', 'wb97m-v', 'wm05-d','m06-2x', 'tpssh' ]

# Jacob's ladder 

# LSDA (Local Spin Density Approximation)

rung_1 = ['spw92', 'lda', 'svwn5']

# GGA (Generalized Gradient Approximation)

rung_2 = ['b97-d3bj', 'revpbe', 'revpbe-d3bj', 'blyp', 'blyp-d3bj', 'pbe', 'bop', 'bp86', 'bp86vwn', 'bppbe', 'gam']

# MGGA

rung_3 = ['b97m-v', 'b97m-rv', 'm06-l','m06-l-d30', 'tpss', 'tpss-d3bj', 'revtpss', 'bloc', 'm11-l', 'mbeef', 'mgga_ms0', 'mgga_ms1', 'mgga_ms2', 'mgga_ms1-d30', 'mgga_ms2-d30', 'mgga_mvs', 'mn12-l', 'mn15-l', 'otpss', 'pkzb', 'scan', 't-hcth', 'tm', 'vsxc']

# XX (m)GGA -- Hybrids

rung_4 = ['b97','b97-1', 'b97-2', 'b97-3', 'b97-k','b1lyp','b1pw91', 'b3lyp5', 'wb97', 'wb97x', 'wb97x-rv', 'wb97x-v', 'wb97x-d3', 'wb97x-d', 'b3lyp-d3bj', 'revpbe0-d3bj', 'wb97m-v', 'wm05-d', 'm06-d30', 'tpssh-d3bj']

# Double Hybrids (m)GGA -- some of them do not work, bug fix

rung_5 = ['dsd-pbepbe-d3', 'wb97x-2-lp', 'wb97x-2-tqz', 'xyg3', 'xygj-os', 'ptpss-d3']

all = rung_1 + rung_2 + rung_3 + rung_4 + rung_5

t1_sel = ['blyp-d3bj', 'b3lyp-d3bj', 'pbe', 'b97-1', 'b97-3', 'b97m-v', 'b97m-rv', 'wb97', 'wb97x', 'wb97x-d3','wb97x-rv', 'wb97m-v', 'revpbe-d3bj', 'm06-l', 'm06-l-d30', 'dsd-pbepbe-d3']


