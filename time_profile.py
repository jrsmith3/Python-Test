from subprocess import check_output
import os
import sys
import time

cmd = ['python', "problem.py"]

start_time = time.time()
output = check_output(cmd, stdin=open("hard-test-case1000x1000.txt"))
execution_time = time.time() - start_time

print "Largest area:", int(output)
print "Execution time: {}s".format(execution_time)
