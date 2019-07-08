# StockPriceComparedtoTweets
A utility for observing the various correlation statistics between a Twitter user's tweets and a publicly listed company's stock price

Interested in how a Twitter-active CEO is affecting their company's stock price? Or, to what degree of time-lag exits between the greatest (local) correlation in their tweets with their company's stock price?
<br>

This project allows for a basic correlation analysis, coupled with p-values, and a visual.<br>

To get started, enter your Twitter API keys and access tokens in `Tweepy.py`<br>

Scroll to the bottom of this file and you can change the Twitter handle to the user of your preference. Run it, and you'll notice a CSV file of their tweets populate your project directory.<br>


Now, navigate to `StockTwitter.py`, and you can enter your CSV file name and the corresponding company's ticker. As an example, Elon Musk's tweets are included in the project. So, you can change the file name to `elonmusk_tweets.csv`, and the ticker to `TSLA`.


Here's an example of the outputted correlation summary:

![Image of Stats](https://github.com/D-Thatcher/StockPriceComparedtoTweets/blob/master/stats.PNG)

and of the visual:

![Image of Visual](https://github.com/D-Thatcher/StockPriceComparedtoTweets/blob/master/chart.PNG)


You can compare common financial measures, such as volume-weighted-average-price, high, low, close, or just regular volume.


