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

class Segment(object):
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
        'id': 'SegmentId',
        'fly_from': 'SegmentFlyFrom',
        'fly_to': 'SegmentFlyTo',
        'city_from': 'SegmentCityFrom',
        'city_code_from': 'SegmentCityCodeFrom',
        'city_to': 'SegmentCityTo',
        'city_code_to': 'SegmentCityCodeTo',
        'map_idfrom': 'SegmentMapIdfrom',
        'map_idto': 'SegmentMapIdto',
        'lat_from': 'SegmentLatFrom',
        'lng_from': 'SegmentLngFrom',
        'lat_to': 'SegmentLatTo',
        'lng_to': 'SegmentLngTo',
        'station_from': 'StationFrom',
        'station_to': 'StationTo',
        'd_time': 'SegmentDTime',
        'd_time_utc': 'SegmentDTimeUTC',
        'a_time': 'SegmentATime',
        'a_time_utc': 'SegmentATimeUTC',
        'vehicle_type': 'PropertiesVehicleType',
        'airline': 'Airline',
        'flight_no': 'FlightNo',
        'operating_carrier': 'OperatingCarrier',
        'operating_flight_no': 'OperatingFlightNo',
        'equipment': 'Equipment',
        'fare_basis': 'FareBasis',
        'fare_category': 'FareCategory',
        'fare_family': 'FareFamily',
        'fare_classes': 'FareClasses',
        '_return': 'SegmentReturn',
        'bags_recheck_required': 'BagsRecheckRequired',
        'guarantee': 'Guarantee',
        'vi_connection': 'ViConnection',
        'following_airport_change': 'FollowingAirportChange',
        'following_technical_stop': 'FollowingTechnicalStop',
        'price': 'SegmentPrice'
    }

    attribute_map = {
        'id': 'id',
        'fly_from': 'flyFrom',
        'fly_to': 'flyTo',
        'city_from': 'cityFrom',
        'city_code_from': 'cityCodeFrom',
        'city_to': 'cityTo',
        'city_code_to': 'cityCodeTo',
        'map_idfrom': 'mapIdfrom',
        'map_idto': 'mapIdto',
        'lat_from': 'latFrom',
        'lng_from': 'lngFrom',
        'lat_to': 'latTo',
        'lng_to': 'lngTo',
        'station_from': 'stationFrom',
        'station_to': 'stationTo',
        'd_time': 'dTime',
        'd_time_utc': 'dTimeUTC',
        'a_time': 'aTime',
        'a_time_utc': 'aTimeUTC',
        'vehicle_type': 'vehicle_type',
        'airline': 'airline',
        'flight_no': 'flight_no',
        'operating_carrier': 'operating_carrier',
        'operating_flight_no': 'operating_flight_no',
        'equipment': 'equipment',
        'fare_basis': 'fare_basis',
        'fare_category': 'fare_category',
        'fare_family': 'fare_family',
        'fare_classes': 'fare_classes',
        '_return': 'return',
        'bags_recheck_required': 'bags_recheck_required',
        'guarantee': 'guarantee',
        'vi_connection': 'vi_connection',
        'following_airport_change': 'following_airport_change',
        'following_technical_stop': 'following_technical_stop',
        'price': 'price'
    }

    def __init__(self, id=None, fly_from=None, fly_to=None, city_from=None, city_code_from=None, city_to=None, city_code_to=None, map_idfrom=None, map_idto=None, lat_from=None, lng_from=None, lat_to=None, lng_to=None, station_from=None, station_to=None, d_time=None, d_time_utc=None, a_time=None, a_time_utc=None, vehicle_type=None, airline=None, flight_no=None, operating_carrier=None, operating_flight_no=None, equipment=None, fare_basis=None, fare_category=None, fare_family=None, fare_classes=None, _return=None, bags_recheck_required=None, guarantee=None, vi_connection=None, following_airport_change=None, following_technical_stop=None, price=None):  # noqa: E501
        """Segment - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._fly_from = None
        self._fly_to = None
        self._city_from = None
        self._city_code_from = None
        self._city_to = None
        self._city_code_to = None
        self._map_idfrom = None
        self._map_idto = None
        self._lat_from = None
        self._lng_from = None
        self._lat_to = None
        self._lng_to = None
        self._station_from = None
        self._station_to = None
        self._d_time = None
        self._d_time_utc = None
        self._a_time = None
        self._a_time_utc = None
        self._vehicle_type = None
        self._airline = None
        self._flight_no = None
        self._operating_carrier = None
        self._operating_flight_no = None
        self._equipment = None
        self._fare_basis = None
        self._fare_category = None
        self._fare_family = None
        self._fare_classes = None
        self.__return = None
        self._bags_recheck_required = None
        self._guarantee = None
        self._vi_connection = None
        self._following_airport_change = None
        self._following_technical_stop = None
        self._price = None
        self.discriminator = None
        if id is not None:
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
        if map_idfrom is not None:
            self.map_idfrom = map_idfrom
        if map_idto is not None:
            self.map_idto = map_idto
        if lat_from is not None:
            self.lat_from = lat_from
        if lng_from is not None:
            self.lng_from = lng_from
        if lat_to is not None:
            self.lat_to = lat_to
        if lng_to is not None:
            self.lng_to = lng_to
        if station_from is not None:
            self.station_from = station_from
        if station_to is not None:
            self.station_to = station_to
        if d_time is not None:
            self.d_time = d_time
        if d_time_utc is not None:
            self.d_time_utc = d_time_utc
        if a_time is not None:
            self.a_time = a_time
        if a_time_utc is not None:
            self.a_time_utc = a_time_utc
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if airline is not None:
            self.airline = airline
        if flight_no is not None:
            self.flight_no = flight_no
        if operating_carrier is not None:
            self.operating_carrier = operating_carrier
        if operating_flight_no is not None:
            self.operating_flight_no = operating_flight_no
        if equipment is not None:
            self.equipment = equipment
        if fare_basis is not None:
            self.fare_basis = fare_basis
        if fare_category is not None:
            self.fare_category = fare_category
        if fare_family is not None:
            self.fare_family = fare_family
        if fare_classes is not None:
            self.fare_classes = fare_classes
        if _return is not None:
            self._return = _return
        if bags_recheck_required is not None:
            self.bags_recheck_required = bags_recheck_required
        if guarantee is not None:
            self.guarantee = guarantee
        if vi_connection is not None:
            self.vi_connection = vi_connection
        if following_airport_change is not None:
            self.following_airport_change = following_airport_change
        if following_technical_stop is not None:
            self.following_technical_stop = following_technical_stop
        if price is not None:
            self.price = price

    @property
    def id(self):
        """Gets the id of this Segment.  # noqa: E501


        :return: The id of this Segment.  # noqa: E501
        :rtype: SegmentId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Segment.


        :param id: The id of this Segment.  # noqa: E501
        :type: SegmentId
        """

        self._id = id

    @property
    def fly_from(self):
        """Gets the fly_from of this Segment.  # noqa: E501


        :return: The fly_from of this Segment.  # noqa: E501
        :rtype: SegmentFlyFrom
        """
        return self._fly_from

    @fly_from.setter
    def fly_from(self, fly_from):
        """Sets the fly_from of this Segment.


        :param fly_from: The fly_from of this Segment.  # noqa: E501
        :type: SegmentFlyFrom
        """

        self._fly_from = fly_from

    @property
    def fly_to(self):
        """Gets the fly_to of this Segment.  # noqa: E501


        :return: The fly_to of this Segment.  # noqa: E501
        :rtype: SegmentFlyTo
        """
        return self._fly_to

    @fly_to.setter
    def fly_to(self, fly_to):
        """Sets the fly_to of this Segment.


        :param fly_to: The fly_to of this Segment.  # noqa: E501
        :type: SegmentFlyTo
        """

        self._fly_to = fly_to

    @property
    def city_from(self):
        """Gets the city_from of this Segment.  # noqa: E501


        :return: The city_from of this Segment.  # noqa: E501
        :rtype: SegmentCityFrom
        """
        return self._city_from

    @city_from.setter
    def city_from(self, city_from):
        """Sets the city_from of this Segment.


        :param city_from: The city_from of this Segment.  # noqa: E501
        :type: SegmentCityFrom
        """

        self._city_from = city_from

    @property
    def city_code_from(self):
        """Gets the city_code_from of this Segment.  # noqa: E501


        :return: The city_code_from of this Segment.  # noqa: E501
        :rtype: SegmentCityCodeFrom
        """
        return self._city_code_from

    @city_code_from.setter
    def city_code_from(self, city_code_from):
        """Sets the city_code_from of this Segment.


        :param city_code_from: The city_code_from of this Segment.  # noqa: E501
        :type: SegmentCityCodeFrom
        """

        self._city_code_from = city_code_from

    @property
    def city_to(self):
        """Gets the city_to of this Segment.  # noqa: E501


        :return: The city_to of this Segment.  # noqa: E501
        :rtype: SegmentCityTo
        """
        return self._city_to

    @city_to.setter
    def city_to(self, city_to):
        """Sets the city_to of this Segment.


        :param city_to: The city_to of this Segment.  # noqa: E501
        :type: SegmentCityTo
        """

        self._city_to = city_to

    @property
    def city_code_to(self):
        """Gets the city_code_to of this Segment.  # noqa: E501


        :return: The city_code_to of this Segment.  # noqa: E501
        :rtype: SegmentCityCodeTo
        """
        return self._city_code_to

    @city_code_to.setter
    def city_code_to(self, city_code_to):
        """Sets the city_code_to of this Segment.


        :param city_code_to: The city_code_to of this Segment.  # noqa: E501
        :type: SegmentCityCodeTo
        """

        self._city_code_to = city_code_to

    @property
    def map_idfrom(self):
        """Gets the map_idfrom of this Segment.  # noqa: E501


        :return: The map_idfrom of this Segment.  # noqa: E501
        :rtype: SegmentMapIdfrom
        """
        return self._map_idfrom

    @map_idfrom.setter
    def map_idfrom(self, map_idfrom):
        """Sets the map_idfrom of this Segment.


        :param map_idfrom: The map_idfrom of this Segment.  # noqa: E501
        :type: SegmentMapIdfrom
        """

        self._map_idfrom = map_idfrom

    @property
    def map_idto(self):
        """Gets the map_idto of this Segment.  # noqa: E501


        :return: The map_idto of this Segment.  # noqa: E501
        :rtype: SegmentMapIdto
        """
        return self._map_idto

    @map_idto.setter
    def map_idto(self, map_idto):
        """Sets the map_idto of this Segment.


        :param map_idto: The map_idto of this Segment.  # noqa: E501
        :type: SegmentMapIdto
        """

        self._map_idto = map_idto

    @property
    def lat_from(self):
        """Gets the lat_from of this Segment.  # noqa: E501


        :return: The lat_from of this Segment.  # noqa: E501
        :rtype: SegmentLatFrom
        """
        return self._lat_from

    @lat_from.setter
    def lat_from(self, lat_from):
        """Sets the lat_from of this Segment.


        :param lat_from: The lat_from of this Segment.  # noqa: E501
        :type: SegmentLatFrom
        """

        self._lat_from = lat_from

    @property
    def lng_from(self):
        """Gets the lng_from of this Segment.  # noqa: E501


        :return: The lng_from of this Segment.  # noqa: E501
        :rtype: SegmentLngFrom
        """
        return self._lng_from

    @lng_from.setter
    def lng_from(self, lng_from):
        """Sets the lng_from of this Segment.


        :param lng_from: The lng_from of this Segment.  # noqa: E501
        :type: SegmentLngFrom
        """

        self._lng_from = lng_from

    @property
    def lat_to(self):
        """Gets the lat_to of this Segment.  # noqa: E501


        :return: The lat_to of this Segment.  # noqa: E501
        :rtype: SegmentLatTo
        """
        return self._lat_to

    @lat_to.setter
    def lat_to(self, lat_to):
        """Sets the lat_to of this Segment.


        :param lat_to: The lat_to of this Segment.  # noqa: E501
        :type: SegmentLatTo
        """

        self._lat_to = lat_to

    @property
    def lng_to(self):
        """Gets the lng_to of this Segment.  # noqa: E501


        :return: The lng_to of this Segment.  # noqa: E501
        :rtype: SegmentLngTo
        """
        return self._lng_to

    @lng_to.setter
    def lng_to(self, lng_to):
        """Sets the lng_to of this Segment.


        :param lng_to: The lng_to of this Segment.  # noqa: E501
        :type: SegmentLngTo
        """

        self._lng_to = lng_to

    @property
    def station_from(self):
        """Gets the station_from of this Segment.  # noqa: E501


        :return: The station_from of this Segment.  # noqa: E501
        :rtype: StationFrom
        """
        return self._station_from

    @station_from.setter
    def station_from(self, station_from):
        """Sets the station_from of this Segment.


        :param station_from: The station_from of this Segment.  # noqa: E501
        :type: StationFrom
        """

        self._station_from = station_from

    @property
    def station_to(self):
        """Gets the station_to of this Segment.  # noqa: E501


        :return: The station_to of this Segment.  # noqa: E501
        :rtype: StationTo
        """
        return self._station_to

    @station_to.setter
    def station_to(self, station_to):
        """Sets the station_to of this Segment.


        :param station_to: The station_to of this Segment.  # noqa: E501
        :type: StationTo
        """

        self._station_to = station_to

    @property
    def d_time(self):
        """Gets the d_time of this Segment.  # noqa: E501


        :return: The d_time of this Segment.  # noqa: E501
        :rtype: SegmentDTime
        """
        return self._d_time

    @d_time.setter
    def d_time(self, d_time):
        """Sets the d_time of this Segment.


        :param d_time: The d_time of this Segment.  # noqa: E501
        :type: SegmentDTime
        """

        self._d_time = d_time

    @property
    def d_time_utc(self):
        """Gets the d_time_utc of this Segment.  # noqa: E501


        :return: The d_time_utc of this Segment.  # noqa: E501
        :rtype: SegmentDTimeUTC
        """
        return self._d_time_utc

    @d_time_utc.setter
    def d_time_utc(self, d_time_utc):
        """Sets the d_time_utc of this Segment.


        :param d_time_utc: The d_time_utc of this Segment.  # noqa: E501
        :type: SegmentDTimeUTC
        """

        self._d_time_utc = d_time_utc

    @property
    def a_time(self):
        """Gets the a_time of this Segment.  # noqa: E501


        :return: The a_time of this Segment.  # noqa: E501
        :rtype: SegmentATime
        """
        return self._a_time

    @a_time.setter
    def a_time(self, a_time):
        """Sets the a_time of this Segment.


        :param a_time: The a_time of this Segment.  # noqa: E501
        :type: SegmentATime
        """

        self._a_time = a_time

    @property
    def a_time_utc(self):
        """Gets the a_time_utc of this Segment.  # noqa: E501


        :return: The a_time_utc of this Segment.  # noqa: E501
        :rtype: SegmentATimeUTC
        """
        return self._a_time_utc

    @a_time_utc.setter
    def a_time_utc(self, a_time_utc):
        """Sets the a_time_utc of this Segment.


        :param a_time_utc: The a_time_utc of this Segment.  # noqa: E501
        :type: SegmentATimeUTC
        """

        self._a_time_utc = a_time_utc

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this Segment.  # noqa: E501


        :return: The vehicle_type of this Segment.  # noqa: E501
        :rtype: PropertiesVehicleType
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this Segment.


        :param vehicle_type: The vehicle_type of this Segment.  # noqa: E501
        :type: PropertiesVehicleType
        """

        self._vehicle_type = vehicle_type

    @property
    def airline(self):
        """Gets the airline of this Segment.  # noqa: E501


        :return: The airline of this Segment.  # noqa: E501
        :rtype: Airline
        """
        return self._airline

    @airline.setter
    def airline(self, airline):
        """Sets the airline of this Segment.


        :param airline: The airline of this Segment.  # noqa: E501
        :type: Airline
        """

        self._airline = airline

    @property
    def flight_no(self):
        """Gets the flight_no of this Segment.  # noqa: E501


        :return: The flight_no of this Segment.  # noqa: E501
        :rtype: FlightNo
        """
        return self._flight_no

    @flight_no.setter
    def flight_no(self, flight_no):
        """Sets the flight_no of this Segment.


        :param flight_no: The flight_no of this Segment.  # noqa: E501
        :type: FlightNo
        """

        self._flight_no = flight_no

    @property
    def operating_carrier(self):
        """Gets the operating_carrier of this Segment.  # noqa: E501


        :return: The operating_carrier of this Segment.  # noqa: E501
        :rtype: OperatingCarrier
        """
        return self._operating_carrier

    @operating_carrier.setter
    def operating_carrier(self, operating_carrier):
        """Sets the operating_carrier of this Segment.


        :param operating_carrier: The operating_carrier of this Segment.  # noqa: E501
        :type: OperatingCarrier
        """

        self._operating_carrier = operating_carrier

    @property
    def operating_flight_no(self):
        """Gets the operating_flight_no of this Segment.  # noqa: E501


        :return: The operating_flight_no of this Segment.  # noqa: E501
        :rtype: OperatingFlightNo
        """
        return self._operating_flight_no

    @operating_flight_no.setter
    def operating_flight_no(self, operating_flight_no):
        """Sets the operating_flight_no of this Segment.


        :param operating_flight_no: The operating_flight_no of this Segment.  # noqa: E501
        :type: OperatingFlightNo
        """

        self._operating_flight_no = operating_flight_no

    @property
    def equipment(self):
        """Gets the equipment of this Segment.  # noqa: E501


        :return: The equipment of this Segment.  # noqa: E501
        :rtype: Equipment
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this Segment.


        :param equipment: The equipment of this Segment.  # noqa: E501
        :type: Equipment
        """

        self._equipment = equipment

    @property
    def fare_basis(self):
        """Gets the fare_basis of this Segment.  # noqa: E501


        :return: The fare_basis of this Segment.  # noqa: E501
        :rtype: FareBasis
        """
        return self._fare_basis

    @fare_basis.setter
    def fare_basis(self, fare_basis):
        """Sets the fare_basis of this Segment.


        :param fare_basis: The fare_basis of this Segment.  # noqa: E501
        :type: FareBasis
        """

        self._fare_basis = fare_basis

    @property
    def fare_category(self):
        """Gets the fare_category of this Segment.  # noqa: E501


        :return: The fare_category of this Segment.  # noqa: E501
        :rtype: FareCategory
        """
        return self._fare_category

    @fare_category.setter
    def fare_category(self, fare_category):
        """Sets the fare_category of this Segment.


        :param fare_category: The fare_category of this Segment.  # noqa: E501
        :type: FareCategory
        """

        self._fare_category = fare_category

    @property
    def fare_family(self):
        """Gets the fare_family of this Segment.  # noqa: E501


        :return: The fare_family of this Segment.  # noqa: E501
        :rtype: FareFamily
        """
        return self._fare_family

    @fare_family.setter
    def fare_family(self, fare_family):
        """Sets the fare_family of this Segment.


        :param fare_family: The fare_family of this Segment.  # noqa: E501
        :type: FareFamily
        """

        self._fare_family = fare_family

    @property
    def fare_classes(self):
        """Gets the fare_classes of this Segment.  # noqa: E501


        :return: The fare_classes of this Segment.  # noqa: E501
        :rtype: FareClasses
        """
        return self._fare_classes

    @fare_classes.setter
    def fare_classes(self, fare_classes):
        """Sets the fare_classes of this Segment.


        :param fare_classes: The fare_classes of this Segment.  # noqa: E501
        :type: FareClasses
        """

        self._fare_classes = fare_classes

    @property
    def _return(self):
        """Gets the _return of this Segment.  # noqa: E501


        :return: The _return of this Segment.  # noqa: E501
        :rtype: SegmentReturn
        """
        return self.__return

    @_return.setter
    def _return(self, _return):
        """Sets the _return of this Segment.


        :param _return: The _return of this Segment.  # noqa: E501
        :type: SegmentReturn
        """

        self.__return = _return

    @property
    def bags_recheck_required(self):
        """Gets the bags_recheck_required of this Segment.  # noqa: E501


        :return: The bags_recheck_required of this Segment.  # noqa: E501
        :rtype: BagsRecheckRequired
        """
        return self._bags_recheck_required

    @bags_recheck_required.setter
    def bags_recheck_required(self, bags_recheck_required):
        """Sets the bags_recheck_required of this Segment.


        :param bags_recheck_required: The bags_recheck_required of this Segment.  # noqa: E501
        :type: BagsRecheckRequired
        """

        self._bags_recheck_required = bags_recheck_required

    @property
    def guarantee(self):
        """Gets the guarantee of this Segment.  # noqa: E501


        :return: The guarantee of this Segment.  # noqa: E501
        :rtype: Guarantee
        """
        return self._guarantee

    @guarantee.setter
    def guarantee(self, guarantee):
        """Sets the guarantee of this Segment.


        :param guarantee: The guarantee of this Segment.  # noqa: E501
        :type: Guarantee
        """

        self._guarantee = guarantee

    @property
    def vi_connection(self):
        """Gets the vi_connection of this Segment.  # noqa: E501


        :return: The vi_connection of this Segment.  # noqa: E501
        :rtype: ViConnection
        """
        return self._vi_connection

    @vi_connection.setter
    def vi_connection(self, vi_connection):
        """Sets the vi_connection of this Segment.


        :param vi_connection: The vi_connection of this Segment.  # noqa: E501
        :type: ViConnection
        """

        self._vi_connection = vi_connection

    @property
    def following_airport_change(self):
        """Gets the following_airport_change of this Segment.  # noqa: E501


        :return: The following_airport_change of this Segment.  # noqa: E501
        :rtype: FollowingAirportChange
        """
        return self._following_airport_change

    @following_airport_change.setter
    def following_airport_change(self, following_airport_change):
        """Sets the following_airport_change of this Segment.


        :param following_airport_change: The following_airport_change of this Segment.  # noqa: E501
        :type: FollowingAirportChange
        """

        self._following_airport_change = following_airport_change

    @property
    def following_technical_stop(self):
        """Gets the following_technical_stop of this Segment.  # noqa: E501


        :return: The following_technical_stop of this Segment.  # noqa: E501
        :rtype: FollowingTechnicalStop
        """
        return self._following_technical_stop

    @following_technical_stop.setter
    def following_technical_stop(self, following_technical_stop):
        """Sets the following_technical_stop of this Segment.


        :param following_technical_stop: The following_technical_stop of this Segment.  # noqa: E501
        :type: FollowingTechnicalStop
        """

        self._following_technical_stop = following_technical_stop

    @property
    def price(self):
        """Gets the price of this Segment.  # noqa: E501


        :return: The price of this Segment.  # noqa: E501
        :rtype: SegmentPrice
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Segment.


        :param price: The price of this Segment.  # noqa: E501
        :type: SegmentPrice
        """

        self._price = price

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
        if issubclass(Segment, dict):
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
        if not isinstance(other, Segment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other