import requests
base_url = input("Enter the base url: ")
apikey = input("Enter Your api key: ")
city_name = input("Enter your city name: ")
complete_url = base_url + city_name + "&appid=" + apikey +"&mode=json&units=metric"

response = requests.get(complete_url)

if response.status_code == 200:
    data = response.json()
    if "main" in data:
        print("Current Temperature:", data["main"]["temp"])
        print("Maximum Temperature:", data["main"]["temp_max"])
        print("Minimum Temperature:", data["main"]["temp_min"])
        print("Current Temperature Feels like:", data["main"]["feels_like"])
        print("Pressure:", data["main"]["pressure"])
        print("Humidity:", data["main"]["humidity"])
    else:
        print("No weather information found for the city.")
elif response.status_code == 401:
    print("Invalid API key.")
elif response.status_code == 404:
    print("City not found.")
elif response.status_code == 400:
    print("Bad request.")
elif response.status_code == 429:
    print("Too Many Requests. Please wait and try again later.")
else:
    print("Failed to retrieve weather information. Status code:", response.status_code)

