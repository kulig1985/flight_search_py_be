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

class SearchParams(object):
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
        'fly_from_type': 'str',
        'to_type': 'str',
        'seats': 'object'
    }

    attribute_map = {
        'fly_from_type': 'flyFrom_type',
        'to_type': 'to_type',
        'seats': 'seats'
    }

    def __init__(self, fly_from_type=None, to_type=None, seats=None):  # noqa: E501
        """SearchParams - a model defined in Swagger"""  # noqa: E501
        self._fly_from_type = None
        self._to_type = None
        self._seats = None
        self.discriminator = None
        if fly_from_type is not None:
            self.fly_from_type = fly_from_type
        if to_type is not None:
            self.to_type = to_type
        if seats is not None:
            self.seats = seats

    @property
    def fly_from_type(self):
        """Gets the fly_from_type of this SearchParams.  # noqa: E501

        It's based on extracted departure locations from the request. The type which is most numerous among all the extracted locations, will be specified here.  # noqa: E501

        :return: The fly_from_type of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._fly_from_type

    @fly_from_type.setter
    def fly_from_type(self, fly_from_type):
        """Sets the fly_from_type of this SearchParams.

        It's based on extracted departure locations from the request. The type which is most numerous among all the extracted locations, will be specified here.  # noqa: E501

        :param fly_from_type: The fly_from_type of this SearchParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["airport", "city"]  # noqa: E501
        if fly_from_type not in allowed_values:
            raise ValueError(
                "Invalid value for `fly_from_type` ({0}), must be one of {1}"  # noqa: E501
                .format(fly_from_type, allowed_values)
            )

        self._fly_from_type = fly_from_type

    @property
    def to_type(self):
        """Gets the to_type of this SearchParams.  # noqa: E501

        It's based on extracted destination locations from the request. The type which is most numerous among all the extracted locations, will be specified here.  # noqa: E501

        :return: The to_type of this SearchParams.  # noqa: E501
        :rtype: str
        """
        return self._to_type

    @to_type.setter
    def to_type(self, to_type):
        """Sets the to_type of this SearchParams.

        It's based on extracted destination locations from the request. The type which is most numerous among all the extracted locations, will be specified here.  # noqa: E501

        :param to_type: The to_type of this SearchParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["airport", "city"]  # noqa: E501
        if to_type not in allowed_values:
            raise ValueError(
                "Invalid value for `to_type` ({0}), must be one of {1}"  # noqa: E501
                .format(to_type, allowed_values)
            )

        self._to_type = to_type

    @property
    def seats(self):
        """Gets the seats of this SearchParams.  # noqa: E501

        Numbers of requested passengers.  # noqa: E501

        :return: The seats of this SearchParams.  # noqa: E501
        :rtype: object
        """
        return self._seats

    @seats.setter
    def seats(self, seats):
        """Sets the seats of this SearchParams.

        Numbers of requested passengers.  # noqa: E501

        :param seats: The seats of this SearchParams.  # noqa: E501
        :type: object
        """

        self._seats = seats

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
        if issubclass(SearchParams, dict):
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
        if not isinstance(other, SearchParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
