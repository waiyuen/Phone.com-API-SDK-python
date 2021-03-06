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


class CreatePricingParams(object):
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
        'pricing_id': 'int',
        'reason': 'str',
        'expire_date': 'int'
    }

    attribute_map = {
        'pricing_id': 'pricing_id',
        'reason': 'reason',
        'expire_date': 'expire_date'
    }

    def __init__(self, pricing_id=None, reason=None, expire_date=None):
        """
        CreatePricingParams - a model defined in Swagger
        """

        self._pricing_id = None
        self._reason = None
        self._expire_date = None

        if pricing_id is not None:
          self.pricing_id = pricing_id
        if reason is not None:
          self.reason = reason
        if expire_date is not None:
          self.expire_date = expire_date

    @property
    def pricing_id(self):
        """
        Gets the pricing_id of this CreatePricingParams.
        Pricing plan code

        :return: The pricing_id of this CreatePricingParams.
        :rtype: int
        """
        return self._pricing_id

    @pricing_id.setter
    def pricing_id(self, pricing_id):
        """
        Sets the pricing_id of this CreatePricingParams.
        Pricing plan code

        :param pricing_id: The pricing_id of this CreatePricingParams.
        :type: int
        """

        self._pricing_id = pricing_id

    @property
    def reason(self):
        """
        Gets the reason of this CreatePricingParams.
        Reason this pricing plan is added to the subaccount

        :return: The reason of this CreatePricingParams.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this CreatePricingParams.
        Reason this pricing plan is added to the subaccount

        :param reason: The reason of this CreatePricingParams.
        :type: str
        """

        self._reason = reason

    @property
    def expire_date(self):
        """
        Gets the expire_date of this CreatePricingParams.
        Pricing plan expiration time in UNIX format. Disregard or set it to null for plan which never expires

        :return: The expire_date of this CreatePricingParams.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """
        Sets the expire_date of this CreatePricingParams.
        Pricing plan expiration time in UNIX format. Disregard or set it to null for plan which never expires

        :param expire_date: The expire_date of this CreatePricingParams.
        :type: int
        """

        self._expire_date = expire_date

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
        if not isinstance(other, CreatePricingParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
