import requests


def get_info(text=None, year=None, month=None, day=None):
	url = "https://historical-events-by-api-ninjas.p.rapidapi.com/v1/historicalevents"

	querystring = {}
	if text:
		querystring['text'] = str(text)

	if year:
		querystring['year'] = str(year)

	if month:
		querystring['month'] = str(month)

	if day:
		querystring['day'] = str(day)
	headers = {
		"X-RapidAPI-Key": "ba0efc9885mshdd54fda1cd38290p18ac69jsn59bbf9e55335",
		"X-RapidAPI-Host": "historical-events-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	if response.status_code != requests.codes.ok:
		print("Error:", response.status_code, response.text)
		return

	data = {}
	for idx, stories in enumerate(response):
		data[idx] = stories
	return data