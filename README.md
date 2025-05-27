# 🎧 Voice-Controlled Spotify Player
## 📌 Project Description
This project is a Python-based voice-controlled interface for playing songs on Spotify using Selenium and speech recognition. Users can activate playback by saying a predefined wake word (e.g., "Hey Spotify"), followed by their song request (e.g., "play Believer by Imagine Dragons"). The browser automation mimics user interaction with Spotify’s web interface to search and play the desired song.

### Built with:

Python

Selenium (Browser Automation with Brave)

SpeechRecognition (Voice input handling)

Pyttsx3 (Text-to-speech for feedback)

## 🚀 Need for This Project
Manually interacting with web music players can interrupt workflow or leisure activities. This project aims to:

* Provide hands-free music control.


* Offer an accessible interface for users with mobility or visual impairments.

* Explore real-world integration of browser automation and voice interfaces.

* Main reason 🤫 - Brave runs spotify add free, spotify contains every songs, and in windows we cannot interact with spotify, so i fealt the need of this project 

## 🛠️ How It Works
* Wake Word Detection — The system listens continuously for a wake word. (able to hear - "ok google", "hey google", "alexa", "hey siri")

* Command Recognition — Once triggered, it captures the next spoken phrase as the song request.

* Voice Feedback — The system repeats the recognized command for confirmation.

* Spotify Interaction — Using Selenium, the browser is opened (or reused), the song is searched and played.

## 📦 Installation
### Requirements
Ensure you have the following installed:

* Python 3.8+

* Brave Browser

* porcupine access key(available when you signin at https://picovoice.ai/platform/porcupine/)

---
## Some must do steps

* In wake_word.py access key is necessary and you need access key by creating a account at picovoice.ai link provided above

* in main.py add your username to options.add_agrument

* when brave lauches ensure search bar available in that brave instance, if not cross the pop up of browser is automated and reload the browser
---

## Clone and Set Up

```
git clone https://github.com/yourusername/voice-spotify-player.git
cd voice-spotify-player
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
```
Update the path to Brave binary and user profile in the Python file.

## 📁 File Structure
``` text
voice-spotify-player/
│
├── main.py                    # Main script to run the assistant
├── requirements.txt
├── speech_handler.py
├── spotify_control.py
├── test_speech.py
├── wake_word.py
├── LICENCE
└── README.md                  
```

## Future Plans
Currently it is only for playing diffent songs, but i would like to add the following features:
* play and pause
* volume up and down

## 📃 License
This project is licensed under the MIT License.
