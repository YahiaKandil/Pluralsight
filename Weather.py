import requests

def weather_details():
    api_key = "67da29cb91129f1a68c1c06c1be92daa"
    city = input("\nInput the city name: \n\n")
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=" + api_key + "&units=imperial"
    request = requests.get(url)
    json = request.json()
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description":description, 
    "temp_min":temp_min,
     "temp_max":temp_max}


weather_det = weather_details()
print("\nToday's forcast is", weather_det.get("description"), "\n")
print("The minimum temperature is" , weather_det.get("temp_min"), "\n")
print("The maximum temperature is" , weather_det.get("temp_max"), "\n")

