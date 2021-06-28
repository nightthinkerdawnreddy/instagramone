import mysql.connector
import time

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="bhaskar",
#  password="Bhas3434@",
#  database="djangoone"
#)
#mycursor=mydb.cursor()
#mycursor.execute("select * from testing_urlposting")
#results=mycursor.fetchall()
#mycursor.execute("delete form testing_urlposting where urlpost=h%")
#for i in results:
#    print(i[1])
###selenium part starts
from selenium import webdriver
driver=webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(180)
#driver.execute_script("window.open('');")
#driver.switch_to.window(driver.window_handles[1])
#new_url="https://www.instagram.com/p/CP2VnuNMc65/?utm_medium=share_sheet"
#driver.get(new_url)
#driver.close()

#username=driver.find_element_by_name("username")
#password=driver.find_element_by_name("password")
#username.send_keys("dawnreddy1111")
#the thing is that the files keeps on quering the database of the table of the final for now leave it and continue to the next 
#password.send_keys("Bhas3434@")
#driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
idone=[]
while True:
  mydb = mysql.connector.connect(
    host="localhost",
    user="bhaskar",
    password="Bhas3434@",
    database="djangoone"
  )
  mycursor=mydb.cursor()
  mycursor.execute("select * from testing_urlposting")
  results=mycursor.fetchall()
  for i in results:
    print(i[1])
    if i[0] not in idone:
      driver.execute_script("window.open('');")
      driver.switch_to.window(driver.window_handles[1])
      new_url=i[1]
      driver.get(new_url)
      time.sleep(15)
      driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div').click()
      time.sleep(5)
      driver.close()
      driver.switch_to.window(driver.window_handles[0])
      driver.get("https://www.yahoo.com")
      time.sleep(5)
      idone.append(i[0])
      #time.sleep(10)s
    

    
#print(results)

#print(mydb)