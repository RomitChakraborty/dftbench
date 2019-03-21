# dftbench
Auxillliary python script for a custom DFT benchmark in QChem

To perform a dft benchmark

1. Copy the contents of the source folder to your ~/bin/ directory. This makes sure it is available on the command prompt irrespective of your pwd
2. Create a vanilla qc input file test.in you wish to run with a method, let's say b3lyp

3. source your bashrc and then run 

genscan.py test.in cluster

this writes qchem input for an assortment of density functionals for the given input configuration

Additional features:

Has a read feature that parses your output. I focussed on EDA and frequency calculations to parse

Changes elements in your input if you need them

Changes bases (most of the available ones in qchem)

Has this feature where you can also submit it to the queue bypassing the annoying submitSLURM command

Bugfix:

Have to add re.ignorecase to the regexes, i think it works only for lowercase input



