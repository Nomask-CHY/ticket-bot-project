from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup the webdriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to a website
driver.get("https://www.google.com")

# Keep the browser open until you manually close it
input("Press Enter to close the browser...")
driver.quit()