"""What this code does"""
#practice clicking and finding a stock on yahoo.finance 
# from yahoo home page
# download datat to csv file


# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
# Replace 'path/to/chromedriver.exe' with the actual path to your ChromeDriver executable
ser_obj = Service(r"C:\Users\timde\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")

# Define a function to get a configured WebDriver instance
def get_driver():
    # Create an instance of ChromeOptions
    options = webdriver.ChromeOptions()
    
    # Add various ChromeOptions to configure the behavior of the WebDriver
    options.add_argument("disable-infobars")  # Disable info bars
    options.add_argument("start-maximized")  # Start the browser in maximized mode
    options.add_argument("disable-dev-shm-usage")  # Disable shared memory usage
    options.add_argument("no-sandbox")  # Disable sandboxing
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude switches for automation
    options.add_argument("disable-blink-features=AutomationControlled")  # Disable certain Blink features controlled by automatio
    # Create an instance of WebDriver with the configured options
    driver = webdriver.Chrome(service=ser_obj, options=options)
    
    # Open a website, for example, 'http://automated.pythonanywhere.com'
    driver.get("https://www.google.com/")
 
    # Return the configured WebDriver instance
    return driver



# Define a function to interact with the WebDriver (not executed in the provided code)
def main():
    # Call the 'get_driver' function to obtain a WebDriver instance
    driver = get_driver()
    # Find an HTML element using xpath or id
    time.sleep(5)
    # open google and accept cookies
    driver.find_element(by="xpath", value = "/html/body/div[2]/div[3]/div[3]/span/div/div/div/div[3]/div[1]/button[1]").click()
    time.sleep(5)
    #search for yahoo in google
    driver.find_element(by="xpath", value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea").send_keys("yahoo" + Keys.RETURN)
    time.sleep(5)
    #open yahoo main link, link 3 on google
    driver.find_element(by="xpath", value="/html/body/div[5]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[1]/div/div/span/a/h3").click()
    time.sleep(5)
    # accept cookies in yahoo
    driver.find_element(by="xpath", value="/html/body/div/div/div/div/form/div[2]/div[2]/button[1]").click()
    time.sleep(5)
    # open yahoo finance link
    driver.find_element(by="xpath", value="/html/body/header/div/div/div/div/div/div[2]/div/div[2]/nav/ul/li[2]/a").click()
    time.sleep(5)
    driver.find_element(by="id", value="yfin-usr-qry").send_keys("sofi" + Keys.RETURN)
    time.sleep(5)
    print(driver.current_url)
    driver.find_element(by="xpath", value="/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div/section/div/ul/li[5]/a/span").click()

  
#  Call the 'main' function and print the result
print(main())
