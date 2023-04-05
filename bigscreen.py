import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    #Informations 
    email = 'user'
    password = 'password'

    #Creating a new Instance of the browser
    browser = uc.Chrome(driver_executable_path='./chromedriver/chromedriver.exe')
    browser.maximize_window()
    browser.get('https://accounts.google.com/')
    

    #Connecting to User Account
    email_field = browser.find_element(By.XPATH,'//input')
    email_field.click()
    email_field.send_keys(email)
    browser.reconnect(1.5)
    email_field.send_keys(Keys.ENTER) 
    browser.reconnect(5.0)
    password_field = browser.find_element(By.XPATH,"//input[@type='password']")
    password_field.click()
    password_field.send_keys(password)
    browser.reconnect(1.0)
    password_field.send_keys(Keys.ENTER)
    browser.reconnect(1.5)
    

    #Redirecting to youtube after a succesfull connection
    browser.get('https://www.youtube.com/')
    browser.reconnect(2)



    #List of subscribed channels name
    subscribed_to = browser.find_elements(By.XPATH,"//*[@id='img'][@height='24']")
    

    for s in subscribed_to :
        s.click()
        channels = []
        browser.implicitly_wait(2)
        channel_name = browser.find_element(By.XPATH,'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[1]/ytd-channel-name/div/div/yt-formatted-string')
        channels.append(channel_name.text)

        
        browser.implicitly_wait(3)
        subscribe_button = browser.find_element(By.XPATH,"//ytd-subscription-notification-toggle-button-renderer-next")
        subscribe_button.click()
        browser.reconnect(2)

        subscribe_button = browser.find_element(By.XPATH,"//yt-formatted-string[text()='Unsubscribe']")
        subscribe_button.click()
        browser.reconnect(2)

        confirmation_button = browser.find_element(By.XPATH,"//button[@aria-label='Unsubscribe']")
        confirmation_button.click()
        browser.reconnect(2)


    print(f'\n\n\nSuccesfully Unsubscribed To : \n\n\t{channels}\n\n\n')
    while True:
        pass



if __name__ == '__main__' :
    main()