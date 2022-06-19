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

class InlineResponse2002(object):
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
        'search_id': 'SearchId',
        'currency': 'Currency',
        'fx_rate': 'FxRate',
        'data': 'list[Itinerary3]',
        'currency_rate': 'CurrencyRate',
        'time': 'Time',
        'connections': 'Connections',
        'search_params': 'SearchParams',
        'refresh': 'Refresh',
        'ref_tasks': 'RefTasks'
    }

    attribute_map = {
        'search_id': 'search_id',
        'currency': 'currency',
        'fx_rate': 'fx_rate',
        'data': 'data',
        'currency_rate': 'currency_rate',
        'time': 'time',
        'connections': 'connections',
        'search_params': 'search_params',
        'refresh': 'refresh',
        'ref_tasks': 'ref_tasks'
    }

    def __init__(self, search_id=None, currency=None, fx_rate=None, data=None, currency_rate=None, time=None, connections=None, search_params=None, refresh=None, ref_tasks=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501
        self._search_id = None
        self._currency = None
        self._fx_rate = None
        self._data = None
        self._currency_rate = None
        self._time = None
        self._connections = None
        self._search_params = None
        self._refresh = None
        self._ref_tasks = None
        self.discriminator = None
        if search_id is not None:
            self.search_id = search_id
        if currency is not None:
            self.currency = currency
        if fx_rate is not None:
            self.fx_rate = fx_rate
        if data is not None:
            self.data = data
        if currency_rate is not None:
            self.currency_rate = currency_rate
        if time is not None:
            self.time = time
        if connections is not None:
            self.connections = connections
        if search_params is not None:
            self.search_params = search_params
        if refresh is not None:
            self.refresh = refresh
        if ref_tasks is not None:
            self.ref_tasks = ref_tasks

    @property
    def search_id(self):
        """Gets the search_id of this InlineResponse2002.  # noqa: E501


        :return: The search_id of this InlineResponse2002.  # noqa: E501
        :rtype: SearchId
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this InlineResponse2002.


        :param search_id: The search_id of this InlineResponse2002.  # noqa: E501
        :type: SearchId
        """

        self._search_id = search_id

    @property
    def currency(self):
        """Gets the currency of this InlineResponse2002.  # noqa: E501


        :return: The currency of this InlineResponse2002.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InlineResponse2002.


        :param currency: The currency of this InlineResponse2002.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def fx_rate(self):
        """Gets the fx_rate of this InlineResponse2002.  # noqa: E501


        :return: The fx_rate of this InlineResponse2002.  # noqa: E501
        :rtype: FxRate
        """
        return self._fx_rate

    @fx_rate.setter
    def fx_rate(self, fx_rate):
        """Sets the fx_rate of this InlineResponse2002.


        :param fx_rate: The fx_rate of this InlineResponse2002.  # noqa: E501
        :type: FxRate
        """

        self._fx_rate = fx_rate

    @property
    def data(self):
        """Gets the data of this InlineResponse2002.  # noqa: E501

        List of itineraries.  # noqa: E501

        :return: The data of this InlineResponse2002.  # noqa: E501
        :rtype: list[Itinerary3]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse2002.

        List of itineraries.  # noqa: E501

        :param data: The data of this InlineResponse2002.  # noqa: E501
        :type: list[Itinerary3]
        """

        self._data = data

    @property
    def currency_rate(self):
        """Gets the currency_rate of this InlineResponse2002.  # noqa: E501


        :return: The currency_rate of this InlineResponse2002.  # noqa: E501
        :rtype: CurrencyRate
        """
        return self._currency_rate

    @currency_rate.setter
    def currency_rate(self, currency_rate):
        """Sets the currency_rate of this InlineResponse2002.


        :param currency_rate: The currency_rate of this InlineResponse2002.  # noqa: E501
        :type: CurrencyRate
        """

        self._currency_rate = currency_rate

    @property
    def time(self):
        """Gets the time of this InlineResponse2002.  # noqa: E501


        :return: The time of this InlineResponse2002.  # noqa: E501
        :rtype: Time
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse2002.


        :param time: The time of this InlineResponse2002.  # noqa: E501
        :type: Time
        """

        self._time = time

    @property
    def connections(self):
        """Gets the connections of this InlineResponse2002.  # noqa: E501


        :return: The connections of this InlineResponse2002.  # noqa: E501
        :rtype: Connections
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this InlineResponse2002.


        :param connections: The connections of this InlineResponse2002.  # noqa: E501
        :type: Connections
        """

        self._connections = connections

    @property
    def search_params(self):
        """Gets the search_params of this InlineResponse2002.  # noqa: E501


        :return: The search_params of this InlineResponse2002.  # noqa: E501
        :rtype: SearchParams
        """
        return self._search_params

    @search_params.setter
    def search_params(self, search_params):
        """Sets the search_params of this InlineResponse2002.


        :param search_params: The search_params of this InlineResponse2002.  # noqa: E501
        :type: SearchParams
        """

        self._search_params = search_params

    @property
    def refresh(self):
        """Gets the refresh of this InlineResponse2002.  # noqa: E501


        :return: The refresh of this InlineResponse2002.  # noqa: E501
        :rtype: Refresh
        """
        return self._refresh

    @refresh.setter
    def refresh(self, refresh):
        """Sets the refresh of this InlineResponse2002.


        :param refresh: The refresh of this InlineResponse2002.  # noqa: E501
        :type: Refresh
        """

        self._refresh = refresh

    @property
    def ref_tasks(self):
        """Gets the ref_tasks of this InlineResponse2002.  # noqa: E501


        :return: The ref_tasks of this InlineResponse2002.  # noqa: E501
        :rtype: RefTasks
        """
        return self._ref_tasks

    @ref_tasks.setter
    def ref_tasks(self, ref_tasks):
        """Sets the ref_tasks of this InlineResponse2002.


        :param ref_tasks: The ref_tasks of this InlineResponse2002.  # noqa: E501
        :type: RefTasks
        """

        self._ref_tasks = ref_tasks

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
