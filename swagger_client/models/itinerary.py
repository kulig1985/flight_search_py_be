# coding: utf-8

"""
    Search API

    For existing users using the api.skypicker.com endpoint:\\ You need to have an affiliate (partner) ID. This ID is used across Kiwi.com services to distinguish between partners. In this API, for all endpoints, you need to specify it in query parameter `partner`.  For new users of the Kiwi.com APIs:\\ Please register to our Tequila portal at [tequila.kiwi.com](https://tequila.kiwi.com/) to get your unique API key and use the new API there.  This API provides several options how to search for itineraries. At the moment there are different type of itineraries and different endpoints how to search for them. For oneway and roundtrip itineraries /flights endpoint need to be used. If you want to search for itineraries with multiple stops and you know exactly in which order you want them, then use our multicity searching which is available on /flights/multicity endpoint. Finally if you want to search for itineraries where you know the start and end of you journey and you know all the stops, but you don't mind in which order then you can use our Nomad searching which is available on /traveling_salesman endpoint.  Response from all endpoints will contain a list of itineraries, where each itinerary contain a link leading directly to Kiwi.com booking page where the user can book the specified flight. Each itinerary will also contain booking token which is needed in [Booking API](https://docs.kiwi.com/#header-booking-api).  Please note that all parameters marked as \"Deprecated\" are still accepted, although later they will be decommissioned. Some of them will be decommissioned completely and some of them can be replaced with other more powerful parameters. More information can be found in the description of the actual parameter.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Itinerary(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'ItineraryId',
        'fly_from': 'ItineraryFlyFrom',
        'fly_to': 'ItineraryFlyTo',
        'city_from': 'ItineraryCityFrom',
        'city_code_from': 'ItineraryCityCodeFrom',
        'city_to': 'ItineraryCityTo',
        'city_code_to': 'ItineraryCityCodeTo',
        'country_from': 'ItineraryCountryFrom',
        'country_to': 'ItineraryCountryTo',
        'map_idfrom': 'ItineraryMapIdfrom',
        'map_idto': 'ItineraryMapIdto',
        'd_time': 'ItineraryDTime',
        'd_time_utc': 'ItineraryDTimeUTC',
        'a_time': 'ItineraryATime',
        'a_time_utc': 'ItineraryATimeUTC',
        'bags_price': 'BagsPrice',
        'baglimit': 'Baglimit',
        'price': 'Price',
        'conversion': 'Conversion',
        'fly_duration': 'FlyDuration',
        'return_duration': 'ReturnDuration',
        'duration': 'Duration',
        'nights_in_dest': 'NightsInDest',
        'distance': 'Distance',
        'virtual_interlining': 'VirtualInterlining',
        'throw_away_ticketing': 'ThrowAwayTicketing',
        'hidden_city_ticketing': 'HiddenCityTicketing',
        'pnr_count': 'PnrCount',
        'has_airport_change': 'HasAirportChange',
        'technical_stops': 'TechnicalStops',
        'booking_token': 'BookingToken',
        'deep_link': 'DeepLink',
        'route': 'list[Segment]',
        'type_flights': 'TypeFlights',
        'p1': 'P1'
    }

    attribute_map = {
        'id': 'id',
        'fly_from': 'flyFrom',
        'fly_to': 'flyTo',
        'city_from': 'cityFrom',
        'city_code_from': 'cityCodeFrom',
        'city_to': 'cityTo',
        'city_code_to': 'cityCodeTo',
        'country_from': 'countryFrom',
        'country_to': 'countryTo',
        'map_idfrom': 'mapIdfrom',
        'map_idto': 'mapIdto',
        'd_time': 'dTime',
        'd_time_utc': 'dTimeUTC',
        'a_time': 'aTime',
        'a_time_utc': 'aTimeUTC',
        'bags_price': 'bags_price',
        'baglimit': 'baglimit',
        'price': 'price',
        'conversion': 'conversion',
        'fly_duration': 'fly_duration',
        'return_duration': 'return_duration',
        'duration': 'duration',
        'nights_in_dest': 'nightsInDest',
        'distance': 'distance',
        'virtual_interlining': 'virtual_interlining',
        'throw_away_ticketing': 'throw_away_ticketing',
        'hidden_city_ticketing': 'hidden_city_ticketing',
        'pnr_count': 'pnr_count',
        'has_airport_change': 'has_airport_change',
        'technical_stops': 'technical_stops',
        'booking_token': 'booking_token',
        'deep_link': 'deep_link',
        'route': 'route',
        'type_flights': 'type_flights',
        'p1': 'p1'
    }

    def __init__(self, id=None, fly_from=None, fly_to=None, city_from=None, city_code_from=None, city_to=None, city_code_to=None, country_from=None, country_to=None, map_idfrom=None, map_idto=None, d_time=None, d_time_utc=None, a_time=None, a_time_utc=None, bags_price=None, baglimit=None, price=None, conversion=None, fly_duration=None, return_duration=None, duration=None, nights_in_dest=None, distance=None, virtual_interlining=None, throw_away_ticketing=None, hidden_city_ticketing=None, pnr_count=None, has_airport_change=None, technical_stops=None, booking_token=None, deep_link=None, route=None, type_flights=None, p1=None):  # noqa: E501
        """Itinerary - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fly_from = None
        self._fly_to = None
        self._city_from = None
        self._city_code_from = None
        self._city_to = None
        self._city_code_to = None
        self._country_from = None
        self._country_to = None
        self._map_idfrom = None
        self._map_idto = None
        self._d_time = None
        self._d_time_utc = None
        self._a_time = None
        self._a_time_utc = None
        self._bags_price = None
        self._baglimit = None
        self._price = None
        self._conversion = None
        self._fly_duration = None
        self._return_duration = None
        self._duration = None
        self._nights_in_dest = None
        self._distance = None
        self._virtual_interlining = None
        self._throw_away_ticketing = None
        self._hidden_city_ticketing = None
        self._pnr_count = None
        self._has_airport_change = None
        self._technical_stops = None
        self._booking_token = None
        self._deep_link = None
        self._route = None
        self._type_flights = None
        self._p1 = None
        self.discriminator = None
        self.id = id
        if fly_from is not None:
            self.fly_from = fly_from
        if fly_to is not None:
            self.fly_to = fly_to
        if city_from is not None:
            self.city_from = city_from
        if city_code_from is not None:
            self.city_code_from = city_code_from
        if city_to is not None:
            self.city_to = city_to
        if city_code_to is not None:
            self.city_code_to = city_code_to
        if country_from is not None:
            self.country_from = country_from
        if country_to is not None:
            self.country_to = country_to
        if map_idfrom is not None:
            self.map_idfrom = map_idfrom
        if map_idto is not None:
            self.map_idto = map_idto
        if d_time is not None:
            self.d_time = d_time
        if d_time_utc is not None:
            self.d_time_utc = d_time_utc
        if a_time is not None:
            self.a_time = a_time
        if a_time_utc is not None:
            self.a_time_utc = a_time_utc
        if bags_price is not None:
            self.bags_price = bags_price
        if baglimit is not None:
            self.baglimit = baglimit
        if price is not None:
            self.price = price
        if conversion is not None:
            self.conversion = conversion
        if fly_duration is not None:
            self.fly_duration = fly_duration
        if return_duration is not None:
            self.return_duration = return_duration
        if duration is not None:
            self.duration = duration
        if nights_in_dest is not None:
            self.nights_in_dest = nights_in_dest
        if distance is not None:
            self.distance = distance
        if virtual_interlining is not None:
            self.virtual_interlining = virtual_interlining
        if throw_away_ticketing is not None:
            self.throw_away_ticketing = throw_away_ticketing
        if hidden_city_ticketing is not None:
            self.hidden_city_ticketing = hidden_city_ticketing
        if pnr_count is not None:
            self.pnr_count = pnr_count
        if has_airport_change is not None:
            self.has_airport_change = has_airport_change
        if technical_stops is not None:
            self.technical_stops = technical_stops
        if booking_token is not None:
            self.booking_token = booking_token
        if deep_link is not None:
            self.deep_link = deep_link
        if route is not None:
            self.route = route
        if type_flights is not None:
            self.type_flights = type_flights
        if p1 is not None:
            self.p1 = p1

    @property
    def id(self):
        """Gets the id of this Itinerary.  # noqa: E501


        :return: The id of this Itinerary.  # noqa: E501
        :rtype: ItineraryId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Itinerary.


        :param id: The id of this Itinerary.  # noqa: E501
        :type: ItineraryId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def fly_from(self):
        """Gets the fly_from of this Itinerary.  # noqa: E501


        :return: The fly_from of this Itinerary.  # noqa: E501
        :rtype: ItineraryFlyFrom
        """
        return self._fly_from

    @fly_from.setter
    def fly_from(self, fly_from):
        """Sets the fly_from of this Itinerary.


        :param fly_from: The fly_from of this Itinerary.  # noqa: E501
        :type: ItineraryFlyFrom
        """

        self._fly_from = fly_from

    @property
    def fly_to(self):
        """Gets the fly_to of this Itinerary.  # noqa: E501


        :return: The fly_to of this Itinerary.  # noqa: E501
        :rtype: ItineraryFlyTo
        """
        return self._fly_to

    @fly_to.setter
    def fly_to(self, fly_to):
        """Sets the fly_to of this Itinerary.


        :param fly_to: The fly_to of this Itinerary.  # noqa: E501
        :type: ItineraryFlyTo
        """

        self._fly_to = fly_to

    @property
    def city_from(self):
        """Gets the city_from of this Itinerary.  # noqa: E501


        :return: The city_from of this Itinerary.  # noqa: E501
        :rtype: ItineraryCityFrom
        """
        return self._city_from

    @city_from.setter
    def city_from(self, city_from):
        """Sets the city_from of this Itinerary.


        :param city_from: The city_from of this Itinerary.  # noqa: E501
        :type: ItineraryCityFrom
        """

        self._city_from = city_from

    @property
    def city_code_from(self):
        """Gets the city_code_from of this Itinerary.  # noqa: E501


        :return: The city_code_from of this Itinerary.  # noqa: E501
        :rtype: ItineraryCityCodeFrom
        """
        return self._city_code_from

    @city_code_from.setter
    def city_code_from(self, city_code_from):
        """Sets the city_code_from of this Itinerary.


        :param city_code_from: The city_code_from of this Itinerary.  # noqa: E501
        :type: ItineraryCityCodeFrom
        """

        self._city_code_from = city_code_from

    @property
    def city_to(self):
        """Gets the city_to of this Itinerary.  # noqa: E501


        :return: The city_to of this Itinerary.  # noqa: E501
        :rtype: ItineraryCityTo
        """
        return self._city_to

    @city_to.setter
    def city_to(self, city_to):
        """Sets the city_to of this Itinerary.


        :param city_to: The city_to of this Itinerary.  # noqa: E501
        :type: ItineraryCityTo
        """

        self._city_to = city_to

    @property
    def city_code_to(self):
        """Gets the city_code_to of this Itinerary.  # noqa: E501


        :return: The city_code_to of this Itinerary.  # noqa: E501
        :rtype: ItineraryCityCodeTo
        """
        return self._city_code_to

    @city_code_to.setter
    def city_code_to(self, city_code_to):
        """Sets the city_code_to of this Itinerary.


        :param city_code_to: The city_code_to of this Itinerary.  # noqa: E501
        :type: ItineraryCityCodeTo
        """

        self._city_code_to = city_code_to

    @property
    def country_from(self):
        """Gets the country_from of this Itinerary.  # noqa: E501


        :return: The country_from of this Itinerary.  # noqa: E501
        :rtype: ItineraryCountryFrom
        """
        return self._country_from

    @country_from.setter
    def country_from(self, country_from):
        """Sets the country_from of this Itinerary.


        :param country_from: The country_from of this Itinerary.  # noqa: E501
        :type: ItineraryCountryFrom
        """

        self._country_from = country_from

    @property
    def country_to(self):
        """Gets the country_to of this Itinerary.  # noqa: E501


        :return: The country_to of this Itinerary.  # noqa: E501
        :rtype: ItineraryCountryTo
        """
        return self._country_to

    @country_to.setter
    def country_to(self, country_to):
        """Sets the country_to of this Itinerary.


        :param country_to: The country_to of this Itinerary.  # noqa: E501
        :type: ItineraryCountryTo
        """

        self._country_to = country_to

    @property
    def map_idfrom(self):
        """Gets the map_idfrom of this Itinerary.  # noqa: E501


        :return: The map_idfrom of this Itinerary.  # noqa: E501
        :rtype: ItineraryMapIdfrom
        """
        return self._map_idfrom

    @map_idfrom.setter
    def map_idfrom(self, map_idfrom):
        """Sets the map_idfrom of this Itinerary.


        :param map_idfrom: The map_idfrom of this Itinerary.  # noqa: E501
        :type: ItineraryMapIdfrom
        """

        self._map_idfrom = map_idfrom

    @property
    def map_idto(self):
        """Gets the map_idto of this Itinerary.  # noqa: E501


        :return: The map_idto of this Itinerary.  # noqa: E501
        :rtype: ItineraryMapIdto
        """
        return self._map_idto

    @map_idto.setter
    def map_idto(self, map_idto):
        """Sets the map_idto of this Itinerary.


        :param map_idto: The map_idto of this Itinerary.  # noqa: E501
        :type: ItineraryMapIdto
        """

        self._map_idto = map_idto

    @property
    def d_time(self):
        """Gets the d_time of this Itinerary.  # noqa: E501


        :return: The d_time of this Itinerary.  # noqa: E501
        :rtype: ItineraryDTime
        """
        return self._d_time

    @d_time.setter
    def d_time(self, d_time):
        """Sets the d_time of this Itinerary.


        :param d_time: The d_time of this Itinerary.  # noqa: E501
        :type: ItineraryDTime
        """

        self._d_time = d_time

    @property
    def d_time_utc(self):
        """Gets the d_time_utc of this Itinerary.  # noqa: E501


        :return: The d_time_utc of this Itinerary.  # noqa: E501
        :rtype: ItineraryDTimeUTC
        """
        return self._d_time_utc

    @d_time_utc.setter
    def d_time_utc(self, d_time_utc):
        """Sets the d_time_utc of this Itinerary.


        :param d_time_utc: The d_time_utc of this Itinerary.  # noqa: E501
        :type: ItineraryDTimeUTC
        """

        self._d_time_utc = d_time_utc

    @property
    def a_time(self):
        """Gets the a_time of this Itinerary.  # noqa: E501


        :return: The a_time of this Itinerary.  # noqa: E501
        :rtype: ItineraryATime
        """
        return self._a_time

    @a_time.setter
    def a_time(self, a_time):
        """Sets the a_time of this Itinerary.


        :param a_time: The a_time of this Itinerary.  # noqa: E501
        :type: ItineraryATime
        """

        self._a_time = a_time

    @property
    def a_time_utc(self):
        """Gets the a_time_utc of this Itinerary.  # noqa: E501


        :return: The a_time_utc of this Itinerary.  # noqa: E501
        :rtype: ItineraryATimeUTC
        """
        return self._a_time_utc

    @a_time_utc.setter
    def a_time_utc(self, a_time_utc):
        """Sets the a_time_utc of this Itinerary.


        :param a_time_utc: The a_time_utc of this Itinerary.  # noqa: E501
        :type: ItineraryATimeUTC
        """

        self._a_time_utc = a_time_utc

    @property
    def bags_price(self):
        """Gets the bags_price of this Itinerary.  # noqa: E501


        :return: The bags_price of this Itinerary.  # noqa: E501
        :rtype: BagsPrice
        """
        return self._bags_price

    @bags_price.setter
    def bags_price(self, bags_price):
        """Sets the bags_price of this Itinerary.


        :param bags_price: The bags_price of this Itinerary.  # noqa: E501
        :type: BagsPrice
        """

        self._bags_price = bags_price

    @property
    def baglimit(self):
        """Gets the baglimit of this Itinerary.  # noqa: E501


        :return: The baglimit of this Itinerary.  # noqa: E501
        :rtype: Baglimit
        """
        return self._baglimit

    @baglimit.setter
    def baglimit(self, baglimit):
        """Sets the baglimit of this Itinerary.


        :param baglimit: The baglimit of this Itinerary.  # noqa: E501
        :type: Baglimit
        """

        self._baglimit = baglimit

    @property
    def price(self):
        """Gets the price of this Itinerary.  # noqa: E501


        :return: The price of this Itinerary.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Itinerary.


        :param price: The price of this Itinerary.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def conversion(self):
        """Gets the conversion of this Itinerary.  # noqa: E501


        :return: The conversion of this Itinerary.  # noqa: E501
        :rtype: Conversion
        """
        return self._conversion

    @conversion.setter
    def conversion(self, conversion):
        """Sets the conversion of this Itinerary.


        :param conversion: The conversion of this Itinerary.  # noqa: E501
        :type: Conversion
        """

        self._conversion = conversion

    @property
    def fly_duration(self):
        """Gets the fly_duration of this Itinerary.  # noqa: E501


        :return: The fly_duration of this Itinerary.  # noqa: E501
        :rtype: FlyDuration
        """
        return self._fly_duration

    @fly_duration.setter
    def fly_duration(self, fly_duration):
        """Sets the fly_duration of this Itinerary.


        :param fly_duration: The fly_duration of this Itinerary.  # noqa: E501
        :type: FlyDuration
        """

        self._fly_duration = fly_duration

    @property
    def return_duration(self):
        """Gets the return_duration of this Itinerary.  # noqa: E501


        :return: The return_duration of this Itinerary.  # noqa: E501
        :rtype: ReturnDuration
        """
        return self._return_duration

    @return_duration.setter
    def return_duration(self, return_duration):
        """Sets the return_duration of this Itinerary.


        :param return_duration: The return_duration of this Itinerary.  # noqa: E501
        :type: ReturnDuration
        """

        self._return_duration = return_duration

    @property
    def duration(self):
        """Gets the duration of this Itinerary.  # noqa: E501


        :return: The duration of this Itinerary.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Itinerary.


        :param duration: The duration of this Itinerary.  # noqa: E501
        :type: Duration
        """

        self._duration = duration

    @property
    def nights_in_dest(self):
        """Gets the nights_in_dest of this Itinerary.  # noqa: E501


        :return: The nights_in_dest of this Itinerary.  # noqa: E501
        :rtype: NightsInDest
        """
        return self._nights_in_dest

    @nights_in_dest.setter
    def nights_in_dest(self, nights_in_dest):
        """Sets the nights_in_dest of this Itinerary.


        :param nights_in_dest: The nights_in_dest of this Itinerary.  # noqa: E501
        :type: NightsInDest
        """

        self._nights_in_dest = nights_in_dest

    @property
    def distance(self):
        """Gets the distance of this Itinerary.  # noqa: E501


        :return: The distance of this Itinerary.  # noqa: E501
        :rtype: Distance
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Itinerary.


        :param distance: The distance of this Itinerary.  # noqa: E501
        :type: Distance
        """

        self._distance = distance

    @property
    def virtual_interlining(self):
        """Gets the virtual_interlining of this Itinerary.  # noqa: E501


        :return: The virtual_interlining of this Itinerary.  # noqa: E501
        :rtype: VirtualInterlining
        """
        return self._virtual_interlining

    @virtual_interlining.setter
    def virtual_interlining(self, virtual_interlining):
        """Sets the virtual_interlining of this Itinerary.


        :param virtual_interlining: The virtual_interlining of this Itinerary.  # noqa: E501
        :type: VirtualInterlining
        """

        self._virtual_interlining = virtual_interlining

    @property
    def throw_away_ticketing(self):
        """Gets the throw_away_ticketing of this Itinerary.  # noqa: E501


        :return: The throw_away_ticketing of this Itinerary.  # noqa: E501
        :rtype: ThrowAwayTicketing
        """
        return self._throw_away_ticketing

    @throw_away_ticketing.setter
    def throw_away_ticketing(self, throw_away_ticketing):
        """Sets the throw_away_ticketing of this Itinerary.


        :param throw_away_ticketing: The throw_away_ticketing of this Itinerary.  # noqa: E501
        :type: ThrowAwayTicketing
        """

        self._throw_away_ticketing = throw_away_ticketing

    @property
    def hidden_city_ticketing(self):
        """Gets the hidden_city_ticketing of this Itinerary.  # noqa: E501


        :return: The hidden_city_ticketing of this Itinerary.  # noqa: E501
        :rtype: HiddenCityTicketing
        """
        return self._hidden_city_ticketing

    @hidden_city_ticketing.setter
    def hidden_city_ticketing(self, hidden_city_ticketing):
        """Sets the hidden_city_ticketing of this Itinerary.


        :param hidden_city_ticketing: The hidden_city_ticketing of this Itinerary.  # noqa: E501
        :type: HiddenCityTicketing
        """

        self._hidden_city_ticketing = hidden_city_ticketing

    @property
    def pnr_count(self):
        """Gets the pnr_count of this Itinerary.  # noqa: E501


        :return: The pnr_count of this Itinerary.  # noqa: E501
        :rtype: PnrCount
        """
        return self._pnr_count

    @pnr_count.setter
    def pnr_count(self, pnr_count):
        """Sets the pnr_count of this Itinerary.


        :param pnr_count: The pnr_count of this Itinerary.  # noqa: E501
        :type: PnrCount
        """

        self._pnr_count = pnr_count

    @property
    def has_airport_change(self):
        """Gets the has_airport_change of this Itinerary.  # noqa: E501


        :return: The has_airport_change of this Itinerary.  # noqa: E501
        :rtype: HasAirportChange
        """
        return self._has_airport_change

    @has_airport_change.setter
    def has_airport_change(self, has_airport_change):
        """Sets the has_airport_change of this Itinerary.


        :param has_airport_change: The has_airport_change of this Itinerary.  # noqa: E501
        :type: HasAirportChange
        """

        self._has_airport_change = has_airport_change

    @property
    def technical_stops(self):
        """Gets the technical_stops of this Itinerary.  # noqa: E501


        :return: The technical_stops of this Itinerary.  # noqa: E501
        :rtype: TechnicalStops
        """
        return self._technical_stops

    @technical_stops.setter
    def technical_stops(self, technical_stops):
        """Sets the technical_stops of this Itinerary.


        :param technical_stops: The technical_stops of this Itinerary.  # noqa: E501
        :type: TechnicalStops
        """

        self._technical_stops = technical_stops

    @property
    def booking_token(self):
        """Gets the booking_token of this Itinerary.  # noqa: E501


        :return: The booking_token of this Itinerary.  # noqa: E501
        :rtype: BookingToken
        """
        return self._booking_token

    @booking_token.setter
    def booking_token(self, booking_token):
        """Sets the booking_token of this Itinerary.


        :param booking_token: The booking_token of this Itinerary.  # noqa: E501
        :type: BookingToken
        """

        self._booking_token = booking_token

    @property
    def deep_link(self):
        """Gets the deep_link of this Itinerary.  # noqa: E501


        :return: The deep_link of this Itinerary.  # noqa: E501
        :rtype: DeepLink
        """
        return self._deep_link

    @deep_link.setter
    def deep_link(self, deep_link):
        """Sets the deep_link of this Itinerary.


        :param deep_link: The deep_link of this Itinerary.  # noqa: E501
        :type: DeepLink
        """

        self._deep_link = deep_link

    @property
    def route(self):
        """Gets the route of this Itinerary.  # noqa: E501

        List of segments.  # noqa: E501

        :return: The route of this Itinerary.  # noqa: E501
        :rtype: list[Segment]
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this Itinerary.

        List of segments.  # noqa: E501

        :param route: The route of this Itinerary.  # noqa: E501
        :type: list[Segment]
        """

        self._route = route

    @property
    def type_flights(self):
        """Gets the type_flights of this Itinerary.  # noqa: E501


        :return: The type_flights of this Itinerary.  # noqa: E501
        :rtype: TypeFlights
        """
        return self._type_flights

    @type_flights.setter
    def type_flights(self, type_flights):
        """Sets the type_flights of this Itinerary.


        :param type_flights: The type_flights of this Itinerary.  # noqa: E501
        :type: TypeFlights
        """

        self._type_flights = type_flights

    @property
    def p1(self):
        """Gets the p1 of this Itinerary.  # noqa: E501


        :return: The p1 of this Itinerary.  # noqa: E501
        :rtype: P1
        """
        return self._p1

    @p1.setter
    def p1(self, p1):
        """Sets the p1 of this Itinerary.


        :param p1: The p1 of this Itinerary.  # noqa: E501
        :type: P1
        """

        self._p1 = p1

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Itinerary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Itinerary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
