import numpy as np
import random

# after lags before by time_lag(before, after)
def positive_correlation_time_lag(before, after, max_lag=None):
    corr = np.correlate(before,after,"full")
    return len(corr) // 2.0 - np.argmax(corr)

# r = [random.random() for i in range(0,40)]
# r = list(range(0,10))
# rr = r.copy()
# a = r + [0,0,0,0,0]
# b = [0,0,0,0,0]+rr
#
# print(time_lag(a,b))