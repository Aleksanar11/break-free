from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import random
import subprocess

# Hardcoded username and password
email = 'aleksandar.zahariev@tek-experts.com'
password = 'Ewqzxc123!!!'

# Kill all existing Edge processes, but continue if no processes are found
try:
    subprocess.run(["taskkill", "/F", "/IM", "msedge.exe", "/T"], check=True)
except subprocess.CalledProcessError:
    pass  # Ignore the error if no Edge processes are found

# Set the path to your Edge executable
edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

# Set the path to your Edge WebDriver
edgedriver_path = r"C:\Users\3axo\Desktop\ne6to\msedgedriver.exe"

# Set the path to your Edge user profile
profile_path = "C:/Users/3axo/AppData/Local/Microsoft/Edge/User Data"

# Set up Edge options
edge_options = Options()
edge_options.add_argument(f"user-data-dir={profile_path}")
edge_options.add_argument("profile-directory=Default")  # Use the default profile directory

# Initialize Edge WebDriver with the specified options and service
service = Service(executable_path=edgedriver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# Open the desired webpage
driver.get('https://www.monetwfo-eu.com/Monet5/login/login.aspx')
time.sleep(5)

# Interact with the webpage
company_input = driver.find_element("name", 'txtTenantId')
company_input.send_keys('Tek Experts 1')

username_input = driver.find_element("name", 'txtUserName')
username_input.send_keys(email)

password_input = driver.find_element("name", 'txtPassword')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)
time.sleep(20)

# email_input2 = driver.find_element("name", 'loginfmt')
# email_input2.send_keys(email)
# email_input2.send_keys(Keys.ENTER)
# time.sleep(5)

# password_input2 = driver.find_element("name", 'passwd')
# password_input2.send_keys(password)
# password_input2.send_keys(Keys.ENTER)
# time.sleep(5)

# reduce_time_asked = driver.find_element("id", 'idSIButton9')
# reduce_time_asked.send_keys(Keys.ENTER)
# time.sleep(10)

statusListCombo = driver.find_element("id", 'statusListCombo')
statusListCombo = Select(statusListCombo)
statusListCombo.select_by_visible_text('03. Lunch')
Submit = driver.find_element("id", 'submitmanualStatusChange')
Submit.send_keys(Keys.ENTER)
time.sleep(random.randint(3580, 3620))

statusListCombo = driver.find_element("id", 'statusListCombo')
statusListCombo = Select(statusListCombo)
statusListCombo.select_by_visible_text('01. Available/Case Work')
Submit = driver.find_element("id", 'submitmanualStatusChange')
Submit.send_keys(Keys.ENTER)
time.sleep(7)

# Quit the browser
driver.quit()
