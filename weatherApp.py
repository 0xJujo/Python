import requests
import json
from datetime import date
import pyttsx3

date=date.today()

city= input("Enter your city name: ")

url= f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{date}?key=JMWD8TZ3A49TWG76K59ARNTW4"

response= requests.get(url)
# print(response.text)
# print(type(response.text))
if response.status_code == 200:
    # Load JSON data
    weather_data = json.loads(response.text)
    
    # Extract temperature from the currentConditions
    current_temp = weather_data['currentConditions']['temp']
    description = weather_data['description']
    # Build your description including the temperature
    desc = f"Current temperature in {city} is {current_temp}°F and {description}"
    engine = pyttsx3.init()
    engine.say(desc)
    engine.runAndWait()

else:
    print(f"Error fetching data: Status code {response.status_code}")