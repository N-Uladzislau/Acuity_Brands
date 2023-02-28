import random
import time
import driver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium.webdriver import ActionChains
faker_class = Faker()
F = Faker()
F.STATE = Faker(["en_US"])



# URL for main Website
main_url = "https://www.acuitybrands.com/"

# Main logo
main_logo = '//*[@class="header__main__logo"]'

# media on main page
media = "//a[@class='header__main__logo']"

# Distech main logo
distech_logo = '//*[@alt="Distech logo"]'


# Time delay 1-3
def delay1_3():
    time.sleep(random.randint(1, 3))


# Check API Fun
def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("URL has", requests.get(driver.current_url).status_code , "as Status Code")
    else:
        print("API response code is not 200")

# verify Title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print(f'Page has, {driver.title} as Page title')
    # scr of page if page has different title
    driver.get_screenshot_as_file(f'Page has different {title}.png')
    if not title in driver.title:
        raise Exception(f'Page {title} has wrong Title')


# Switch frame on main menu
def switch_main_frame(driver):
    try:
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@title='AB Home, 2022 EarthLIGHT Popup']"))
        print("frame is switched on 'Main page'")
    except NoSuchElementException:
        print("Frame wasn't switched")

# Close the ads if it's present on web page
def close_ad(driver):
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ufw-item-container-close"]')))
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="ufw-item-container-close"]')))
        driver.find_element(By.XPATH, '//*[@class="ufw-item-container-close"]').click()
    except NoSuchElementException:
        print("No ads on the page")

# create payment for "Lithonia Lighting" with library Faker
def payment(driver):
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    # create random email, check if placeholder is visible and clickable
    wait.until(EC.visibility_of_element_located((By.ID, "email")))
    wait.until(EC.element_to_be_clickable((By.ID, "email")))
    # clear field
    driver.find_element(By.ID, "email").clear()
    # inter random email
    driver.find_element(By.ID, "email").send_keys(F.email())
    # verify that County/Region is "United States"
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@name="countryCode"]//*[text()="United States"]')))
    # input First Name (optional) ??? how it could be ? first name is optional
    # verify that placeholder for "First name" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'firstName')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'firstName')))
    # clear field
    driver.find_element(By.NAME, 'firstName').clear()
    # inter random Name
    driver.find_element(By.NAME, "firstName").send_keys(F.first_name())
    # input Last Name
    # verify that placeholder for "Last name" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'lastName')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'lastName')))
    # clear field
    driver.find_element(By.NAME, 'lastName').clear()
    # inter random Name
    driver.find_element(By.NAME, "lastName").send_keys(F.last_name())
    # verify that placeholder for "Address" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'address1')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'address1')))
    # clear field
    driver.find_element(By.NAME, 'address1').clear()
    # inter random Address
    driver.find_element(By.NAME, "address1").send_keys(F.STATE.street_address())
    # verify that placeholder for "Apartment, suite, etc." is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'address2')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'address2')))
    # clear field
    driver.find_element(By.NAME, 'address2').clear()
    # inter random Apartment, suite, etc.
    driver.find_element(By.NAME, "address2").send_keys(F.STATE.secondary_address())
    # verify that placeholder for "City" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'city')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'city')))
    # clear field
    driver.find_element(By.NAME, 'city').clear()
    # inter random City
    driver.find_element(By.NAME, "city").send_keys(F.STATE.city())
    # I don't choose State in leave "California" and just verify that "California" exist
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[text()="California"]')))
    # verify that placeholder for "Zipcode" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.NAME, 'postalCode')))
    wait.until(EC.element_to_be_clickable((By.NAME, 'postalCode')))
    # clear field
    driver.find_element(By.NAME, 'postalCode').clear()
    # inter random Zipcode
    driver.find_element(By.NAME, "postalCode").send_keys(F.STATE.zipcode())
    time.sleep(1)
    # verify that button "Continue to shipping" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH,
                    '//button[@type="submit" and @class="aqHkS Mlpfi bAS_j okQ4n wkoOa DmJZe Lot1G EmqTg"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH,
                    '//button[@type="submit" and @class="aqHkS Mlpfi bAS_j okQ4n wkoOa DmJZe Lot1G EmqTg"]')))


def search_field(driver):
    wait = WebDriverWait(driver, 10)
    # verify that "Search Field" is visible and clickable
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@title="Enter keywords to search"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@title="Enter keywords to search"]')))
    # Clear Field
    driver.find_element(By.XPATH, '//*[@title="Enter keywords to search"]').clear()




