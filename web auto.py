from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
key=webdriver.common.keys.Keys()
driver = webdriver.Firefox()
driver.get("https://piratebaylive.com")
elem = driver.find_element_by_xpath('/html/body/main/section/form/div[1]/input')
elem.send_keys("pokemon")
elem.send_keys(key.RETURN)
wait = WebDriverWait(driver, 10)
men_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/main/div/section/ol/li[6]/span[4]/a/img")))
ActionChains(driver).move_to_element(men_menu).perform()
el = driver.find_element_by_xpath('/html/body/main/div/section/ol/li[6]/span[4]/a/img')
el.click()

wait2 = WebDriverWait(driver, 10)
men_menu = wait2.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div/div/div/a[2]")))
ActionChains(driver).move_to_element(men_menu).perform()
b = driver.find_element_by_xpath("/html/body/div/div/div/a[2]")
b.click()














