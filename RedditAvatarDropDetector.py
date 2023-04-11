import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def make_twilio_call():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>Nothing Changed Dont Worry!</Say></Response>',
        to='+919392062662',
        from_='+15077044568'
        )

options = webdriver.ChromeOptions()
options.add_argument('--use-gl=angle')
options.add_argument(r'--user-data-dir=C:\Users\Charan\AppData\Local\Google\Chrome\User Data')
options.add_argument(r'--profile-directory=Default')
options.add_argument('start-maximized')

driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get('https://www.reddit.com/avatar/shop/gallery?utm_medium=web2x&utm_source=share')

wait = WebDriverWait(driver, 60)

while True:
    try:
        running_snoo_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '._title_14e8h_10._emptyTitle_14e8h_29')))
        if(running_snoo_text.text == 'These collectibles sure go fast'):
            driver.find_elements(By.CSS_SELECTOR, '._pillOption_1such_54')[1].click()
            time.sleep(0.5)
            driver.find_element(By.CSS_SELECTOR, '._pillOption_1such_54').click()
        else:
            make_twilio_call()
            break

    except:
        make_twilio_call()
        break

input("Press any key to close the browser...")

