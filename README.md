# britishairways-python [![Build Status](https://travis-ci.org/adamgilman/britishairways-python.svg?branch=master)](https://travis-ci.org/adamgilman/britishairways-python)
Python API to British Airways Flight Search

```bash
adamgilman$ export CLIENTKEY=[KeyFrom - developer.ba.com]
```

```python
>>> from britishair import BA
>>> from datetime import datetime
>>> ba = BA()
>>> outboundDateTime = datetime(month=4, day=3, year=2015)
>>> inboundDateTime = datetime(month=4, day=10, year=2015)
>>> locationOutbound = "LHR"
>>> locationInbound = "LAX"
>>> fareClass = "Economy"
>>> fares = ba.search(outboundDateTime, locationOutbound, inboundDateTime, locationInbound, fareClass)
>>> fares[0][u'AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['@Amount']
u'965.66'
>>> fares[0][u'AirItineraryPricingInfo']['ItinTotalFare']['TotalFare']['@CurrencyCode']
u'GBP'

```
