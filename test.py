import speech_recognition as sr

def transcribe_audio():
    # Create a Recognizer object
    recognizer = sr.Recognizer()

    print("Listening to audio...")

    try:
        # Use the Microphone class to capture the system's audio output
        with sr.Microphone() as source:
            # Adjust the recognizer sensitivity to ambient noise
            recognizer.adjust_for_ambient_noise(source)
            print("Microphone active, please play the audio.")

            # while True:
            try:
                # Capture audio
                audio = recognizer.listen(source)
                print("Processing audio...")
                # Recognize speech using Google's recognizer
                text = recognizer.recognize_google(audio, language='en-IN')
                print("Transcription:", text)
            except sr.WaitTimeoutError:
                print("Listening timeout, no speech detected.")
                
            except sr.UnknownValueError:
                print("Could not understand the audio, please try again.")
                
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                

    except KeyboardInterrupt:
        print("Script interrupted by the user.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("Script ended.")
    # print(text)
    return text

if __name__ == "__main__":
    transcribe_audio()
