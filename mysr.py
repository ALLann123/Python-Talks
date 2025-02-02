import platform
import speech_recognition as sr
import subprocess

if platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll

    # Define error handler
    error_handler = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

    # Don't do anything if there is an error message
    def py_error_handler(filename, line, function, err, fmt):
        pass

    # Pass to C
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)

    # Check if JACK server is running, if not start it
    try:
        subprocess.run(['jack_control', 'start'], check=True)
    except subprocess.CalledProcessError:
        print("Failed to start JACK server")
        exit(1)

# Now define the voice_to_text() function for all platforms
def voice_to_text():
    voice_input = ""
    speech = sr.Recognizer()  # Create a Recognizer instance

    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source, timeout=10, phrase_time_limit=10)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass

    return voice_input
