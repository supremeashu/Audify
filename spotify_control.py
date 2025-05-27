
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def play_song(driver, song_name):
    wait = WebDriverWait(driver, 15)
    try:
        # # Click on Search in sidebar
        # print("Clicking search...")
        # search_button = driver.find_element(By.XPATH, '//button[@data-testid="play-button"]')
        # search_button.click()
        # time.sleep(3)

        # Enter song name in search box
        search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="What do you want to play?"]')))
        search_box.clear()
        search_box.send_keys(song_name)
        time.sleep(1)
        search_box.send_keys(Keys.RETURN)
        time.sleep(1)

        print("Hovering over first song card...")
        # Hover over the song card
        song_card = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ix_8kg3iUb9VS5SmTnBY']//button[@aria-label='Play']")))
        ActionChains(driver).move_to_element(song_card).perform()
        song_card.click()

        # # Click on the first song result
        # print("Clicking first result...")
        # first_result = song_card.find_element(By.XPATH, ".//button[@aria-label='Play' or @aria-label='Pause']")

        # first_result.click()
        print(f"🎵 Playing '{song_name}'")

        # time.sleep(30)

    except Exception as e:
        print("❌ Error while trying to play song:", e)
 






# default settup code
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# options = webdriver.ChromeOptions()
# options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"  # adjust if different

# driver = webdriver.Chrome(options=options)
# driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# title = driver.title

# driver.implicitly_wait(0.5)

# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

# text_box.send_keys("Selenium")
# submit_button.click()

# message = driver.find_element(by=By.ID, value="message")
# text = message.text
# time.sleep(6)
# driver.quit()