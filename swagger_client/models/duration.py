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

class Duration(object):
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
        'departure': 'int',
        '_return': 'int',
        'total': 'int'
    }

    attribute_map = {
        'departure': 'departure',
        '_return': 'return',
        'total': 'total'
    }

    def __init__(self, departure=None, _return=None, total=None):  # noqa: E501
        """Duration - a model defined in Swagger"""  # noqa: E501
        self._departure = None
        self.__return = None
        self._total = None
        self.discriminator = None
        if departure is not None:
            self.departure = departure
        if _return is not None:
            self._return = _return
        if total is not None:
            self.total = total

    @property
    def departure(self):
        """Gets the departure of this Duration.  # noqa: E501

        The duration of itinerary outbound part in seconds.  # noqa: E501

        :return: The departure of this Duration.  # noqa: E501
        :rtype: int
        """
        return self._departure

    @departure.setter
    def departure(self, departure):
        """Sets the departure of this Duration.

        The duration of itinerary outbound part in seconds.  # noqa: E501

        :param departure: The departure of this Duration.  # noqa: E501
        :type: int
        """

        self._departure = departure

    @property
    def _return(self):
        """Gets the _return of this Duration.  # noqa: E501

        The duration of itinerary inbound part in seconds.  # noqa: E501

        :return: The _return of this Duration.  # noqa: E501
        :rtype: int
        """
        return self.__return

    @_return.setter
    def _return(self, _return):
        """Sets the _return of this Duration.

        The duration of itinerary inbound part in seconds.  # noqa: E501

        :param _return: The _return of this Duration.  # noqa: E501
        :type: int
        """

        self.__return = _return

    @property
    def total(self):
        """Gets the total of this Duration.  # noqa: E501

        The duration of whole itinerary in seconds.  # noqa: E501

        :return: The total of this Duration.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Duration.

        The duration of whole itinerary in seconds.  # noqa: E501

        :param total: The total of this Duration.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(Duration, dict):
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
        if not isinstance(other, Duration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
