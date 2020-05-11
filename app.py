import yahoo_finance
import db_connector
import datetime
import keyring

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

now_time = datetime.datetime.now()
timestamp = now_time.strftime("%Y-%m-%d %H:%M:%S")
workbench_pwd = keyring.get_password("mysql", "workbench")
sql_insert = "INSERT INTO financeapp (ticker, price, outstanding, teps, fep, bv, fpe, pbv, valuation, datetime) " \
            "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
values = (ticker.upper(), price, outstanding, teps, fpe, bv, fpe, pbv, valuation, timestamp)
sql_query = "SELECT * FROM finan"
db_connector.database_query("192.168.1.7", "workbench", workbench_pwd, "fin", sql_insert, values)

db_connector.database_query("192.168.1.7", "workbench", workbench_pwd, "fin", sql_query, values)

if 0 < valuation <= 22.5:
    print("This stock may be a good value.\nThe valuation is {0}.".format(valuation))
else:
    print("This stock is probably overvalued.\nThe valuation is {0}.".format(valuation))
