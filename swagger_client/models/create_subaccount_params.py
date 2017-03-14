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


class CreateSubaccountParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, username=None, password=None, contact=None, billing_contact=None):
        """
        CreateSubaccountParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'username': 'str',
            'password': 'str',
            'contact': 'ContactSubaccount',
            'billing_contact': 'ContactSubaccount'
        }

        self.attribute_map = {
            'username': 'username',
            'password': 'password',
            'contact': 'contact',
            'billing_contact': 'billing_contact'
        }

        self._username = username
        self._password = password
        self._contact = contact
        self._billing_contact = billing_contact

    @property
    def username(self):
        """
        Gets the username of this CreateSubaccountParams.
        Sub account password

        :return: The username of this CreateSubaccountParams.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateSubaccountParams.
        Sub account password

        :param username: The username of this CreateSubaccountParams.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def password(self):
        """
        Gets the password of this CreateSubaccountParams.
        Sub account password

        :return: The password of this CreateSubaccountParams.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateSubaccountParams.
        Sub account password

        :param password: The password of this CreateSubaccountParams.
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")

        self._password = password

    @property
    def contact(self):
        """
        Gets the contact of this CreateSubaccountParams.
        Contact Object. See below for details.

        :return: The contact of this CreateSubaccountParams.
        :rtype: ContactSubaccount
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this CreateSubaccountParams.
        Contact Object. See below for details.

        :param contact: The contact of this CreateSubaccountParams.
        :type: ContactSubaccount
        """

        self._contact = contact

    @property
    def billing_contact(self):
        """
        Gets the billing_contact of this CreateSubaccountParams.
        Contact Object for billing purposes. See below for details.

        :return: The billing_contact of this CreateSubaccountParams.
        :rtype: ContactSubaccount
        """
        return self._billing_contact

    @billing_contact.setter
    def billing_contact(self, billing_contact):
        """
        Sets the billing_contact of this CreateSubaccountParams.
        Contact Object for billing purposes. See below for details.

        :param billing_contact: The billing_contact of this CreateSubaccountParams.
        :type: ContactSubaccount
        """

        self._billing_contact = billing_contact

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
        if not isinstance(other, CreateSubaccountParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
