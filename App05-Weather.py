from urllib.request import Request, urlopen, URLError

request = Request('http://api.openweathermap.org/data/2.5/forecast?q=London,us')

try:
	response = urlopen(request)
	weather = response.read()
	print(weather)
except URLError:
    print('No kittez. Got an error code: ')