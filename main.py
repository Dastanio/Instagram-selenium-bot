from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time 
import random



class InstagramBot():

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.browser = webdriver.Chrome("/Users/user/Desktop/any_python_scripts/InstagramBot/chromedriver")

        def close_browser(self):

            self.browser.close()
            self.browser.quit()

        def login(self):

            browser = self.browser
            browser.get('http://www.instagram.com')
            time.sleep(random.randrange(1,5))

            username_input = browser.find_element_by_name('username')
            username_input.clear()  
            username_input.send_keys(username)

            time.sleep(2)

            password_input = browser.find_element_by_name('password')
            password_input.clear()  
            password_input.send_keys(password) 

            password_input.send_keys(Keys.ENTER)
            time.sleep(5)

        def like_photo_by_hashtag(self, hashtag):

            browser = self.browser

            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
            time.sleep(3)

            for i in range(1, 4):
                browser.execute_script('window.scrollTo(0, document.body.scrollHeight); ')
                time.sleep(random.randrange(3,  5))

            hrefs = browser.find_elements_by_tag_name('a')
            post_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]

            for i in post_urls:
                try:
                    browser.get(i)
                    time.sleep(1)
                    like_button = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
                    time.sleep(3)
                except Exception as ex:
                    print(ex)
        
        def xpath_exists(self, url):

            browser = self.browser
            try:
                browser.find_element_by_xpath(url)
                exist = True

            except NoSuchElementException:
                exist = False

            return exist

        def put_exactly_like(self, userpost):
            