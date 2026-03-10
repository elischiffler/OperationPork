import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

url = "https://docs.google.com/forms/d/e/1FAIpQLSf82SyhinhJlzbc8gUKmLJBy5bmbYVrqSm0idZQcq8dJXv2_A/viewform"

# Set a max wait time of 10 seconds
wait = WebDriverWait(driver, 10)

driver.get(url)

for i in range(300):
    try:
        # 1. Wait for the "Other" radio button container to appear
        other_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='radio' and @data-value='__other_option__']")))
        other_radio.click()
        print(f"Iteration {i+1}: Clicked 'Other' button...")

        # 2. Wait for the specific text input field to become visible/interactable
        other_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='text' and @aria-label='Other response']")))
        
        # 3. Type 'John Pork'
        other_input.send_keys("John Pork X Jack Collab")
        print(f"Iteration {i+1}: Entered 'John Pork'...")

        # 4. Find and click Submit
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Submit')]")))
        submit_button.click()
        
        # 5. Wait for "Submit another response" link to confirm submission and loop
        another_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Submit another response')]")))
        another_link.click()

        print(f"Success! Operation Pork iteration {i+1} is complete.")
        time.sleep(1)

    except Exception as e:
        print(f"Still having trouble on iteration {i+1}: {e}")
        driver.get(url)

driver.quit()