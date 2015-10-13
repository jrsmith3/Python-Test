
from subprocess import check_output
import os
import sys
if len(sys.argv) >= 2:
    test_file = sys.argv[1]
else:
    test_file = 'problem.py'

for i in range(len(os.listdir('test-cases'))/2):
    cmd = ['python', test_file]
    # cmd = 'sbcl --script problem.lisp'.split(' ')
    # cmd = 'python %s' % test_file
    # cmd = cmd.split(' ')
    output = check_output(cmd, stdin=open('test-cases/input0' + str(i) + '.txt')).strip('\n')
    expected_output = open('test-cases/output0' + str(i) + '.txt').read()
    try:
        assert output == expected_output, 'Test case %d failed: Expected: %s Actual: %s' % (i, expected_output, output)
        print 'Test case %d passed successfully!' % i
    except AssertionError as e:
        print e
    
    
