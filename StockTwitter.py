import csv
import datetime
import fix_yahoo_finance as yf
from scipy.stats.stats import pearsonr,spearmanr,kendalltau
from scipy import std
import matplotlib.pyplot as plt
import TimeLa

print('Finished Importing.')

def extract_dash(time_str):
    s = time_str.split(' ')
    return s[0]

def year_month_day(time_csv):
    day = extract_dash(time_csv)
    return datetime.datetime.strptime(day, "%Y-%m-%d")

def typical_price(high,low,close):
    return (high+low+close)/3.0

def all_date(file):
    with open(file, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        all_date = []
        for row in csv_reader:
            all_date.append(year_month_day(row['created_at']))
    return all_date

def increment_hash_counter(hc,key):
    hc[key] += 1



def correlation_summary(ticker, tweet_file):
    all_dates = all_date(tweet_file)

    start = all_dates[-1]
    end = all_dates[0]

    date_generated = {(start + datetime.timedelta(days=x)): 0 for x in range(0, (end - start).days + 1)}
    # Count tweets for each day in range
    for dt in all_dates:
        increment_hash_counter(date_generated,dt)


    df = yf.download(ticker, extract_dash(str(start)), extract_dash(str(end)))
    list_of_date = [str(i) for i in list(df.index)]

    lo_tweet = []
    lo_price = []
    lo_vwap = []

    vol_so_far = 0.0
    vp_so_far = 0.0

    ic = 0
    for high, low, close, vol in zip(df['High'], df['Low'], df['Close'], df['Volume']):
        vol = float(vol)
        tp = typical_price(high, low, close)

        vp_so_far += vol * tp
        vol_so_far += vol

        date = list_of_date[ic]
        dt = year_month_day(date)

        lo_tweet.append(date_generated[dt])
        lo_price.append(tp)
        lo_vwap.append(vp_so_far / vol_so_far)

        ic += 1


    pcc, ppc_alpha = pearsonr(lo_tweet,lo_price)
    scc, scc_alpha = spearmanr(lo_tweet, lo_price)
    kcc, kcc_alpha = kendalltau(lo_tweet, lo_price)

    print('______________________________________________________________')
    print('Only tweets during trading days are considered for comparison.')
    print("Total number of tweets: ", len(all_dates))
    print("Total number of trading days: ", len(list_of_date))
    print("Starting date: ", extract_dash(str(start)))
    print("End date: ", extract_dash(str(end)))
    print('Pearson Correlation Coefficient: ',pcc,'   P-Value: ',str(ppc_alpha))
    print('Spearmann Rank Correlation Coefficient: ',scc,'    P-Value',str(scc_alpha))
    print('Kendall Tau Rank Correlation Coefficient: ', kcc,'   P-Value: ',str(kcc_alpha))
    print('Inter-Correlation-Coefficient Standard Deviation: ',std([pcc,scc,kcc]))
    print('Global Time Lag: ', TimeLa.positive_correlation_time_lag(lo_tweet,lo_price))
    print('______________________________________________________________')

    plt.plot(lo_tweet, label='Number of Tweets')
    plt.plot(lo_price, label='Price Index')
    plt.legend()
    plt.show()


correlation_summary('CRM','Benioff_tweets.csv')