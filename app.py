import yahoo_finance

ticker = input("Enter a Stock Ticker: ")

key_stats = yahoo_finance.key_stats(ticker)
# stock_profile = yahoo_finance.stock_profile(ticker)
financial_data = yahoo_finance.financial_data(ticker)

# company = stock_profile["assetProfile"]["currentPrice"]["fmt"]

# equity =

price = financial_data["financialData"]["currentPrice"]["fmt"]
outstanding = key_stats["defaultKeyStatistics"]["sharesOutstanding"]["fmt"]
teps = key_stats["defaultKeyStatistics"]["trailingEps"]["raw"]
feps = key_stats["defaultKeyStatistics"]["forwardEps"]["raw"]
bv = key_stats["defaultKeyStatistics"]["bookValue"]["raw"]
fpe = key_stats["defaultKeyStatistics"]["forwardPE"]["raw"]
pbv = key_stats["defaultKeyStatistics"]["priceToBook"]["raw"]
valuation = (float(fpe) * float(pbv))
#

print("{0} Stock Highlights".format(ticker.upper()))
print("Current Price: {0}".format(price))
print("Shares Outstanding: {0}".format(outstanding))
print("Trailing EPS: {0}".format(teps))
print("Future EPS: {0}".format(feps))
print("Book Value: {0}".format(bv))
print("Forward P/E: {0}".format(fpe))
print("P/BV: {0}".format(pbv))
print("The Buffett Simple Valuation: {0}".format(valuation))

if 0 < valuation <= 22.5:
    print("This stock may be a good value.")
else:
    print("This stock is probably overvalued.")
