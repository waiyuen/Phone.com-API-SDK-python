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


class SortListPhoneNumbersRegions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country_code=None, npa=None, nxx=None, is_toll_free=None, city=None, province_postal_code=None, country_postal_code=None):
        """
        SortListPhoneNumbersRegions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country_code': 'str',
            'npa': 'str',
            'nxx': 'str',
            'is_toll_free': 'str',
            'city': 'str',
            'province_postal_code': 'str',
            'country_postal_code': 'str'
        }

        self.attribute_map = {
            'country_code': 'country_code',
            'npa': 'npa',
            'nxx': 'nxx',
            'is_toll_free': 'is_toll_free',
            'city': 'city',
            'province_postal_code': 'province_postal_code',
            'country_postal_code': 'country_postal_code'
        }

        self._country_code = country_code
        self._npa = npa
        self._nxx = nxx
        self._is_toll_free = is_toll_free
        self._city = city
        self._province_postal_code = province_postal_code
        self._country_postal_code = country_postal_code

    @property
    def country_code(self):
        """
        Gets the country_code of this SortListPhoneNumbersRegions.

        :return: The country_code of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this SortListPhoneNumbersRegions.

        :param country_code: The country_code of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._country_code = country_code

    @property
    def npa(self):
        """
        Gets the npa of this SortListPhoneNumbersRegions.

        :return: The npa of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._npa

    @npa.setter
    def npa(self, npa):
        """
        Sets the npa of this SortListPhoneNumbersRegions.

        :param npa: The npa of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._npa = npa

    @property
    def nxx(self):
        """
        Gets the nxx of this SortListPhoneNumbersRegions.

        :return: The nxx of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._nxx

    @nxx.setter
    def nxx(self, nxx):
        """
        Sets the nxx of this SortListPhoneNumbersRegions.

        :param nxx: The nxx of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._nxx = nxx

    @property
    def is_toll_free(self):
        """
        Gets the is_toll_free of this SortListPhoneNumbersRegions.

        :return: The is_toll_free of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._is_toll_free

    @is_toll_free.setter
    def is_toll_free(self, is_toll_free):
        """
        Sets the is_toll_free of this SortListPhoneNumbersRegions.

        :param is_toll_free: The is_toll_free of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._is_toll_free = is_toll_free

    @property
    def city(self):
        """
        Gets the city of this SortListPhoneNumbersRegions.

        :return: The city of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this SortListPhoneNumbersRegions.

        :param city: The city of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._city = city

    @property
    def province_postal_code(self):
        """
        Gets the province_postal_code of this SortListPhoneNumbersRegions.

        :return: The province_postal_code of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._province_postal_code

    @province_postal_code.setter
    def province_postal_code(self, province_postal_code):
        """
        Sets the province_postal_code of this SortListPhoneNumbersRegions.

        :param province_postal_code: The province_postal_code of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._province_postal_code = province_postal_code

    @property
    def country_postal_code(self):
        """
        Gets the country_postal_code of this SortListPhoneNumbersRegions.

        :return: The country_postal_code of this SortListPhoneNumbersRegions.
        :rtype: str
        """
        return self._country_postal_code

    @country_postal_code.setter
    def country_postal_code(self, country_postal_code):
        """
        Sets the country_postal_code of this SortListPhoneNumbersRegions.

        :param country_postal_code: The country_postal_code of this SortListPhoneNumbersRegions.
        :type: str
        """

        self._country_postal_code = country_postal_code

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
        if not isinstance(other, SortListPhoneNumbersRegions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
