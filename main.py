import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

clicker = driver.find_element(By.ID, "cookie")
duration = 5
whole_duration = 300

# Record the start time
start_time = time.time()

# Loop to click the button as fast as possible until the specified time elapses
while time.time() - start_time < whole_duration:
    starter = time.time()
    while time.time() - starter < duration:
        clicker.click()

    result = driver.find_element(By.ID, "money")
    money = int(result.text.replace(",", ""))  # Convert to int, removing commas if present

    cursor_price = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split()[-1].replace(",", ""))
    grandma_price = int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split()[-1].replace(",", ""))
    factory_price = int(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split()[-1].replace(",", ""))
    mine_price = int(driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.split()[-1].replace(",", ""))
    shipment_price = int(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split()[-1].replace(",", ""))


    try:
        if money >= shipment_price:
            driver.find_element(By.ID, "buyShipment").click()
        elif money >= mine_price:
            driver.find_element(By.ID, "buyMine").click()
        elif money >= factory_price:
            driver.find_element(By.ID, "buyFactory").click()
        elif money >= grandma_price:
            driver.find_element(By.ID, "buyGrandma").click()
        elif money >= cursor_price:
            driver.find_element(By.ID, "buyCursor").click()
    except Exception as e:
        print(f"An error occurred: {e}")


print(f"cookies/second: {driver.find_element(By.ID,"cps").text.split()[-1].replace(",", "")}")
driver.quit()
