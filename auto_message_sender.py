from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import username, password
from selenium.webdriver.chrome.options import Options
import time 
import random


def monitoring_direct(username, password):
    browser = webdriver.Chrome('/Users/user/Desktop/any_python_scripts/InstagramBot/chromedriver')
    try:
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

        direct_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
        time.sleep(5)

        # ls_hrefs = browser.find_elements_by_tag_name('a')

        # print([i.get_attribute('href') for i in ls_hrefs if '/t/' in i.get_attribute('href') ])


        while True:
            time.sleep(1)
            messages_text = browser.find_elements_by_class_name('se6yk')
            for i in messages_text[0:1]:

                text = open('message.txt', 'r').read()
                if i.text != text:
                    with open('message.txt', 'w') as f:
                        f.write(str(i.text) )

                    ls_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a').click()
                                                              
                    txt = browser.find_element_by_tag_name('textarea')
                    txt.send_keys('test')
                    txt.send_keys(Keys.ENTER)



                    print('Опа ктото что то написал')
                    
                    
                else:
                    print('Все как обычно некто нечего не писал')


            time.sleep(5)
    
        
    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()

monitoring_direct(username, password)