# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PhoneNumberContact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type=None, number=None, normalized=None):
        """
        PhoneNumberContact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'number': 'str',
            'normalized': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'number': 'number',
            'normalized': 'normalized'
        }

        self._type = type
        self._number = number
        self._normalized = normalized

    @property
    def type(self):
        """
        Gets the type of this PhoneNumberContact.
        Type of phone number, must be one of: home, business, mobile, fax, pager. Default is home.

        :return: The type of this PhoneNumberContact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PhoneNumberContact.
        Type of phone number, must be one of: home, business, mobile, fax, pager. Default is home.

        :param type: The type of this PhoneNumberContact.
        :type: str
        """

        self._type = type

    @property
    def number(self):
        """
        Gets the number of this PhoneNumberContact.
        Phone number, as entered. Does not need to be formatted in any particular way. Required.

        :return: The number of this PhoneNumberContact.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this PhoneNumberContact.
        Phone number, as entered. Does not need to be formatted in any particular way. Required.

        :param number: The number of this PhoneNumberContact.
        :type: str
        """

        self._number = number

    @property
    def normalized(self):
        """
        Gets the normalized of this PhoneNumberContact.
        Phone number in E.164 format. Read-only.

        :return: The normalized of this PhoneNumberContact.
        :rtype: str
        """
        return self._normalized

    @normalized.setter
    def normalized(self, normalized):
        """
        Sets the normalized of this PhoneNumberContact.
        Phone number in E.164 format. Read-only.

        :param normalized: The normalized of this PhoneNumberContact.
        :type: str
        """

        self._normalized = normalized

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PhoneNumberContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
