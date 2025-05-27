from wake_word import listen_for_wake_word
from speech_handler import get_command
from spotify_control import play_song
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Listening for wake word...")
    # print(f"Launching Brave and playing: {song_name}")

    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    options.add_argument(r"user-data-dir=C:\Users\{your username }\BraveSeleniumProfile") # Change {your username} to your actual username
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://open.spotify.com/")
    wait = WebDriverWait(driver, 15)

    print("Waiting 10 seconds for Spotify to load... Log in manually if not logged in.")
    time.sleep(10)
    while True:
        if listen_for_wake_word():
            print("Wake word detected. Listening for command...")
            speak("yes sir")
            command = get_command()
            if command:
                print(f"Command: {command}")
                speak(f"Playing {command} on Spotify")
                play_song(driver ,command)









# for wake word testing

# from wake_word import listen_for_wake_word

# if __name__ == "__main__":
#     if listen_for_wake_word():
#         print("Now you can speak your command!")
