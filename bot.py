from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# global declaration of variables

class TwitterBOT:
    username = ""
    password = ""
    bot = ""
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        
        # the twitter URL to login
        bot.get('https://twitter.com/login')
        
        time.sleep(3)
        
        # Html elements on the twitter html
        attribute_name_email = 'session[username_or_email]'
        attribute_name_password = 'session[password]'
        
        # find the elements on HTML by the above attributes
        email = bot.find_element_by_name(attribute_name_email)
        password = bot.find_element_by_name(attribute_name_password)
        
        email.clear()
        password.clear()
        
        # send keys of the credentials
        email.send_keys(self.username)
        password.send_keys(self.password)
        
        # RETURN to submit the login credentials
        password.send_keys(Keys.RETURN)
        
        # wait for 5seconds to load the page and open
        time.sleep(5)

    # like tweets
    def like_tweets(self, hashtag):
        bot = self.bot
        
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
        time.sleep(3)
        
        # scroll to view and like a single tweet
        for i in range(1, 3):
            # here, bot excecutes some javascript, scrolling all over the twitter page
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)
            
            # find tweets by class name attribute
            tweet_classname_attribute = 'tweet'
            
            # find tweet
            tweets = bot.find_elements_by_class_name(tweet_classname_attribute)
            
            for elem in tweets:
                # get each link of tweet and form an array of links
                tweet_link_attribute = 'data-permalink-path'
                
                # find links
                links = [elem.get_attribute(tweet_classname_attribute)]
            
                # links = [elem.get_attribute(tweet_classname_attribute) for elem in tweets]
                
                # print(links)
                for link in links:
                    #let bot get each link for each tweet/post 
                    bot.get('https://twitter.com'+link)
                    
                    # find like element by classname and click to perform a like
                    try:
                        like_class_name_attribute = 'HeartAnimation'
                        bot.find_element_by_class_name(like_class_name_attribute).click()
                        time.sleep(15)
                    except Exception as ex:
                        time.sleep(60)
                    
            

