import requests

base_url = input("Enter the base url: ")
api_key = input("Enter Your api key: ")
city_name = input("Enter your city name: ")

complete_url = f"{base_url}{city_name}&appid={api_key}&mode=json&units=metric"

response = requests.get(complete_url)

def handle_200(data):
    print("Current Temperature:",data["main"]["temp"])
    print("Maximum Temperature:",data["main"]["temp_max"])
    print("Minimum Temperature:",data["main"]["temp_min"])
    print("Current Temperature Feels like:",data["main"]["feels_like"])
    print("Pressure:",data["main"]["pressure"])
    print("Humidity:",data["main"]["humidity"])

def handle_401():
    print("Invalid API key.")

def handle_404():
    print("City not found.")

def handle_400():
    print("Bad request.")

def handle_429():
    print("Too Many Requests. Please wait and try again later.")

status_handles = {
    200: handle_200,
    401: handle_401,
    404: handle_404,
    400: handle_400,
    429: handle_429,
}

handler = status_handles.get(response.status_code,lambda : print("Failed to retrieve weather information. Status code:", response.status_code))
handler(response.json())
