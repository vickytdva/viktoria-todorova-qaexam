from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration

input_header = '//*[@id="content"]/ul/li[27]/a'
input_content = 'content'
input_field = '//*[@id="content"]/div/div/div/input'

def click_input_tab():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/")
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_header)))
    elem.click()
    driver.quit()

def input_content_visible():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/")
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, input_content)))
    assert elem.is_displayed(), "Input content is not visible"
    driver.quit()

def send_correct_keys_to_input():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/")
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_field)))
    elem.send_keys('123321')
    assert elem.get_attribute("value") == '123321', "Incorrect value entered"
    driver.quit()

def send_incorrect_keys_to_input():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/")
    elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_field)))
    elem.send_keys('abc')
    assert elem.get_attribute("value") == 'abc', "Incorrect value entered"
    driver.quit()

# Execute the functions
click_input_tab()
input_content_visible()
send_correct_keys_to_input()
send_incorrect_keys_to_input()
