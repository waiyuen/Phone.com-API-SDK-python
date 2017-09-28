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


class PricingFull(object):
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
        'id': 'int',
        'pricing': 'PricingObject',
        'voip_id': 'int',
        'reason': 'str',
        'who': 'str',
        'expire_date': 'str'
    }

    attribute_map = {
        'id': 'id',
        'pricing': 'pricing',
        'voip_id': 'voip_id',
        'reason': 'reason',
        'who': 'who',
        'expire_date': 'expire_date'
    }

    def __init__(self, id=None, pricing=None, voip_id=None, reason=None, who=None, expire_date=None):
        """
        PricingFull - a model defined in Swagger
        """

        self._id = None
        self._pricing = None
        self._voip_id = None
        self._reason = None
        self._who = None
        self._expire_date = None

        if id is not None:
          self.id = id
        if pricing is not None:
          self.pricing = pricing
        if voip_id is not None:
          self.voip_id = voip_id
        if reason is not None:
          self.reason = reason
        if who is not None:
          self.who = who
        if expire_date is not None:
          self.expire_date = expire_date

    @property
    def id(self):
        """
        Gets the id of this PricingFull.
        Integer ID of this object.

        :return: The id of this PricingFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PricingFull.
        Integer ID of this object.

        :param id: The id of this PricingFull.
        :type: int
        """

        self._id = id

    @property
    def pricing(self):
        """
        Gets the pricing of this PricingFull.
        Pricing Object

        :return: The pricing of this PricingFull.
        :rtype: PricingObject
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """
        Sets the pricing of this PricingFull.
        Pricing Object

        :param pricing: The pricing of this PricingFull.
        :type: PricingObject
        """

        self._pricing = pricing

    @property
    def voip_id(self):
        """
        Gets the voip_id of this PricingFull.
        Phone.com API Account (VoIP) ID

        :return: The voip_id of this PricingFull.
        :rtype: int
        """
        return self._voip_id

    @voip_id.setter
    def voip_id(self, voip_id):
        """
        Sets the voip_id of this PricingFull.
        Phone.com API Account (VoIP) ID

        :param voip_id: The voip_id of this PricingFull.
        :type: int
        """

        self._voip_id = voip_id

    @property
    def reason(self):
        """
        Gets the reason of this PricingFull.
        Reason this pricing plan is applied

        :return: The reason of this PricingFull.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this PricingFull.
        Reason this pricing plan is applied

        :param reason: The reason of this PricingFull.
        :type: str
        """

        self._reason = reason

    @property
    def who(self):
        """
        Gets the who of this PricingFull.
        Name of the person / process who added this pricing plan to the subaccount

        :return: The who of this PricingFull.
        :rtype: str
        """
        return self._who

    @who.setter
    def who(self, who):
        """
        Sets the who of this PricingFull.
        Name of the person / process who added this pricing plan to the subaccount

        :param who: The who of this PricingFull.
        :type: str
        """

        self._who = who

    @property
    def expire_date(self):
        """
        Gets the expire_date of this PricingFull.
        Pricing plan expiration timestamp in unix format. If pricing plan never expires, this item will not be returned

        :return: The expire_date of this PricingFull.
        :rtype: str
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """
        Sets the expire_date of this PricingFull.
        Pricing plan expiration timestamp in unix format. If pricing plan never expires, this item will not be returned

        :param expire_date: The expire_date of this PricingFull.
        :type: str
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
        if not isinstance(other, PricingFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other