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


class ContactResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'name': 'str',
        'address': 'Address',
        'primary_email': 'str',
        'alternate_email': 'str',
        'company': 'str',
        'phone': 'str',
        'fax': 'str'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'primary_email': 'primary_email',
        'alternate_email': 'alternate_email',
        'company': 'company',
        'phone': 'phone',
        'fax': 'fax'
    }

    def __init__(self, name=None, address=None, primary_email=None, alternate_email=None, company=None, phone=None, fax=None):
        """
        ContactResponse - a model defined in Swagger
        """

        self._name = None
        self._address = None
        self._primary_email = None
        self._alternate_email = None
        self._company = None
        self._phone = None
        self._fax = None

        if name is not None:
          self.name = name
        if address is not None:
          self.address = address
        if primary_email is not None:
          self.primary_email = primary_email
        if alternate_email is not None:
          self.alternate_email = alternate_email
        if company is not None:
          self.company = company
        if phone is not None:
          self.phone = phone
        if fax is not None:
          self.fax = fax

    @property
    def name(self):
        """
        Gets the name of this ContactResponse.
        Contact name

        :return: The name of this ContactResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ContactResponse.
        Contact name

        :param name: The name of this ContactResponse.
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this ContactResponse.

        :return: The address of this ContactResponse.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ContactResponse.

        :param address: The address of this ContactResponse.
        :type: Address
        """

        self._address = address

    @property
    def primary_email(self):
        """
        Gets the primary_email of this ContactResponse.
        Primary email address. Required.

        :return: The primary_email of this ContactResponse.
        :rtype: str
        """
        return self._primary_email

    @primary_email.setter
    def primary_email(self, primary_email):
        """
        Sets the primary_email of this ContactResponse.
        Primary email address. Required.

        :param primary_email: The primary_email of this ContactResponse.
        :type: str
        """

        self._primary_email = primary_email

    @property
    def alternate_email(self):
        """
        Gets the alternate_email of this ContactResponse.
        Alternate email address

        :return: The alternate_email of this ContactResponse.
        :rtype: str
        """
        return self._alternate_email

    @alternate_email.setter
    def alternate_email(self, alternate_email):
        """
        Sets the alternate_email of this ContactResponse.
        Alternate email address

        :param alternate_email: The alternate_email of this ContactResponse.
        :type: str
        """

        self._alternate_email = alternate_email

    @property
    def company(self):
        """
        Gets the company of this ContactResponse.
        Company name

        :return: The company of this ContactResponse.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this ContactResponse.
        Company name

        :param company: The company of this ContactResponse.
        :type: str
        """

        self._company = company

    @property
    def phone(self):
        """
        Gets the phone of this ContactResponse.
        Phone number. Required.

        :return: The phone of this ContactResponse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this ContactResponse.
        Phone number. Required.

        :param phone: The phone of this ContactResponse.
        :type: str
        """

        self._phone = phone

    @property
    def fax(self):
        """
        Gets the fax of this ContactResponse.
        Fax number

        :return: The fax of this ContactResponse.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this ContactResponse.
        Fax number

        :param fax: The fax of this ContactResponse.
        :type: str
        """

        self._fax = fax

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
        if not isinstance(other, ContactResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
