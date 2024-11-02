import logging
import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import datetime


options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument(
    "user-data-dir=C:\\Users\\Utente\\AppData\\Local\\Google\\Chrome\\User Data")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

food_lunch = [
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
    "150g of spaghetti served with a pesto sauce crafted from fresh basil, Parmesan cheese, pine nuts, garlic, and extra virgin olive oil, complemented by halved cherry tomatoes that are lightly cooked and placed on top",
]

vegetables_lunch = [
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables"
]


food_dinner = [
    "5 scrambled eggs",
    "5 scrambled eggs",
    "5 scrambled eggs",
    "5 scrambled eggs",
    "5 scrambled eggs",
    "5 scrambled eggs",
    "5 scrambled eggs",
]

vegetables_dinner = [
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables",
    "vegetables"
]


def push_up_upload(number):
    # 0 for lunch
    # 1 for dinner
    # days i eat lunch at fribley
    flibely = [2,5,6]
    # days i dont eat lunch
    nolunch = [0,1,3,4]
    leutener = False
    today = datetime.datetime.today()
    day_num = today.weekday()

    date_format = "%m/%d/%Y"

    if (number == 0):
        print('Ordering lunch')
        foodlist = food_lunch
        veglist = vegetables_lunch
        ordertime = '12:30 PM'
        if day_num in nolunch:
            return
        if day_num in flibely:
            leutener = False
    else:
        print('Ordering dinner')
        foodlist = food_dinner
        veglist = vegetables_dinner
        ordertime = '6:25 PM'
    print(day_num)

    logging.info(f'Starting uploading the video')
    bot = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), chrome_options=options)
    bot.get("https://www.cognitoforms.com/CWRUBA/CWRUSpecialDietOrderForm")
    time.sleep(2)

    inputs = ['', 'axm2022@case.edu', "2162589844", today.strftime(
        date_format), ordertime, '', foodlist[day_num] + ' with '+veglist[day_num], "rice"]
    speed = 0.25
    for i in range(8):
        if (i == 0):
            textbox = bot.find_element(By.XPATH, '//*[@id="cog-input-auto-0"]')
            time.sleep(speed)
            textbox.click()
            time.sleep(speed)
            textbox.clear()
            textbox.send_keys("Alessandro")

            textbox = bot.find_element(By.XPATH, '//*[@id="cog-input-auto-1"]')
            time.sleep(speed)
            textbox.click()
            time.sleep(speed)
            textbox.clear()
            textbox.send_keys("Mason")

        elif (i == 5):
            textbox = bot.find_element(By.XPATH, '//*[@tabindex="0"]')
            time.sleep(speed)
            textbox.click()
            time.sleep(1)

            if (leutener == False):
                textbox = bot.find_element(
                    By.XPATH, '//*[@class="el-radio cog-checkable__item"]')
                time.sleep(speed)
                textbox.click()
                time.sleep(1)
        else:
            textbox = bot.find_element(By.XPATH, '//*[@id="cog-'+str(i)+'"]')
            time.sleep(speed)
            textbox.click()
            time.sleep(speed)
            textbox.clear()
            textbox.send_keys(inputs[i])

    """ # this actually orders food
    textbox = bot.find_element(
        By.XPATH, ' //*[@class="el-button cog-button--has-status cog-button--primary cog-button--navigation cog-button--submit el-button--default cog-button"]')
    time.sleep(speed)
    textbox.click() """
    time.sleep(1)
    bot.quit()


if __name__ == "__main__":
    push_up_upload(0) 
    push_up_upload(1)
