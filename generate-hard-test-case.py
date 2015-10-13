"""Usage:

At the command line, if you do `python generate-hard-test-case.py 15 78`,
this script will produce a file called `hard-test-case15x78.txt` that
contains a matrix with 15 rows and 78 columns.
"""

from random import random, choice
import sys
m, n = map(int, sys.argv[1:])
with open('hard-test-case{0}x{1}.txt'.format(m, n), 'w') as test_file:
    test_file.write('{0}\n{1}\n'.format(m, n))
    matrix = '\n'.join([' '.join([choice('01') for i in range(n)]) for i in range(m)])
    test_file.write(matrix)
