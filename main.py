from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import quote
import time
import os

# Configurations
login_time = 45       # Time for login (in seconds)
new_msg_time = 10     # Time to wait for a new message to load (in seconds)
send_msg_time = 10    # Time to wait for a message to send (in seconds)
upload_time = 15      # Time to wait for the video upload to complete (in seconds)
country_code = 91     # Set your country code

# Video file path
video_path = r"D:\Ajay - Viosa\whatsapp bulk message\Video.mp4"

# Set up the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Read and encode the message text
with open('message.txt', 'r', encoding="utf-8") as file:
    msg = quote(file.read())

# Open WhatsApp Web
driver.get('https://web.whatsapp.com')
time.sleep(login_time)

# Read the phone numbers and send messages
with open('numbers.txt', 'r') as file:
    numbers = [line.strip() for line in file]

for num in numbers:
    try:
        # Create the WhatsApp link
        link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
        driver.get(link)
        time.sleep(new_msg_time)

        # # Send the message
        # actions = ActionChains(driver)
        # actions.send_keys(Keys.ENTER)
        # actions.perform()
        # time.sleep(send_msg_time)

        # Attach and send the video along with the text message
        # input_box = driver.find_element(By.CSS_SELECTOR, '[contenteditable="true"]')
        
        # # Send the text message
        # input_box.send_keys(msg)
        # time.sleep(2)  # Adjust as needed

        # Attach and send the video
        attach_button = driver.find_element(By.CSS_SELECTOR, 'span[data-icon="attach-menu-plus"]')
        attach_button.click()
        time.sleep(2)  # Wait for the attachment menu to open

        # Select "Photos & videos" option
        media_option = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        media_option.send_keys(video_path)
        time.sleep(upload_time)  # Wait for the video to upload

        # Send the video
        send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
        send_button.click()
        time.sleep(send_msg_time)


    except Exception as e:
        print(f"Failed to send message to {num}: {e}")

# Quit the driver
driver.quit()
