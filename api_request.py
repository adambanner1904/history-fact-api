import requests
from request_handling import to_dict
import json


def get_info(text=None, year=None, month=None, day=None):

	url = "https://historical-events-by-api-ninjas.p.rapidapi.com/v1/historicalevents"

	querystring = {}
	if text != '' and text:
		querystring['text'] = str(text)

	if year != '' and year:
		querystring['year'] = str(year)

	if month != '' and month:
		querystring['month'] = str(month)

	if day != '' and day:
		querystring['day'] = str(day)
	headers = {
		"X-RapidAPI-Key": "ba0efc9885mshdd54fda1cd38290p18ac69jsn59bbf9e55335",
		"X-RapidAPI-Host": "historical-events-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)
	if response.status_code != requests.codes.ok:
		print("Error:", response.status_code, response.text)
		return
	else:
		response = json.loads(response.text)
		response = to_dict(response)

	return response


info = get_info(**{'text': 'roman empire', 'year': '', 'day': ''})
print(len(info))
