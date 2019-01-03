import sys
import time
import datetime
import calendar

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def click(driver, HTML_ITEM):
    element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, HTML_ITEM)))
    element.click()


def fill(driver, HTML_ITEM, text):
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, HTML_ITEM))).send_keys(text)


def enter(driver, HTML_ITEM):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, HTML_ITEM))).send_keys(Keys.ENTER)


def printSeleniumElement(element):
    try:
        print('/-----------------')
        print(element.text)
        print(element.tag_name)
        print(element.parent)
        print(element.location)
        print(element.size)
    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        print('\-----------------')


def printSeleniumElements(elements, elementName):
    print("-------elements: " + elementName + " -------")
    for element in elements:
        printSeleniumElement(element)


def login_cloudconsole(driver):
    driver.get("https://console.cloud.google.com/cloudshell/editor")
    fill(driver, '#identifierId', "ckwong1204a")
    click(driver, '#identifierNext')
    time.sleep(1)
    fill(driver, '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input', "hkjayjay")
    click(driver, '#passwordNext > content')
    time.sleep(60)


def input_console_command(driver, command):
    time.sleep(1)
    driver.find_element_by_tag_name('body').send_keys(command)
    time.sleep(2)
    driver.find_element_by_tag_name('body').send_keys(Keys.RETURN)
    time.sleep(2)

def swith_to_devshell_n(driver, devshell_n):
    # reset drive to top content
    driver.switch_to.default_content()
    # select all id contains "devshell-:"   (iframe)
    iframes_all = driver.find_elements_by_xpath("//*[contains(@id,'devshell-:')]")
    # switch to iframe devshell_n
    driver.switch_to.frame(iframes_all[devshell_n])
    iframes1 = driver.find_elements_by_tag_name('iframe')
    time.sleep(1)
    driver.switch_to.frame(iframes1[0])


def add_new_devshell(driver):
    driver.switch_to.default_content()
    click(driver,
          "body > pan-shell > div > div.pan-shell-main-container.layout-row.flex > div > div.layout-row > pan-lazy-loader > pan-dev-shell > div > div.p6n-devshell-header.p6n-action-bar > div:nth-child(5) > pan-devshell-new-tab-menu > div > jfk-button > pan-icon")
    time.sleep(10)


def main():
    print("Trigger time: ", datetime.datetime.now(), calendar.day_name[datetime.datetime.today().weekday()])
    if datetime.datetime.today().weekday() > 4:
        return

    try:
        chrome_path = ".\chromedriver.exe"
        driver = webdriver.Chrome(chrome_path)

        login_cloudconsole(driver)

        # tab 1   ###############################
        add_new_devshell(driver)
        swith_to_devshell_n(driver, 0)
        input_console_command(driver, "date")
        input_console_command(driver, "cd ~/ckquant/cloudshell")
        input_console_command(driver, "./f1_run.sh")

        # new tab ###############################
        add_new_devshell(driver)

        # tab 2   ###############################
        swith_to_devshell_n(driver, 1)
        input_console_command(driver, "date")
        input_console_command(driver, "cd ~/ckquant/cloudshell")
        input_console_command(driver, "./f2_futu.sh")

        # close all connection  ##################
        time.sleep(100)
        input_console_command(driver, "exit")
        input_console_command(driver, "exit")
        input_console_command(driver, "exit")

        print("Trigger done: ", datetime.datetime.now())

    except:
        print("Unexpected error:", sys.exc_info()[0])
    finally:
        driver.quit()

if __name__ == '__main__':
    main()

# cmd for "Task Scheduler" for this trigger
# C:\Work\Futu\ckquant\cloudshellControl\trigger.py >> log.txt
