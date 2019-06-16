import matplotlib.pyplot as plt
import quandl
data = quandl.get("WIKI/TSLA", start_date="2018-01-01", end_date="2019-01-01", api_key="")
data.Close.plot()
plt.show()