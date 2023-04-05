
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    #Informations 
    email = 'user'
    password = 'password'

    #Creating a new Instance of the browser
    browser = uc.Chrome(driver_executable_path='./chromedriver/chromedriver.exe')

    
    browser.get('https://accounts.google.com/')
    
    email_field = browser.find_element(By.XPATH,'//input')
    email_field.click()
    email_field.send_keys(email)
    browser.reconnect(1.5)
    email_field.send_keys(Keys.ENTER) 
    browser.reconnect(5.0)


    try:
        try_again = browser.find_element(By.XPATH,"//*[@aria-label='Try again']")
        try_again.click()
        browser.reconnect(4)
        email_field = browser.find_element(By.XPATH,'//input')
        email_field.click()
        email_field.send_keys(email)
        browser.reconnect(4)
        email_field.send_keys(Keys.ENTER) 
        browser.reconnect(5.0)
    except :
        print('Error')
        

    password_field = browser.find_element(By.XPATH,"//input[@type='password']")
    password_field.click()
    password_field.send_keys(password)
    browser.reconnect(1.0)
    password_field.send_keys(Keys.ENTER)
    browser.reconnect(1.5)
    

    #Going to youtube after a succesfull connection
    browser.get('https://www.youtube.com/')
    browser.reconnect(2)


    #Making screen size smaller to make the script works for all the devices 
    browser.set_window_size(800,600)
    browser.reconnect(1)
    yt_menu_icon = browser.find_elements(By.XPATH,"//yt-icon[@id='guide-icon']")
    yt_menu_icon[0].click()
    browser.reconnect(2)

    #
    subscribed_to = browser.find_elements(By.XPATH,"//*[@id='img'][@height='24']")
    #
    browser.get('https://www.youtube.com/')
    browser.reconnect(2)
    

    for s in subscribed_to :
        yt_menu_icon = browser.find_elements(By.XPATH,"//yt-icon[@id='guide-icon']")
        yt_menu_icon[0].click()
        browser.reconnect(3)
    	
        subscribed_to = browser.find_elements(By.XPATH,"//*[@id='img'][@height='24']")
        browser.reconnect(3)


        s = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='img'][@height='24']")))
        s.click()
       
        subscribe_button = browser.find_element(By.XPATH,"//div//ytd-subscribe-button-renderer")
        subscribe_button.click()
        browser.reconnect(2)

        subscribe_button = browser.find_element(By.XPATH,"//yt-formatted-string[text()='Unsubscribe']")
        subscribe_button.click()
        browser.reconnect(2)

        confirmation_button = browser.find_element(By.XPATH,"//button[@aria-label='Unsubscribe']")
        confirmation_button.click()
        browser.reconnect(2)

        browser.get('https://www.youtube.com/')
        browser.reconnect(2)
    








    while True:
        pass



if __name__ == '__main__' :
    main()