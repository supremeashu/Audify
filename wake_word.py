# wake_word.py
import pvporcupine
import pyaudio
import struct


def listen_for_wake_word():
    porcupine = pvporcupine.create(
        access_key="YOUR_PICOVOICE_ACCESS_KEY",  # Replace with your Picovoice access key
        keywords=["ok google", "hey google", "alexa", "hey siri"]
    )  # Use the built-in "blueberry" wake word

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )

    print("Say wake word to activate...")

    try:
        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                return True
    finally:
        porcupine.delete()


# resourrce followed = https://picovoice.ai/docs/quick-start/porcupine-python/#picovoice-account--accesskey