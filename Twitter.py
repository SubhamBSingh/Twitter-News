from selenium import webdriver
from newsapi import NewsApiClient
import time
import random

NewsAPI = NewsApiClient(api_key='e3fb0a59b3f64cedbea1c1a2ff5a9df1')

def RandomSource():

    global Articles

    Source = ['abc-news','aftenposten','ansa','bloonberg','buzzfeed','bbc-news']

    Y = random.randint(0,5)

    TopHeadlines = NewsAPI.get_top_headlines(sources=Source.pop(Y))
    Articles = TopHeadlines('articles')

def RandomNews():

    global Articles
    global Message

    X = random.randint(0,5)

    ArticlesP = Articles(X)
    Message = ArticlesP('title')+"\n\n"+ArticlesP('url')

Driver = webdriver.Firefox()
Driver.get('https://www.twitter.com')

time.sleep(5)

Username = 'SeleniumAutoT'
Password = 'SeleniumAutomation'

time.sleep(5)

LogInElement = Driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div/a[2]')
LogInElement.click()

time.sleep(5)

UsernameElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input')
UsernameElement.clear()
UsernameElement.send_keys(Username)

time.sleep(5)

PasswordElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input')
PasswordElement.clear()
PasswordElement.send_keys(Password)

time.sleep(5)

LogInNElement = Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button')
LogInNElement.click()

time.sleep(5)

TweetBoxElement = Driver.find_element_by_xpath('//*[@id="tweet-box-home-timeline"]')

for i in range(24):
    TweetBoxElement.send_keys(Message)

    time.sleep(5)

    TweetButtonElement = Driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div[2]/button')
    TweetButtonElement.click()

    time.sleep(3600)