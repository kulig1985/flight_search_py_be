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

class BodyRequests(object):
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
        'partner_market': 'PartnerMarket',
        'fly_from': 'FlyFrom',
        'fly_to': 'FlyTo',
        'fly_days': 'FlyDays',
        'fly_days_type': 'FlyDaysType',
        'depart_after': 'DepartAfter',
        'depart_before': 'DepartBefore',
        'arrive_after': 'ArriveAfter',
        'arrive_before': 'ArriveBefore',
        'nights_in_dst_from': 'NightsInDstFrom',
        'nights_in_dst_to': 'NightsInDstTo',
        'dtime_from': 'DtimeFrom',
        'dtime_to': 'DtimeTo',
        'atime_from': 'AtimeFrom',
        'atime_to': 'AtimeTo',
        'max_fly_duration': 'MaxFlyDuration',
        'vehicle_type': 'VehicleType',
        'select_airlines': 'SelectAirlines',
        'select_airlines_exclude': 'SelectAirlinesExclude',
        'select_stop_airport': 'SelectStopAirport',
        'select_stop_airport_exclude': 'SelectStopAirportExclude',
        'stopover_from': 'StopoverFrom',
        'stopover_to': 'StopoverTo',
        'max_stopovers': 'MaxStopovers',
        'max_sector_stopovers': 'MaxSectorStopovers',
        'conn_on_diff_airport': 'ConnOnDiffAirport',
        'selected_cabins': 'SelectedCabins',
        'mix_with_cabins': 'MixWithCabins',
        'adults': 'Adults',
        'children': 'Children',
        'infants': 'Infants',
        'adult_hold_bag': 'AdultHoldBag',
        'adult_hand_bag': 'AdultHandBag',
        'child_hold_bag': 'ChildHoldBag',
        'child_hand_bag': 'ChildHandBag',
        'price_from': 'PriceFrom',
        'price_to': 'PriceFrom',
        'sort': 'Sort',
        'asc': 'Asc',
        'limit': 'Limit',
        'date_from': 'DateFrom',
        'date_to': 'DateTo',
        'only_working_days': 'OnlyWorkingDays',
        'only_weekends': 'OnlyWeekends',
        'direct_flights': 'DirectFlights',
        'v': 'V'
    }

    attribute_map = {
        'partner_market': 'partner_market',
        'fly_from': 'fly_from',
        'fly_to': 'fly_to',
        'fly_days': 'fly_days',
        'fly_days_type': 'fly_days_type',
        'depart_after': 'depart_after',
        'depart_before': 'depart_before',
        'arrive_after': 'arrive_after',
        'arrive_before': 'arrive_before',
        'nights_in_dst_from': 'nights_in_dst_from',
        'nights_in_dst_to': 'nights_in_dst_to',
        'dtime_from': 'dtime_from',
        'dtime_to': 'dtime_to',
        'atime_from': 'atime_from',
        'atime_to': 'atime_to',
        'max_fly_duration': 'max_fly_duration',
        'vehicle_type': 'vehicle_type',
        'select_airlines': 'select_airlines',
        'select_airlines_exclude': 'select_airlines_exclude',
        'select_stop_airport': 'select_stop_airport',
        'select_stop_airport_exclude': 'select_stop_airport_exclude',
        'stopover_from': 'stopover_from',
        'stopover_to': 'stopover_to',
        'max_stopovers': 'max_stopovers',
        'max_sector_stopovers': 'max_sector_stopovers',
        'conn_on_diff_airport': 'conn_on_diff_airport',
        'selected_cabins': 'selected_cabins',
        'mix_with_cabins': 'mix_with_cabins',
        'adults': 'adults',
        'children': 'children',
        'infants': 'infants',
        'adult_hold_bag': 'adult_hold_bag',
        'adult_hand_bag': 'adult_hand_bag',
        'child_hold_bag': 'child_hold_bag',
        'child_hand_bag': 'child_hand_bag',
        'price_from': 'price_from',
        'price_to': 'price_to',
        'sort': 'sort',
        'asc': 'asc',
        'limit': 'limit',
        'date_from': 'date_from',
        'date_to': 'date_to',
        'only_working_days': 'only_working_days',
        'only_weekends': 'only_weekends',
        'direct_flights': 'direct_flights',
        'v': 'v'
    }

    def __init__(self, partner_market=None, fly_from=None, fly_to=None, fly_days=None, fly_days_type=None, depart_after=None, depart_before=None, arrive_after=None, arrive_before=None, nights_in_dst_from=None, nights_in_dst_to=None, dtime_from=None, dtime_to=None, atime_from=None, atime_to=None, max_fly_duration=None, vehicle_type=None, select_airlines=None, select_airlines_exclude=None, select_stop_airport=None, select_stop_airport_exclude=None, stopover_from=None, stopover_to=None, max_stopovers=None, max_sector_stopovers=None, conn_on_diff_airport=None, selected_cabins=None, mix_with_cabins=None, adults=None, children=None, infants=None, adult_hold_bag=None, adult_hand_bag=None, child_hold_bag=None, child_hand_bag=None, price_from=None, price_to=None, sort=None, asc=None, limit=None, date_from=None, date_to=None, only_working_days=None, only_weekends=None, direct_flights=None, v=None):  # noqa: E501
        """BodyRequests - a model defined in Swagger"""  # noqa: E501
        self._partner_market = None
        self._fly_from = None
        self._fly_to = None
        self._fly_days = None
        self._fly_days_type = None
        self._depart_after = None
        self._depart_before = None
        self._arrive_after = None
        self._arrive_before = None
        self._nights_in_dst_from = None
        self._nights_in_dst_to = None
        self._dtime_from = None
        self._dtime_to = None
        self._atime_from = None
        self._atime_to = None
        self._max_fly_duration = None
        self._vehicle_type = None
        self._select_airlines = None
        self._select_airlines_exclude = None
        self._select_stop_airport = None
        self._select_stop_airport_exclude = None
        self._stopover_from = None
        self._stopover_to = None
        self._max_stopovers = None
        self._max_sector_stopovers = None
        self._conn_on_diff_airport = None
        self._selected_cabins = None
        self._mix_with_cabins = None
        self._adults = None
        self._children = None
        self._infants = None
        self._adult_hold_bag = None
        self._adult_hand_bag = None
        self._child_hold_bag = None
        self._child_hand_bag = None
        self._price_from = None
        self._price_to = None
        self._sort = None
        self._asc = None
        self._limit = None
        self._date_from = None
        self._date_to = None
        self._only_working_days = None
        self._only_weekends = None
        self._direct_flights = None
        self._v = None
        self.discriminator = None
        if partner_market is not None:
            self.partner_market = partner_market
        if fly_from is not None:
            self.fly_from = fly_from
        if fly_to is not None:
            self.fly_to = fly_to
        if fly_days is not None:
            self.fly_days = fly_days
        if fly_days_type is not None:
            self.fly_days_type = fly_days_type
        if depart_after is not None:
            self.depart_after = depart_after
        if depart_before is not None:
            self.depart_before = depart_before
        if arrive_after is not None:
            self.arrive_after = arrive_after
        if arrive_before is not None:
            self.arrive_before = arrive_before
        if nights_in_dst_from is not None:
            self.nights_in_dst_from = nights_in_dst_from
        if nights_in_dst_to is not None:
            self.nights_in_dst_to = nights_in_dst_to
        if dtime_from is not None:
            self.dtime_from = dtime_from
        if dtime_to is not None:
            self.dtime_to = dtime_to
        if atime_from is not None:
            self.atime_from = atime_from
        if atime_to is not None:
            self.atime_to = atime_to
        if max_fly_duration is not None:
            self.max_fly_duration = max_fly_duration
        if vehicle_type is not None:
            self.vehicle_type = vehicle_type
        if select_airlines is not None:
            self.select_airlines = select_airlines
        if select_airlines_exclude is not None:
            self.select_airlines_exclude = select_airlines_exclude
        if select_stop_airport is not None:
            self.select_stop_airport = select_stop_airport
        if select_stop_airport_exclude is not None:
            self.select_stop_airport_exclude = select_stop_airport_exclude
        if stopover_from is not None:
            self.stopover_from = stopover_from
        if stopover_to is not None:
            self.stopover_to = stopover_to
        if max_stopovers is not None:
            self.max_stopovers = max_stopovers
        if max_sector_stopovers is not None:
            self.max_sector_stopovers = max_sector_stopovers
        if conn_on_diff_airport is not None:
            self.conn_on_diff_airport = conn_on_diff_airport
        if selected_cabins is not None:
            self.selected_cabins = selected_cabins
        if mix_with_cabins is not None:
            self.mix_with_cabins = mix_with_cabins
        if adults is not None:
            self.adults = adults
        if children is not None:
            self.children = children
        if infants is not None:
            self.infants = infants
        if adult_hold_bag is not None:
            self.adult_hold_bag = adult_hold_bag
        if adult_hand_bag is not None:
            self.adult_hand_bag = adult_hand_bag
        if child_hold_bag is not None:
            self.child_hold_bag = child_hold_bag
        if child_hand_bag is not None:
            self.child_hand_bag = child_hand_bag
        if price_from is not None:
            self.price_from = price_from
        if price_to is not None:
            self.price_to = price_to
        if sort is not None:
            self.sort = sort
        if asc is not None:
            self.asc = asc
        if limit is not None:
            self.limit = limit
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if only_working_days is not None:
            self.only_working_days = only_working_days
        if only_weekends is not None:
            self.only_weekends = only_weekends
        if direct_flights is not None:
            self.direct_flights = direct_flights
        if v is not None:
            self.v = v

    @property
    def partner_market(self):
        """Gets the partner_market of this BodyRequests.  # noqa: E501


        :return: The partner_market of this BodyRequests.  # noqa: E501
        :rtype: PartnerMarket
        """
        return self._partner_market

    @partner_market.setter
    def partner_market(self, partner_market):
        """Sets the partner_market of this BodyRequests.


        :param partner_market: The partner_market of this BodyRequests.  # noqa: E501
        :type: PartnerMarket
        """

        self._partner_market = partner_market

    @property
    def fly_from(self):
        """Gets the fly_from of this BodyRequests.  # noqa: E501


        :return: The fly_from of this BodyRequests.  # noqa: E501
        :rtype: FlyFrom
        """
        return self._fly_from

    @fly_from.setter
    def fly_from(self, fly_from):
        """Sets the fly_from of this BodyRequests.


        :param fly_from: The fly_from of this BodyRequests.  # noqa: E501
        :type: FlyFrom
        """

        self._fly_from = fly_from

    @property
    def fly_to(self):
        """Gets the fly_to of this BodyRequests.  # noqa: E501


        :return: The fly_to of this BodyRequests.  # noqa: E501
        :rtype: FlyTo
        """
        return self._fly_to

    @fly_to.setter
    def fly_to(self, fly_to):
        """Sets the fly_to of this BodyRequests.


        :param fly_to: The fly_to of this BodyRequests.  # noqa: E501
        :type: FlyTo
        """

        self._fly_to = fly_to

    @property
    def fly_days(self):
        """Gets the fly_days of this BodyRequests.  # noqa: E501


        :return: The fly_days of this BodyRequests.  # noqa: E501
        :rtype: FlyDays
        """
        return self._fly_days

    @fly_days.setter
    def fly_days(self, fly_days):
        """Sets the fly_days of this BodyRequests.


        :param fly_days: The fly_days of this BodyRequests.  # noqa: E501
        :type: FlyDays
        """

        self._fly_days = fly_days

    @property
    def fly_days_type(self):
        """Gets the fly_days_type of this BodyRequests.  # noqa: E501


        :return: The fly_days_type of this BodyRequests.  # noqa: E501
        :rtype: FlyDaysType
        """
        return self._fly_days_type

    @fly_days_type.setter
    def fly_days_type(self, fly_days_type):
        """Sets the fly_days_type of this BodyRequests.


        :param fly_days_type: The fly_days_type of this BodyRequests.  # noqa: E501
        :type: FlyDaysType
        """

        self._fly_days_type = fly_days_type

    @property
    def depart_after(self):
        """Gets the depart_after of this BodyRequests.  # noqa: E501


        :return: The depart_after of this BodyRequests.  # noqa: E501
        :rtype: DepartAfter
        """
        return self._depart_after

    @depart_after.setter
    def depart_after(self, depart_after):
        """Sets the depart_after of this BodyRequests.


        :param depart_after: The depart_after of this BodyRequests.  # noqa: E501
        :type: DepartAfter
        """

        self._depart_after = depart_after

    @property
    def depart_before(self):
        """Gets the depart_before of this BodyRequests.  # noqa: E501


        :return: The depart_before of this BodyRequests.  # noqa: E501
        :rtype: DepartBefore
        """
        return self._depart_before

    @depart_before.setter
    def depart_before(self, depart_before):
        """Sets the depart_before of this BodyRequests.


        :param depart_before: The depart_before of this BodyRequests.  # noqa: E501
        :type: DepartBefore
        """

        self._depart_before = depart_before

    @property
    def arrive_after(self):
        """Gets the arrive_after of this BodyRequests.  # noqa: E501


        :return: The arrive_after of this BodyRequests.  # noqa: E501
        :rtype: ArriveAfter
        """
        return self._arrive_after

    @arrive_after.setter
    def arrive_after(self, arrive_after):
        """Sets the arrive_after of this BodyRequests.


        :param arrive_after: The arrive_after of this BodyRequests.  # noqa: E501
        :type: ArriveAfter
        """

        self._arrive_after = arrive_after

    @property
    def arrive_before(self):
        """Gets the arrive_before of this BodyRequests.  # noqa: E501


        :return: The arrive_before of this BodyRequests.  # noqa: E501
        :rtype: ArriveBefore
        """
        return self._arrive_before

    @arrive_before.setter
    def arrive_before(self, arrive_before):
        """Sets the arrive_before of this BodyRequests.


        :param arrive_before: The arrive_before of this BodyRequests.  # noqa: E501
        :type: ArriveBefore
        """

        self._arrive_before = arrive_before

    @property
    def nights_in_dst_from(self):
        """Gets the nights_in_dst_from of this BodyRequests.  # noqa: E501


        :return: The nights_in_dst_from of this BodyRequests.  # noqa: E501
        :rtype: NightsInDstFrom
        """
        return self._nights_in_dst_from

    @nights_in_dst_from.setter
    def nights_in_dst_from(self, nights_in_dst_from):
        """Sets the nights_in_dst_from of this BodyRequests.


        :param nights_in_dst_from: The nights_in_dst_from of this BodyRequests.  # noqa: E501
        :type: NightsInDstFrom
        """

        self._nights_in_dst_from = nights_in_dst_from

    @property
    def nights_in_dst_to(self):
        """Gets the nights_in_dst_to of this BodyRequests.  # noqa: E501


        :return: The nights_in_dst_to of this BodyRequests.  # noqa: E501
        :rtype: NightsInDstTo
        """
        return self._nights_in_dst_to

    @nights_in_dst_to.setter
    def nights_in_dst_to(self, nights_in_dst_to):
        """Sets the nights_in_dst_to of this BodyRequests.


        :param nights_in_dst_to: The nights_in_dst_to of this BodyRequests.  # noqa: E501
        :type: NightsInDstTo
        """

        self._nights_in_dst_to = nights_in_dst_to

    @property
    def dtime_from(self):
        """Gets the dtime_from of this BodyRequests.  # noqa: E501


        :return: The dtime_from of this BodyRequests.  # noqa: E501
        :rtype: DtimeFrom
        """
        return self._dtime_from

    @dtime_from.setter
    def dtime_from(self, dtime_from):
        """Sets the dtime_from of this BodyRequests.


        :param dtime_from: The dtime_from of this BodyRequests.  # noqa: E501
        :type: DtimeFrom
        """

        self._dtime_from = dtime_from

    @property
    def dtime_to(self):
        """Gets the dtime_to of this BodyRequests.  # noqa: E501


        :return: The dtime_to of this BodyRequests.  # noqa: E501
        :rtype: DtimeTo
        """
        return self._dtime_to

    @dtime_to.setter
    def dtime_to(self, dtime_to):
        """Sets the dtime_to of this BodyRequests.


        :param dtime_to: The dtime_to of this BodyRequests.  # noqa: E501
        :type: DtimeTo
        """

        self._dtime_to = dtime_to

    @property
    def atime_from(self):
        """Gets the atime_from of this BodyRequests.  # noqa: E501


        :return: The atime_from of this BodyRequests.  # noqa: E501
        :rtype: AtimeFrom
        """
        return self._atime_from

    @atime_from.setter
    def atime_from(self, atime_from):
        """Sets the atime_from of this BodyRequests.


        :param atime_from: The atime_from of this BodyRequests.  # noqa: E501
        :type: AtimeFrom
        """

        self._atime_from = atime_from

    @property
    def atime_to(self):
        """Gets the atime_to of this BodyRequests.  # noqa: E501


        :return: The atime_to of this BodyRequests.  # noqa: E501
        :rtype: AtimeTo
        """
        return self._atime_to

    @atime_to.setter
    def atime_to(self, atime_to):
        """Sets the atime_to of this BodyRequests.


        :param atime_to: The atime_to of this BodyRequests.  # noqa: E501
        :type: AtimeTo
        """

        self._atime_to = atime_to

    @property
    def max_fly_duration(self):
        """Gets the max_fly_duration of this BodyRequests.  # noqa: E501


        :return: The max_fly_duration of this BodyRequests.  # noqa: E501
        :rtype: MaxFlyDuration
        """
        return self._max_fly_duration

    @max_fly_duration.setter
    def max_fly_duration(self, max_fly_duration):
        """Sets the max_fly_duration of this BodyRequests.


        :param max_fly_duration: The max_fly_duration of this BodyRequests.  # noqa: E501
        :type: MaxFlyDuration
        """

        self._max_fly_duration = max_fly_duration

    @property
    def vehicle_type(self):
        """Gets the vehicle_type of this BodyRequests.  # noqa: E501


        :return: The vehicle_type of this BodyRequests.  # noqa: E501
        :rtype: VehicleType
        """
        return self._vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        """Sets the vehicle_type of this BodyRequests.


        :param vehicle_type: The vehicle_type of this BodyRequests.  # noqa: E501
        :type: VehicleType
        """

        self._vehicle_type = vehicle_type

    @property
    def select_airlines(self):
        """Gets the select_airlines of this BodyRequests.  # noqa: E501


        :return: The select_airlines of this BodyRequests.  # noqa: E501
        :rtype: SelectAirlines
        """
        return self._select_airlines

    @select_airlines.setter
    def select_airlines(self, select_airlines):
        """Sets the select_airlines of this BodyRequests.


        :param select_airlines: The select_airlines of this BodyRequests.  # noqa: E501
        :type: SelectAirlines
        """

        self._select_airlines = select_airlines

    @property
    def select_airlines_exclude(self):
        """Gets the select_airlines_exclude of this BodyRequests.  # noqa: E501


        :return: The select_airlines_exclude of this BodyRequests.  # noqa: E501
        :rtype: SelectAirlinesExclude
        """
        return self._select_airlines_exclude

    @select_airlines_exclude.setter
    def select_airlines_exclude(self, select_airlines_exclude):
        """Sets the select_airlines_exclude of this BodyRequests.


        :param select_airlines_exclude: The select_airlines_exclude of this BodyRequests.  # noqa: E501
        :type: SelectAirlinesExclude
        """

        self._select_airlines_exclude = select_airlines_exclude

    @property
    def select_stop_airport(self):
        """Gets the select_stop_airport of this BodyRequests.  # noqa: E501


        :return: The select_stop_airport of this BodyRequests.  # noqa: E501
        :rtype: SelectStopAirport
        """
        return self._select_stop_airport

    @select_stop_airport.setter
    def select_stop_airport(self, select_stop_airport):
        """Sets the select_stop_airport of this BodyRequests.


        :param select_stop_airport: The select_stop_airport of this BodyRequests.  # noqa: E501
        :type: SelectStopAirport
        """

        self._select_stop_airport = select_stop_airport

    @property
    def select_stop_airport_exclude(self):
        """Gets the select_stop_airport_exclude of this BodyRequests.  # noqa: E501


        :return: The select_stop_airport_exclude of this BodyRequests.  # noqa: E501
        :rtype: SelectStopAirportExclude
        """
        return self._select_stop_airport_exclude

    @select_stop_airport_exclude.setter
    def select_stop_airport_exclude(self, select_stop_airport_exclude):
        """Sets the select_stop_airport_exclude of this BodyRequests.


        :param select_stop_airport_exclude: The select_stop_airport_exclude of this BodyRequests.  # noqa: E501
        :type: SelectStopAirportExclude
        """

        self._select_stop_airport_exclude = select_stop_airport_exclude

    @property
    def stopover_from(self):
        """Gets the stopover_from of this BodyRequests.  # noqa: E501


        :return: The stopover_from of this BodyRequests.  # noqa: E501
        :rtype: StopoverFrom
        """
        return self._stopover_from

    @stopover_from.setter
    def stopover_from(self, stopover_from):
        """Sets the stopover_from of this BodyRequests.


        :param stopover_from: The stopover_from of this BodyRequests.  # noqa: E501
        :type: StopoverFrom
        """

        self._stopover_from = stopover_from

    @property
    def stopover_to(self):
        """Gets the stopover_to of this BodyRequests.  # noqa: E501


        :return: The stopover_to of this BodyRequests.  # noqa: E501
        :rtype: StopoverTo
        """
        return self._stopover_to

    @stopover_to.setter
    def stopover_to(self, stopover_to):
        """Sets the stopover_to of this BodyRequests.


        :param stopover_to: The stopover_to of this BodyRequests.  # noqa: E501
        :type: StopoverTo
        """

        self._stopover_to = stopover_to

    @property
    def max_stopovers(self):
        """Gets the max_stopovers of this BodyRequests.  # noqa: E501


        :return: The max_stopovers of this BodyRequests.  # noqa: E501
        :rtype: MaxStopovers
        """
        return self._max_stopovers

    @max_stopovers.setter
    def max_stopovers(self, max_stopovers):
        """Sets the max_stopovers of this BodyRequests.


        :param max_stopovers: The max_stopovers of this BodyRequests.  # noqa: E501
        :type: MaxStopovers
        """

        self._max_stopovers = max_stopovers

    @property
    def max_sector_stopovers(self):
        """Gets the max_sector_stopovers of this BodyRequests.  # noqa: E501


        :return: The max_sector_stopovers of this BodyRequests.  # noqa: E501
        :rtype: MaxSectorStopovers
        """
        return self._max_sector_stopovers

    @max_sector_stopovers.setter
    def max_sector_stopovers(self, max_sector_stopovers):
        """Sets the max_sector_stopovers of this BodyRequests.


        :param max_sector_stopovers: The max_sector_stopovers of this BodyRequests.  # noqa: E501
        :type: MaxSectorStopovers
        """

        self._max_sector_stopovers = max_sector_stopovers

    @property
    def conn_on_diff_airport(self):
        """Gets the conn_on_diff_airport of this BodyRequests.  # noqa: E501


        :return: The conn_on_diff_airport of this BodyRequests.  # noqa: E501
        :rtype: ConnOnDiffAirport
        """
        return self._conn_on_diff_airport

    @conn_on_diff_airport.setter
    def conn_on_diff_airport(self, conn_on_diff_airport):
        """Sets the conn_on_diff_airport of this BodyRequests.


        :param conn_on_diff_airport: The conn_on_diff_airport of this BodyRequests.  # noqa: E501
        :type: ConnOnDiffAirport
        """

        self._conn_on_diff_airport = conn_on_diff_airport

    @property
    def selected_cabins(self):
        """Gets the selected_cabins of this BodyRequests.  # noqa: E501


        :return: The selected_cabins of this BodyRequests.  # noqa: E501
        :rtype: SelectedCabins
        """
        return self._selected_cabins

    @selected_cabins.setter
    def selected_cabins(self, selected_cabins):
        """Sets the selected_cabins of this BodyRequests.


        :param selected_cabins: The selected_cabins of this BodyRequests.  # noqa: E501
        :type: SelectedCabins
        """

        self._selected_cabins = selected_cabins

    @property
    def mix_with_cabins(self):
        """Gets the mix_with_cabins of this BodyRequests.  # noqa: E501


        :return: The mix_with_cabins of this BodyRequests.  # noqa: E501
        :rtype: MixWithCabins
        """
        return self._mix_with_cabins

    @mix_with_cabins.setter
    def mix_with_cabins(self, mix_with_cabins):
        """Sets the mix_with_cabins of this BodyRequests.


        :param mix_with_cabins: The mix_with_cabins of this BodyRequests.  # noqa: E501
        :type: MixWithCabins
        """

        self._mix_with_cabins = mix_with_cabins

    @property
    def adults(self):
        """Gets the adults of this BodyRequests.  # noqa: E501


        :return: The adults of this BodyRequests.  # noqa: E501
        :rtype: Adults
        """
        return self._adults

    @adults.setter
    def adults(self, adults):
        """Sets the adults of this BodyRequests.


        :param adults: The adults of this BodyRequests.  # noqa: E501
        :type: Adults
        """

        self._adults = adults

    @property
    def children(self):
        """Gets the children of this BodyRequests.  # noqa: E501


        :return: The children of this BodyRequests.  # noqa: E501
        :rtype: Children
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this BodyRequests.


        :param children: The children of this BodyRequests.  # noqa: E501
        :type: Children
        """

        self._children = children

    @property
    def infants(self):
        """Gets the infants of this BodyRequests.  # noqa: E501


        :return: The infants of this BodyRequests.  # noqa: E501
        :rtype: Infants
        """
        return self._infants

    @infants.setter
    def infants(self, infants):
        """Sets the infants of this BodyRequests.


        :param infants: The infants of this BodyRequests.  # noqa: E501
        :type: Infants
        """

        self._infants = infants

    @property
    def adult_hold_bag(self):
        """Gets the adult_hold_bag of this BodyRequests.  # noqa: E501


        :return: The adult_hold_bag of this BodyRequests.  # noqa: E501
        :rtype: AdultHoldBag
        """
        return self._adult_hold_bag

    @adult_hold_bag.setter
    def adult_hold_bag(self, adult_hold_bag):
        """Sets the adult_hold_bag of this BodyRequests.


        :param adult_hold_bag: The adult_hold_bag of this BodyRequests.  # noqa: E501
        :type: AdultHoldBag
        """

        self._adult_hold_bag = adult_hold_bag

    @property
    def adult_hand_bag(self):
        """Gets the adult_hand_bag of this BodyRequests.  # noqa: E501


        :return: The adult_hand_bag of this BodyRequests.  # noqa: E501
        :rtype: AdultHandBag
        """
        return self._adult_hand_bag

    @adult_hand_bag.setter
    def adult_hand_bag(self, adult_hand_bag):
        """Sets the adult_hand_bag of this BodyRequests.


        :param adult_hand_bag: The adult_hand_bag of this BodyRequests.  # noqa: E501
        :type: AdultHandBag
        """

        self._adult_hand_bag = adult_hand_bag

    @property
    def child_hold_bag(self):
        """Gets the child_hold_bag of this BodyRequests.  # noqa: E501


        :return: The child_hold_bag of this BodyRequests.  # noqa: E501
        :rtype: ChildHoldBag
        """
        return self._child_hold_bag

    @child_hold_bag.setter
    def child_hold_bag(self, child_hold_bag):
        """Sets the child_hold_bag of this BodyRequests.


        :param child_hold_bag: The child_hold_bag of this BodyRequests.  # noqa: E501
        :type: ChildHoldBag
        """

        self._child_hold_bag = child_hold_bag

    @property
    def child_hand_bag(self):
        """Gets the child_hand_bag of this BodyRequests.  # noqa: E501


        :return: The child_hand_bag of this BodyRequests.  # noqa: E501
        :rtype: ChildHandBag
        """
        return self._child_hand_bag

    @child_hand_bag.setter
    def child_hand_bag(self, child_hand_bag):
        """Sets the child_hand_bag of this BodyRequests.


        :param child_hand_bag: The child_hand_bag of this BodyRequests.  # noqa: E501
        :type: ChildHandBag
        """

        self._child_hand_bag = child_hand_bag

    @property
    def price_from(self):
        """Gets the price_from of this BodyRequests.  # noqa: E501


        :return: The price_from of this BodyRequests.  # noqa: E501
        :rtype: PriceFrom
        """
        return self._price_from

    @price_from.setter
    def price_from(self, price_from):
        """Sets the price_from of this BodyRequests.


        :param price_from: The price_from of this BodyRequests.  # noqa: E501
        :type: PriceFrom
        """

        self._price_from = price_from

    @property
    def price_to(self):
        """Gets the price_to of this BodyRequests.  # noqa: E501


        :return: The price_to of this BodyRequests.  # noqa: E501
        :rtype: PriceFrom
        """
        return self._price_to

    @price_to.setter
    def price_to(self, price_to):
        """Sets the price_to of this BodyRequests.


        :param price_to: The price_to of this BodyRequests.  # noqa: E501
        :type: PriceFrom
        """

        self._price_to = price_to

    @property
    def sort(self):
        """Gets the sort of this BodyRequests.  # noqa: E501


        :return: The sort of this BodyRequests.  # noqa: E501
        :rtype: Sort
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this BodyRequests.


        :param sort: The sort of this BodyRequests.  # noqa: E501
        :type: Sort
        """

        self._sort = sort

    @property
    def asc(self):
        """Gets the asc of this BodyRequests.  # noqa: E501


        :return: The asc of this BodyRequests.  # noqa: E501
        :rtype: Asc
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this BodyRequests.


        :param asc: The asc of this BodyRequests.  # noqa: E501
        :type: Asc
        """

        self._asc = asc

    @property
    def limit(self):
        """Gets the limit of this BodyRequests.  # noqa: E501


        :return: The limit of this BodyRequests.  # noqa: E501
        :rtype: Limit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this BodyRequests.


        :param limit: The limit of this BodyRequests.  # noqa: E501
        :type: Limit
        """

        self._limit = limit

    @property
    def date_from(self):
        """Gets the date_from of this BodyRequests.  # noqa: E501


        :return: The date_from of this BodyRequests.  # noqa: E501
        :rtype: DateFrom
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this BodyRequests.


        :param date_from: The date_from of this BodyRequests.  # noqa: E501
        :type: DateFrom
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this BodyRequests.  # noqa: E501


        :return: The date_to of this BodyRequests.  # noqa: E501
        :rtype: DateTo
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this BodyRequests.


        :param date_to: The date_to of this BodyRequests.  # noqa: E501
        :type: DateTo
        """

        self._date_to = date_to

    @property
    def only_working_days(self):
        """Gets the only_working_days of this BodyRequests.  # noqa: E501


        :return: The only_working_days of this BodyRequests.  # noqa: E501
        :rtype: OnlyWorkingDays
        """
        return self._only_working_days

    @only_working_days.setter
    def only_working_days(self, only_working_days):
        """Sets the only_working_days of this BodyRequests.


        :param only_working_days: The only_working_days of this BodyRequests.  # noqa: E501
        :type: OnlyWorkingDays
        """

        self._only_working_days = only_working_days

    @property
    def only_weekends(self):
        """Gets the only_weekends of this BodyRequests.  # noqa: E501


        :return: The only_weekends of this BodyRequests.  # noqa: E501
        :rtype: OnlyWeekends
        """
        return self._only_weekends

    @only_weekends.setter
    def only_weekends(self, only_weekends):
        """Sets the only_weekends of this BodyRequests.


        :param only_weekends: The only_weekends of this BodyRequests.  # noqa: E501
        :type: OnlyWeekends
        """

        self._only_weekends = only_weekends

    @property
    def direct_flights(self):
        """Gets the direct_flights of this BodyRequests.  # noqa: E501


        :return: The direct_flights of this BodyRequests.  # noqa: E501
        :rtype: DirectFlights
        """
        return self._direct_flights

    @direct_flights.setter
    def direct_flights(self, direct_flights):
        """Sets the direct_flights of this BodyRequests.


        :param direct_flights: The direct_flights of this BodyRequests.  # noqa: E501
        :type: DirectFlights
        """

        self._direct_flights = direct_flights

    @property
    def v(self):
        """Gets the v of this BodyRequests.  # noqa: E501


        :return: The v of this BodyRequests.  # noqa: E501
        :rtype: V
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this BodyRequests.


        :param v: The v of this BodyRequests.  # noqa: E501
        :type: V
        """

        self._v = v

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
        if issubclass(BodyRequests, dict):
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
        if not isinstance(other, BodyRequests):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
