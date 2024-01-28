from time import sleep
import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url="https://www.memrise.com/login/?next=/home/"
wordsObj = {}

def getDetails():
    print("--------------------------------------------------------")
    print("Welcome to Salon Members. (Selenium - Memrise? Get it?)")
    print("--------------------------------------------------------")
    sleep(0.5)
    print("This program will ask you to enter your username and password. These are not stored anywhere, and are only temporary variables to sign you into your Memrise account.")
    sleep(0.5)
    print("You will not see your password as you type it. This is normal. Python secures passwords by not showing them as you type them.")
    print("Also, when the website loads and you are logged in, you will be given ~15 seconds to get rid of any pop-ups that may appear. This is to ensure that they do not interfere with the program.")
    print("--------------------------------------------------------")
    usern = input("Enter your Memrise username (with email): ")
    passwd = getpass.getpass("Enter your Memrise password: ")
    print("--------------------------------------------------------")
    logInObject = {
        "username": usern,
        "password": passwd
    }
    return logInObject["username"], logInObject["password"]

def login(username, password):
    usernameElement = driver.find_element(By.ID, "username")
    usernameElement.send_keys(username)
    passworElement = driver.find_element(By.ID, "password")
    passworElement.send_keys(password)
    sleep(0.5)
    elem = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[3]/button")
    elem.send_keys(Keys.RETURN)

def selectLesson():
    # NEEDS FIXING!!
    lessonTypeSelect = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/div/div[4]/div/div[2]/div[2]/div/button")
    lessonTypeSelect.send_keys(Keys.RETURN)
    sleep(2)
    MainLessonType = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[2]/div/div/a")
    print(MainLessonType.text)
    if MainLessonType == "Learn new words":
        MainLessonType.send_keys(Keys.RETURN)
    else:
        lessonTypeLearn = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div/div/div/div[3]/div/div/div[1]/div/a")
        lessonTypeLearn.send_keys(Keys.RETURN)

def learn():
    # Currently, this only gets the words from the opening page of the learning session. TODO!! 
    global wordsObj
    currPoints = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/span/div/span")
    print(currPoints.text)
    learningLanguage = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div/div/div[1]/label").text
    nativeLanguage = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div/div/div[2]/label").text
    langWord = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div/div/div[1]/h2").text
    nativeWord = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div/div[4]/div/div/div/div[2]/h3").text
    wordsObj[learningLanguage] = []
    wordsObj[nativeLanguage] = []
    wordsObj[learningLanguage].append(langWord)
    wordsObj[nativeLanguage].append(nativeWord)
    print(wordsObj)

username, password = getDetails()

sleep(1)
driver = webdriver.Edge() # or Chrome() or Ie() or Firefox() depending on your preferred web browser. MS Edge  comes preinstalled on Windows hence is used here.
sleep(2)
driver.get(url)
sleep(4)
login(username, password)
sleep(6)
selectLesson()
sleep(5)
learn()
sleep(100)
driver.quit()
