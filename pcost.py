import report
import csv
def pcost(filename):
    portfolio = report.read_portfolio(filename)
    return sum([s['shares']*s['price'] for s in portfolio])

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = pcost(filename)
print('Total cost:', cost)

# pcost.py
