from twitter import Api
from datetime import datetime

twitter_consumer_key =''
twitter_consumer_secret=''
twitter_access_token_key= ''
twitter_access_token_secret =''


class TwitterParser(Api):

    def __init__(self,consumer_key=twitter_consumer_key,
                      consumer_secret=twitter_consumer_secret,
                      access_token_key=twitter_access_token_key,
                      access_token_secret=twitter_access_token_secret):

        super().__init__(consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

        self.max_status_per_user = 9999999



    def verify_active(self):
        return self.VerifyCredentials()

    def to_published(self,twitter_created_date):
        s = twitter_created_date.split(' ')
        dt = datetime.strptime(twitter_created_date, '%a %b %d %H:%M:%S %z %Y')
        return dt


    def get_statuses(self,user):
        statuses = self.GetUserTimeline(screen_name=user, count=self.max_status_per_user)
        lo_item = []
        for s in statuses:
            sd = s.AsDict()
            # print(sd)
            # for i in sd:
            #     print(i, " ", sd[i])
            date = self.to_published(sd['created_at'])

            item = {'title': sd['text'], 'published': date}
            lo_item.append(item)

        return lo_item

    def get_followers(self,user):
        return self.GetFollowers(screen_name=user)

    def get_following(self,user):
        return self.GetFriends(screen_name=user)




















