from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://codeforces.com/enter')
driver.implicitly_wait(5)
def login(username, password):
    driver.find_element(By.NAME, 'handleOrEmail').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.CLASS_NAME, 'submit').click()

def add_friend(username):
    driver.get(f"https://codeforces.com/profile/{username}")
    try:
        driver.find_element(By.CLASS_NAME, 'friendStar')
    except:
        return 
    x = driver.find_elements(By.CLASS_NAME, 'addFriend')
    if(len(x) > 0):
        x[0].click()


login('YOUR-HANDLE', 'YOUR-PASSWORD')
sleep(5)
data = json.load(open('friends.json'))
for friend in data['result']:
    add_friend(friend)
    sleep(1)
