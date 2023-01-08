import requests

def get_exchange_rate():
  url = "https://api.exchangeratesapi.io/latest?base=USD"
  response = requests.get(url)
  return response.json()

exchange_rate = get_exchange_rate()
print(exchange_rate)