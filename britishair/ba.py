import os, json
import requests

from datetime import datetime

class BA(object):
	def __init__(self):
		self.client_key = os.getenv('CLIENTKEY')
		if self.client_key is None:
			raise Exception("No CLIENTKEY env set")

	def _buildDateTime(self, dtinput):
		return dtinput.strftime("%Y-%m-%dT00:00:00Z")

	def _buildParams(self, params):
		output = ""
		for i, kv in enumerate(params):
			if type(kv) is tuple:
				key, value = kv
				output = output + key + "=" + value
				if i != len(params)-1:
					output = output + ";"
		return output

	def search(self, outboundDateTime, locationOutbound, inboundDateTime, locationInbound, fareClass):

		headers = {'Client-Key' : self.client_key}
		params = [
		("departureDateTimeOutbound", self._buildDateTime(outboundDateTime)),
		("locationCodeOriginOutbound", locationOutbound),
		("locationCodeDestinationOutbound", locationInbound),
		("departureDateTimeInbound", self._buildDateTime(inboundDateTime)),
		("locationCodeOriginInbound", locationInbound),
		("locationCodeDestinationInbound", locationOutbound),
		("cabin", fareClass),
		("ADT", "1"),
		("CHD", "0"),
		("INF", "0"),
		("format", ".json")]

		url = "https://api.ba.com/rest-v1/v1/flightOfferMktAffiliates;" + self._buildParams(params)

		response = requests.get(url, headers=headers)
		data = json.loads(response.text)
		itineraries = data[u'OTA_AirLowFareSearchRS'][u'PricedItineraries'][u'PricedItinerary']

		return itineraries
	        


		