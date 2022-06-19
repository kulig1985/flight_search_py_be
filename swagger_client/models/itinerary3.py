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

class Itinerary3(object):
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
        'booking_token': 'BookingToken',
        'deep_link': 'DeepLink',
        'price': 'Price',
        'duration': 'Total',
        'pnr_count': 'PnrCount',
        'currency': 'Currency',
        'baglimit': 'Baglimit',
        'bags_price': 'BagsPrice',
        'route': 'list[Sector2]'
    }

    attribute_map = {
        'id': 'id',
        'booking_token': 'booking_token',
        'deep_link': 'deep_link',
        'price': 'price',
        'duration': 'duration',
        'pnr_count': 'pnr_count',
        'currency': 'currency',
        'baglimit': 'baglimit',
        'bags_price': 'bags_price',
        'route': 'route'
    }

    def __init__(self, id=None, booking_token=None, deep_link=None, price=None, duration=None, pnr_count=None, currency=None, baglimit=None, bags_price=None, route=None):  # noqa: E501
        """Itinerary3 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._booking_token = None
        self._deep_link = None
        self._price = None
        self._duration = None
        self._pnr_count = None
        self._currency = None
        self._baglimit = None
        self._bags_price = None
        self._route = None
        self.discriminator = None
        self.id = id
        if booking_token is not None:
            self.booking_token = booking_token
        if deep_link is not None:
            self.deep_link = deep_link
        if price is not None:
            self.price = price
        if duration is not None:
            self.duration = duration
        if pnr_count is not None:
            self.pnr_count = pnr_count
        if currency is not None:
            self.currency = currency
        if baglimit is not None:
            self.baglimit = baglimit
        if bags_price is not None:
            self.bags_price = bags_price
        if route is not None:
            self.route = route

    @property
    def id(self):
        """Gets the id of this Itinerary3.  # noqa: E501


        :return: The id of this Itinerary3.  # noqa: E501
        :rtype: ItineraryId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Itinerary3.


        :param id: The id of this Itinerary3.  # noqa: E501
        :type: ItineraryId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def booking_token(self):
        """Gets the booking_token of this Itinerary3.  # noqa: E501


        :return: The booking_token of this Itinerary3.  # noqa: E501
        :rtype: BookingToken
        """
        return self._booking_token

    @booking_token.setter
    def booking_token(self, booking_token):
        """Sets the booking_token of this Itinerary3.


        :param booking_token: The booking_token of this Itinerary3.  # noqa: E501
        :type: BookingToken
        """

        self._booking_token = booking_token

    @property
    def deep_link(self):
        """Gets the deep_link of this Itinerary3.  # noqa: E501


        :return: The deep_link of this Itinerary3.  # noqa: E501
        :rtype: DeepLink
        """
        return self._deep_link

    @deep_link.setter
    def deep_link(self, deep_link):
        """Sets the deep_link of this Itinerary3.


        :param deep_link: The deep_link of this Itinerary3.  # noqa: E501
        :type: DeepLink
        """

        self._deep_link = deep_link

    @property
    def price(self):
        """Gets the price of this Itinerary3.  # noqa: E501


        :return: The price of this Itinerary3.  # noqa: E501
        :rtype: Price
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Itinerary3.


        :param price: The price of this Itinerary3.  # noqa: E501
        :type: Price
        """

        self._price = price

    @property
    def duration(self):
        """Gets the duration of this Itinerary3.  # noqa: E501


        :return: The duration of this Itinerary3.  # noqa: E501
        :rtype: Total
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Itinerary3.


        :param duration: The duration of this Itinerary3.  # noqa: E501
        :type: Total
        """

        self._duration = duration

    @property
    def pnr_count(self):
        """Gets the pnr_count of this Itinerary3.  # noqa: E501


        :return: The pnr_count of this Itinerary3.  # noqa: E501
        :rtype: PnrCount
        """
        return self._pnr_count

    @pnr_count.setter
    def pnr_count(self, pnr_count):
        """Sets the pnr_count of this Itinerary3.


        :param pnr_count: The pnr_count of this Itinerary3.  # noqa: E501
        :type: PnrCount
        """

        self._pnr_count = pnr_count

    @property
    def currency(self):
        """Gets the currency of this Itinerary3.  # noqa: E501


        :return: The currency of this Itinerary3.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Itinerary3.


        :param currency: The currency of this Itinerary3.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def baglimit(self):
        """Gets the baglimit of this Itinerary3.  # noqa: E501


        :return: The baglimit of this Itinerary3.  # noqa: E501
        :rtype: Baglimit
        """
        return self._baglimit

    @baglimit.setter
    def baglimit(self, baglimit):
        """Sets the baglimit of this Itinerary3.


        :param baglimit: The baglimit of this Itinerary3.  # noqa: E501
        :type: Baglimit
        """

        self._baglimit = baglimit

    @property
    def bags_price(self):
        """Gets the bags_price of this Itinerary3.  # noqa: E501


        :return: The bags_price of this Itinerary3.  # noqa: E501
        :rtype: BagsPrice
        """
        return self._bags_price

    @bags_price.setter
    def bags_price(self, bags_price):
        """Sets the bags_price of this Itinerary3.


        :param bags_price: The bags_price of this Itinerary3.  # noqa: E501
        :type: BagsPrice
        """

        self._bags_price = bags_price

    @property
    def route(self):
        """Gets the route of this Itinerary3.  # noqa: E501

        List of sectors.  # noqa: E501

        :return: The route of this Itinerary3.  # noqa: E501
        :rtype: list[Sector2]
        """
        return self._route

    @route.setter
    def route(self, route):
        """Sets the route of this Itinerary3.

        List of sectors.  # noqa: E501

        :param route: The route of this Itinerary3.  # noqa: E501
        :type: list[Sector2]
        """

        self._route = route

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
        if issubclass(Itinerary3, dict):
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
        if not isinstance(other, Itinerary3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other