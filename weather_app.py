import requests

def get_data_by_location(location):
    
    api_key = "<INSERT YOUR API KEY>"

    # Get the current time, temperature and weather condition for a given location
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(location, api_key)
    r = requests.get(api_url)
    data = r.json()
    
    # Get the current time of the location
    time_url = "http://worldtimeapi.org/api/timezone/Europe/{}".format(location)
    r = requests.get(time_url)
    time_data = r.json()
    
    # Get the temperature
    temp = data['main']['temp']
    
    # Get the weather condition
    weather = data['weather'][0]['description']
    
    # Get the current time
    time = time_data['datetime']
    
    # Print the data
    print("Location: {}".format(location))
    print("Time: {}".format(time))
    print("Temperature: {} C".format(temp))
    print("Weather: {}".format(weather))

# Test the function
get_data_by_location("London")