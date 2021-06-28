from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.instagram.com/p/CP2VnuNMc65/?utm_medium=share_sheet")
time.sleep(15)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div').click()
#//*[@id="react-root"]/div/div/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span/svg
time.sleep(100)