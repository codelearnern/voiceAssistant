import requests
import speech_recognition as sr
import pyttsx3

API_KEY = "putapikeyhere"

engine = pyttsx3.Engine()
r = sr.Recognizer()

with sr.Microphone() as mic:
	print("What is the name of city?")
	engine.say("What is the name of city?")
	engine.runAndWait()
	city_name = r.recognize_google(r.listen(mic))
	print(city_name)
	print("What is the country code?")
	engine.say("What is the country code?")
	engine.runAndWait()
	country_code = r.recognize_google(r.listen(mic))
	print(country_code)
	print("What units, metric or imperial?")
	engine.say("What units, metric or imperial?")
	engine.runAndWait()
	units = r.recognize_google(r.listen(mic))
	print(units)

res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={API_KEY}&units={units}")
jsonRes = res.json()

print(jsonRes["main"]["temp"])
engine.say(jsonRes["main"]["temp"])
engine.runAndWait()
print(jsonRes["weather"][0]["main"])
engine.say(jsonRes["weather"][0]["main"])
engine.runAndWait()
