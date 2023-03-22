import os
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

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.reddit.com/user/wanomy')

wait = WebDriverWait(driver, 60)

avatar_login_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._3F1tNW0P4Ff182mO_CefIg._2iuoyPiKHN3kfOoeIQalDT._10BQ7pjWbeYP63SAPNS8Ts.HNozj_dKjQZ59ZsfEegz8._34mIRHpFtnJ0Sk97S2Z3D9")))
avatar_login_button.click()

login_iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._25r3t_lrPF3M6zD2YkWvZU")))
driver.switch_to.frame(login_iframe)

username_input = driver.find_element(By.NAME, 'username')
if driver.switch_to.active_element == username_input:
    username_input.send_keys(os.environ['REDDIT_USERNAME'])

password_input = driver.find_element(By.NAME, 'password')
password_input.send_keys(os.environ['REDDIT_PASSWORD'])

login_button = driver.find_element(By.CSS_SELECTOR, '.AnimatedForm__submitButton.m-full-width.m-modalUpdate ')
wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "._1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3")))
login_button.click()

driver.switch_to.default_content()

wait.until_not(EC.presence_of_element_located((By.CSS_SELECTOR, "._3-lF5kPDkSGfnVUW_GtvUV.icon.icon-user")))

while True:
    try:
        style_avatar_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._3F1tNW0P4Ff182mO_CefIg._2iuoyPiKHN3kfOoeIQalDT._10BQ7pjWbeYP63SAPNS8Ts.HNozj_dKjQZ59ZsfEegz8._34mIRHpFtnJ0Sk97S2Z3D9")))
        style_avatar_button.click()

        shop_pill = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._pillOption_1such_54")))
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "._1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3")))
        shop_pill.click()

        browse_all = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._browseAll_1nklo_4")))
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "._1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3")))
        browse_all.click()

        browse_all_content = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "._galleryContainer_fjnnf_1")))
        with open('old_page.txt', 'r') as file:
            old_page_contents = file.read()
            if (old_page_contents == browse_all_content.get_attribute("outerHTML")):
                print("Nothing changed.")
                close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._closeButton_1ujsh_1._closeBtn_1upjl_56")))
                wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "._1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3")))
                close_button.click()
            else:
                try:
                    running_snoo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._title_14e8h_10._emptyTitle_14e8h_29")))
                    if (running_snoo.text == "These collectibles sure go fast"):
                        close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "._closeButton_1ujsh_1._closeBtn_1upjl_56")))
                        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "._1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3")))
                        close_button.click()
                except:
                    make_twilio_call()
                    print("AVATARS MIGHT HAVE DROPPED!")
                    driver.quit()
    except:
        make_twilio_call()
        driver.quit()
