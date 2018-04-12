import os,sys
import cgi
import cgitb
cgitb.enable()

import matplotlib
matplotlib.use('Agg')

os.environ['HOME'] = '/tmp'

import matplotlib.pyplot as plt

plt.plot([1,2,3])

print("Content-type: image/png")
print()

plt.savefig(sys.stdout, format='png')
