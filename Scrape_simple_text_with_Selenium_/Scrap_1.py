# Print a simple greeting
print("Hello")

# Import necessary modules from the Selenium library
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
    driver.get("http://automated.pythonanywhere.com")
    
    # Return the configured WebDriver instance
    return driver

# Define a function to interact with the WebDriver (not executed in the provided code)
def main():
    # Call the 'get_driver' function to obtain a WebDriver instance
    driver = get_driver()
    
    # Find an HTML element using XPath
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    
    # Return the text content of the found element
    return element.text

# Call the 'main' function and print the result
print(main())

# Perform any other actions as needed (Note: Actions after calling 'main' are not executed in the provided code)



