from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
browser.find_element(By.ID, 'book').click()



x = browser.find_element(By.ID, 'input_value').text
y = calc(x)

input = browser.find_element(By.ID, 'answer')
input.send_keys(y)

button = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)

browser.quit()