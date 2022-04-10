from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

url = "https://pypi.org"

driver = webdriver.Firefox()
driver.get(url)

text_input = driver.find_element_by_class_name("search-form__search.large-input")
text_input.send_keys("selenium")
driver.find_element_by_class_name("fa.fa-search").click()