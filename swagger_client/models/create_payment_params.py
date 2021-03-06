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


class CreatePaymentParams(object):
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
        'nickname': 'str',
        'status': 'str',
        'type': 'str',
        'cc_token': 'str'
    }

    attribute_map = {
        'nickname': 'nickname',
        'status': 'status',
        'type': 'type',
        'cc_token': 'cc_token'
    }

    def __init__(self, nickname=None, status=None, type=None, cc_token=None):
        """
        CreatePaymentParams - a model defined in Swagger
        """

        self._nickname = None
        self._status = None
        self._type = None
        self._cc_token = None

        if nickname is not None:
          self.nickname = nickname
        if status is not None:
          self.status = status
        if type is not None:
          self.type = type
        if cc_token is not None:
          self.cc_token = cc_token

    @property
    def nickname(self):
        """
        Gets the nickname of this CreatePaymentParams.
        Name of payment method

        :return: The nickname of this CreatePaymentParams.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this CreatePaymentParams.
        Name of payment method

        :param nickname: The nickname of this CreatePaymentParams.
        :type: str
        """

        self._nickname = nickname

    @property
    def status(self):
        """
        Gets the status of this CreatePaymentParams.
        primary, onfile or hidden

        :return: The status of this CreatePaymentParams.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this CreatePaymentParams.
        primary, onfile or hidden

        :param status: The status of this CreatePaymentParams.
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """
        Gets the type of this CreatePaymentParams.
        Credit Card Type

        :return: The type of this CreatePaymentParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreatePaymentParams.
        Credit Card Type

        :param type: The type of this CreatePaymentParams.
        :type: str
        """

        self._type = type

    @property
    def cc_token(self):
        """
        Gets the cc_token of this CreatePaymentParams.
        Credit Card Token. Token is obtained by entering credit card info via the Credit Card Entry Form

        :return: The cc_token of this CreatePaymentParams.
        :rtype: str
        """
        return self._cc_token

    @cc_token.setter
    def cc_token(self, cc_token):
        """
        Sets the cc_token of this CreatePaymentParams.
        Credit Card Token. Token is obtained by entering credit card info via the Credit Card Entry Form

        :param cc_token: The cc_token of this CreatePaymentParams.
        :type: str
        """

        self._cc_token = cc_token

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
        if not isinstance(other, CreatePaymentParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
