from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run without a visible browser UI
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues
options.add_argument("--window-size=1920,1080")  # Set screen size
options.add_argument("--disable-gpu")  # Disable GPU rendering
options.add_argument("--remote-debugging-port=9222")  # Enable remote debugging

# Initialize WebDriver (Selenium will auto-download ChromeDriver)
driver = webdriver.Chrome(options=options)

try:
    # Open the website
    url = "https://zora3.vercel.app/"
    driver.get(url)

    # Wait until the element is visible
    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/horoscope_of_the_month']"))
    )

    # Click the element
    element.click()
    print("Clicked on 'Horoscope of the Month'!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()  # Close the browser
