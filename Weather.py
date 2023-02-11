import requests

api_key = "67da29cb91129f1a68c1c06c1be92daa"
city = input("\nInput the city name: \n\n")
#str(input("\nEnter the city name:\n\n"))
url = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=" + api_key + "&units=imperial"

request = requests.get(url)
json = request.json()

#print("\n")
description = json.get("weather")[0].get("description")
print("\nToday's forcast is", description, "\n")
#print("\n")

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is" , temp_min, "\n")

temp_max = json.get("main").get("temp_max")
print("The maximum temperature is" , temp_max, "\n")

