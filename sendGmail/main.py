import speech_recognition as sr
import pyttsx3
from email.mime.text import MIMEText
import base64
from Google import Create_Service
import jsonpickle

tts_engine = pyttsx3.init()
sRecognizer = sr.Recognizer()

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

def create_msg(sender, to, subject, text):
    message = MIMEText(text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()} # encrypt and get in format to send

def send_msg(service, uid, msg):
    print(msg)
    # try:
    message = (service.users().messages().send(userId=uid, body=msg)
           .execute())

    #    tts_engine.say(f"Message ID is {message['id']}")
    #    tts_engine.runAndWait()

    return message

    # except Exception as e:
        # tts_engine.say(f"An error occurred, {e}")

msg_to = input("Who are you sending it to?")
with sr.Microphone() as src:
    print("What is the subject")
    tts_engine.say("What is the subject?")
    tts_engine.runAndWait()
    msg_subject = sRecognizer.recognize_google(sRecognizer.listen(src))
    print("What is the message?")
    tts_engine.say("What is the message?")
    tts_engine.runAndWait()
    msg_text = sRecognizer.recognize_google(sRecognizer.listen(src))

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

msg = create_msg("youremailhere@gmail.com", msg_to, msg_subject, msg_text)
send_msg(service, "youremailhere@gmail.com", msg)
