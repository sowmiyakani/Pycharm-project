import requests
import json
apikey ="a54094261ab65dba2b1545a090e45586"
base_url ="https://api.openweathermap.org/data/2.5/weather?q="
city_name = input("Enter your city name:")
complete_url =base_url + city_name +"&appid=" + apikey
response = requests.get(complete_url)
data =response.json()
print("Current Temperature :",data["main"]["temp"])
print("Maximum Temperature :",data["main"]["temp_max"])
print("Minimum Temperature :",data["main"]["temp_min"])
print("Current Temperature Feels like :",data["main"]["feels_like"])
print("pressure :",data["main"]["pressure"])
print("Humidity :",data["main"]["humidity"])
