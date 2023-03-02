import speech_recognition as sr
def mic_input():
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
    # try:
        r = sr.Recognizer()
        r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source, duration=1)
        with sr.Microphone() as source:
            print("Listening....")
            r.energy_threshold = 400
            audio = r.listen(source)
        try:
            print("Recognizing...")
            command = r.recognize_google(audio, language='en-in').lower()
            print(f'You said: {command}')
        except:
            print('Please try again')
            command = self.mic_input()
        return command
        # except Exception as e:
        #     print(e)
        #     return False

mic_input()

