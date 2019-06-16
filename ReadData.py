# from calendar import monthrange
# import csv
# import datetime
# from scipy.stats.stats import pearsonr,spearmanr
# from scipy.signal import correlate
# import fix_yahoo_finance as yf
# import matplotlib.pyplot as plt
# import TimeLa
#
# peers = ['HMC', 'TM', 'F', 'GM']
# df = yf.download('GM',"2012-11-16","2017-09-29")
#
# # Do for TSLA and Peers
# # Verify data are normally distributed if Pearson Coeff. is considered.
#
# # Look at  VWAP and Typical
#
# # Keep in mind that exchanges are only open certain days of the week and a certaing time-period of the day.
# # Whereas, Twitter is always accessible. Thus, I will ignore tweets on weekends.
#
#
# # If time-complexity becomes relevant, use generators for the range of dates
# # and use a proper Counter for counting tweets.
#
# def typical_price(high,low,close):
#     return (high+low+close)/3.0
#
# def days_in_month(year,month):
#     return monthrange(year, month)[1]
#
#
#
#
# # '2017-09-29 17:39:19' -> '2017-09-29' -> datetime object
# def year_month_day(time_csv):
#     s = time_csv.split(' ')
#     day = s[0]
#     return datetime.datetime.strptime(day, "%Y-%m-%d")
#
# def increment_hash_counter(hc,key):
#     hc[key] += 1
#
#
#
# # Build a vector with the ith entry representing the number of tweets in the ith day from 2012-11-16 until 2017-09-29
#
#
# start = datetime.datetime.strptime("2012-11-16", "%Y-%m-%d")
# end = datetime.datetime.strptime("2017-09-29", "%Y-%m-%d")
#
# # Hash Counter object
# date_generated = {(start + datetime.timedelta(days=x)):0 for x in range(0, (end-start).days + 1)}
# # typical_generated = {(start + datetime.timedelta(days=x)):None for x in range(0, (end-start).days + 1)}
#
#
#
# with open(file, mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for row in csv_reader:
#         dt = year_month_day(row['Time'])
#         assert dt in date_generated
#         increment_hash_counter(date_generated,dt)
#
#
#
# list_of_date = [str(i) for i in list(df.index)]
# print('Number of days total: ', len(date_generated))
# print('number of trade-days: ',len(list_of_date))
#
#
# # Guaranteed same order
# lo_tweet = []
# lo_price = []
# lo_vwap = []
#
# vol_so_far = 0.0
# vp_so_far = 0.0
#
# ic = 0
# for high,low,close,vol in zip(df['High'],df['Low'],df['Close'],df['Volume']):
#     vol = float(vol)
#     tp = typical_price(high,low,close)
#
#     vp_so_far += vol*tp
#     vol_so_far += vol
#
#     date = list_of_date[ic]
#     dt = year_month_day(date)
#
#     lo_tweet.append(date_generated[dt])
#     lo_price.append(tp)
#     lo_vwap.append(vp_so_far/vol_so_far)
#
#     ic += 1
#
# lo_price  = lo_price[200:]
# lo_tweet = lo_tweet[200:]
#
# print(pearsonr(lo_tweet,lo_price))
# print('Lag: ', TimeLa.positive_correlation_time_lag(lo_tweet,lo_price))
#
# #plt.plot(correlate(lo_price,lo_tweet))
# plt.plot(lo_tweet,label='Number of Tweets')
# plt.plot(lo_price,label='Price Index')
# plt.legend()
# plt.show()
#
#
#
#
