# from iexfinance.stocks import get_historical_data, get_historical_intraday
# from iexfinance.stocks import Stock
# import matplotlib.pyplot as plt
# from datetime import datetime,date
# import iexfinance
#
# # Crypto
# crypt = iexfinance.stocks.get_crypto_quotes()
#
#
# # Daily
# start = datetime(2017, 1, 1)
# end = datetime(2018, 1, 1)
#
# # data = get_historical_data("TSLA", start=start, end=end, output_format='pandas')
# #
# # data.close.plot()
# # plt.show()
# #
#
# # Minutely
# # a date within three months prior
# my_date = datetime(2019, 3, 1)
#
# # data = get_historical_intraday("TSLA",date=my_date, output_format='pandas')
# # data.close.plot()
# # plt.show()
#
#
# # Sheets
#
# aapl = Stock("TSLA")
# # aapl.get_balance_sheet()
# # aapl.get_income_statement()
# # aapl.get_cash_flow()
# #
# #
# # # List of Competitors (Peers)
# #
# print(aapl.get_peers())