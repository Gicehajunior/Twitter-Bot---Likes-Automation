from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from includes import credentials

class TwitterBOT:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')

        time.sleep(3)
        email = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    # like tweets
    def like_tweets(self, hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        
        # scroll to view and like a single tweet
        for i in range(1, 3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            
            # find tweets by class name attribute
            tweets = bot.find_elements_by_class_name('tweet')
            
            # get each link and form an array of links
            links = [elem.get_attribute('data-permalink-path') for elem in tweets]
            
            print(links)
            

# credentials
user_password = credentials.account_password()
user_uid = credentials.account_uid()

gj = TwitterBOT(user_uid, user_password)
gj.login()
gj.like_tweets('AndelaKenya') 
