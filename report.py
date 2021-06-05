# report.py
import csv
import sys
from pprint import pprint
import fileparse

def read_portfolio(filename):
    
    portfolio = fileparse.parse_csv(filename, select=['name','shares','price'], types=[str,int,float])
    return portfolio

def read_prices(filename):
   
    prices = dict(fileparse.parse_csv(filename,types=[str,float], has_headers=False))
    return prices
   

def make_report(portfolio,prices):
   

    rows = []
    for stock in portfolio:
        current_price = prices[stock['name']]
        change = current_price - stock['price']
        summary = (stock['name'], stock['shares'], current_price, change)
        rows.append(summary)
    return rows
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
            print(f'{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}')
def portfolio_report(portfoliofile, pricefile):
    portfolio = read_portfolio(portfoliofile)
    prices    = read_prices(pricefile)
    report = make_report(portfolio, prices)
    print_report(report)
def main(args):
    if len(args) != 3:
        raise SystemExit('Usage: %s portfile pricefile' % args[0])
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    import sys
    main(sys.argv)
