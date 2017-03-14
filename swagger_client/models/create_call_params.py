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


class CreateCallParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, caller_phone_number=None, caller_extension=None, caller_caller_id=None, caller_private=None, callee_phone_number=None, callee_extension=None, callee_caller_id=None, callee_private=None):
        """
        CreateCallParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'caller_phone_number': 'str',
            'caller_extension': 'int',
            'caller_caller_id': 'str',
            'caller_private': 'bool',
            'callee_phone_number': 'str',
            'callee_extension': 'int',
            'callee_caller_id': 'str',
            'callee_private': 'bool'
        }

        self.attribute_map = {
            'caller_phone_number': 'caller_phone_number',
            'caller_extension': 'caller_extension',
            'caller_caller_id': 'caller_caller_id',
            'caller_private': 'caller_private',
            'callee_phone_number': 'callee_phone_number',
            'callee_extension': 'callee_extension',
            'callee_caller_id': 'callee_caller_id',
            'callee_private': 'callee_private'
        }

        self._caller_phone_number = caller_phone_number
        self._caller_extension = caller_extension
        self._caller_caller_id = caller_caller_id
        self._caller_private = caller_private
        self._callee_phone_number = callee_phone_number
        self._callee_extension = callee_extension
        self._callee_caller_id = callee_caller_id
        self._callee_private = callee_private

    @property
    def caller_phone_number(self):
        """
        Gets the caller_phone_number of this CreateCallParams.
        Caller phone number in E.164 format

        :return: The caller_phone_number of this CreateCallParams.
        :rtype: str
        """
        return self._caller_phone_number

    @caller_phone_number.setter
    def caller_phone_number(self, caller_phone_number):
        """
        Sets the caller_phone_number of this CreateCallParams.
        Caller phone number in E.164 format

        :param caller_phone_number: The caller_phone_number of this CreateCallParams.
        :type: str
        """

        self._caller_phone_number = caller_phone_number

    @property
    def caller_extension(self):
        """
        Gets the caller_extension of this CreateCallParams.
        Caller Extension ID

        :return: The caller_extension of this CreateCallParams.
        :rtype: int
        """
        return self._caller_extension

    @caller_extension.setter
    def caller_extension(self, caller_extension):
        """
        Sets the caller_extension of this CreateCallParams.
        Caller Extension ID

        :param caller_extension: The caller_extension of this CreateCallParams.
        :type: int
        """

        self._caller_extension = caller_extension

    @property
    def caller_caller_id(self):
        """
        Gets the caller_caller_id of this CreateCallParams.
        Caller caller ID in E.164 format

        :return: The caller_caller_id of this CreateCallParams.
        :rtype: str
        """
        return self._caller_caller_id

    @caller_caller_id.setter
    def caller_caller_id(self, caller_caller_id):
        """
        Sets the caller_caller_id of this CreateCallParams.
        Caller caller ID in E.164 format

        :param caller_caller_id: The caller_caller_id of this CreateCallParams.
        :type: str
        """

        self._caller_caller_id = caller_caller_id

    @property
    def caller_private(self):
        """
        Gets the caller_private of this CreateCallParams.
        Flag to set caller ID to private

        :return: The caller_private of this CreateCallParams.
        :rtype: bool
        """
        return self._caller_private

    @caller_private.setter
    def caller_private(self, caller_private):
        """
        Sets the caller_private of this CreateCallParams.
        Flag to set caller ID to private

        :param caller_private: The caller_private of this CreateCallParams.
        :type: bool
        """

        self._caller_private = caller_private

    @property
    def callee_phone_number(self):
        """
        Gets the callee_phone_number of this CreateCallParams.
        Callee phone number in E.164 format

        :return: The callee_phone_number of this CreateCallParams.
        :rtype: str
        """
        return self._callee_phone_number

    @callee_phone_number.setter
    def callee_phone_number(self, callee_phone_number):
        """
        Sets the callee_phone_number of this CreateCallParams.
        Callee phone number in E.164 format

        :param callee_phone_number: The callee_phone_number of this CreateCallParams.
        :type: str
        """

        self._callee_phone_number = callee_phone_number

    @property
    def callee_extension(self):
        """
        Gets the callee_extension of this CreateCallParams.
        Callee Extension ID

        :return: The callee_extension of this CreateCallParams.
        :rtype: int
        """
        return self._callee_extension

    @callee_extension.setter
    def callee_extension(self, callee_extension):
        """
        Sets the callee_extension of this CreateCallParams.
        Callee Extension ID

        :param callee_extension: The callee_extension of this CreateCallParams.
        :type: int
        """

        self._callee_extension = callee_extension

    @property
    def callee_caller_id(self):
        """
        Gets the callee_caller_id of this CreateCallParams.
        Callee caller ID in E.164 format

        :return: The callee_caller_id of this CreateCallParams.
        :rtype: str
        """
        return self._callee_caller_id

    @callee_caller_id.setter
    def callee_caller_id(self, callee_caller_id):
        """
        Sets the callee_caller_id of this CreateCallParams.
        Callee caller ID in E.164 format

        :param callee_caller_id: The callee_caller_id of this CreateCallParams.
        :type: str
        """

        self._callee_caller_id = callee_caller_id

    @property
    def callee_private(self):
        """
        Gets the callee_private of this CreateCallParams.
        Flag to set callee ID to private

        :return: The callee_private of this CreateCallParams.
        :rtype: bool
        """
        return self._callee_private

    @callee_private.setter
    def callee_private(self, callee_private):
        """
        Sets the callee_private of this CreateCallParams.
        Flag to set callee ID to private

        :param callee_private: The callee_private of this CreateCallParams.
        :type: bool
        """

        self._callee_private = callee_private

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
        if not isinstance(other, CreateCallParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
