#pcost.py

import csv
def pcost(filename):

    tcost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                nshares = int(row[1])
                price = float(row[2])
                tcost += nshares * price
            except ValueError:
                print('Bad row:', row)

    return tcost

import sys
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = input('Enter a filename:')

cost = pcost(filename)
print('Total cost:', cost)

# pcost.py
#
# Exercise 1.27
