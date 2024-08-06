import requests
import json
location=input("Enter the name of the city\n")
url=f"https://api.tomorrow.io/v4/weather/forecast?location={location}&apikey=I71CV9M51zFmv8xDGXyqOdwjX40QtbfA"
r=requests.get(url)
print(r.text)
# wdic=json.load(r.text)
# print(wdic["time"]["humidity"]["temperature"]["windDirection"]["windSpeed"])