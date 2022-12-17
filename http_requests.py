import requests

url = "https://api.polygon.io/v3/reference/tickers/AAPL"
apiKey = "y723MRY4JdI2ZlsnqbsFExGJBrXSMqLb"

response = requests.get(url, params={'apiKey': apiKey})

print(response.text)