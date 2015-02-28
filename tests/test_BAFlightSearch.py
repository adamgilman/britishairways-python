import unittest
from datetime import datetime
import vcr

from britishair import BA

my_vcr = vcr.VCR(
	serializer = 'yaml',
	cassette_library_dir = 'tests/fixtures/cassettes',
	record_mode = 'once',
)

class TestBASearch(unittest.TestCase):
    def setUp(self):
        self.ba = BA()

    #@unittest.skip("temp disabled")
    def test_SimpleEconomySearch(self):
        outboundDateTime = datetime(month=4, day=3, year=2015)
        inboundDateTime = datetime(month=4, day=10, year=2015)
        locationOutbound = "LHR"
        locationInbound = "LAX"
        fareClass = "Economy"
        with my_vcr.use_cassette('test_SimpleEconomySearch.json'):
            fares = self.ba.search(outboundDateTime, locationOutbound, inboundDateTime, locationInbound, fareClass)
            amount = fares[0][u'AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['@Amount']
            self.assertEqual( amount, u'965.66')

    def test_SimpleBusinessSearch(self):
        outboundDateTime = datetime(month=4, day=3, year=2015)
        inboundDateTime = datetime(month=4, day=10, year=2015)
        locationOutbound = "LHR"
        locationInbound = "LAX"
        fareClass = "Business"
        with my_vcr.use_cassette('test_SimpleBusinessSearch.json'):
            fares = self.ba.search(outboundDateTime, locationOutbound, inboundDateTime, locationInbound, fareClass)
            amount = fares[0][u'AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['@Amount']
            self.assertEqual( amount, u'2568.66')

    def test_BuildParamsDateTime(self):
        dtinput = datetime(year=2015, month=4, day=3)
        output = "2015-04-03T00:00:00Z"
        self.assertEqual( self.ba._buildDateTime(dtinput), output)

    def test_ParamsPacker(self):
        paramIn = [
            ("departureDateTimeOutbound", "2015-04-03T00:00:00Z"),
            ("locationCodeOriginOutbound", "LHR"),
            ("locationCodeDestinationOutbound", "lax"),
            ("departureDateTimeInbound", "2015-04-10T00:00:00Z"),
            ("locationCodeOriginInbound", "lax"),
            ("locationCodeDestinationInbound", "LHR"),
            ("cabin", "Economy"),
            ("ADT", "1"),
            ("CHD", "0"),
            ("INF", "0"),
            ("format", ".json")]

        paramOut = "departureDateTimeOutbound=2015-04-03T00:00:00Z;locationCodeOriginOutbound=LHR;locationCodeDestinationOutbound=lax;departureDateTimeInbound=2015-04-10T00:00:00Z;locationCodeOriginInbound=lax;locationCodeDestinationInbound=LHR;cabin=Economy;ADT=1;CHD=0;INF=0;format=.json"

        self.assertEqual( self.ba._buildParams(paramIn), paramOut)