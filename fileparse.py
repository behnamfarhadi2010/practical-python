# fileparse.py
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
     
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
  
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        headers = next(rows) if has_headers else []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for rowno, row in enumerate (rows,1):
            if not row:   
                
                continue
            # Filter the row if specific columns were selected
            if select:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {rowno}: Couldn't convert {row}")
                        print(f"Row {rowno}: Reason {e}")
                    continue

            # Make a dictionary
            if types:
                row = [func(val) for func, val in zip(types, row)]
            
            if headers:
                record = dict(zip(headers, row))

            else:
                record = tuple(row)

            records.append(record)

        return records
