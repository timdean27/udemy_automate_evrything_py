"""What this code does"""
# learn how to write a script which logs into form with 
# user name and password
# once script logs in it will press home home page
# can use ID to find element
"""log in using email and password and click on element once logged in"""


# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
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
    options.add_argument("disable-blink-features=AutomationControlled")  # Disable certain Blink features controlled by automation
    
    # Create an instance of WebDriver with the configured options
    driver = webdriver.Chrome(service=ser_obj, options=options)
    
    # Open a website, for example, 'http://automated.pythonanywhere.com'
    driver.get("https://automated.pythonanywhere.com/login/")
    
    # Return the configured WebDriver instance
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    # split string and extract specific part
    output = float(text.split(": ")[1])
    return output

# Define a function to interact with the WebDriver (not executed in the provided code)
def main():
    # Call the 'get_driver' function to obtain a WebDriver instance
    driver = get_driver()
    # Find an HTML element using id
    # sending keyboard input of "automated"
    # keys will type in username box
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(2)
    print(driver.current_url)

    driver.find_element(by="xpath" , value="/html/body/nav/div/a").click()
    time.sleep(2)
    print(driver.current_url)
#  Call the 'main' function and print the result
print(main())

# Perform any other actions as needed (Note: Actions after calling 'main' are not executed in the provided code)

