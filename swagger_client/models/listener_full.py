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


class ListenerFull(object):
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
        'voip_id': 'int',
        'type': 'str',
        'event_type': 'str',
        'callbacks': 'list[object]',
        'updated_at': 'int',
        'created_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'voip_id': 'voip_id',
        'type': 'type',
        'event_type': 'event_type',
        'callbacks': 'callbacks',
        'updated_at': 'updated_at',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, voip_id=None, type=None, event_type=None, callbacks=None, updated_at=None, created_at=None):
        """
        ListenerFull - a model defined in Swagger
        """

        self._id = None
        self._voip_id = None
        self._type = None
        self._event_type = None
        self._callbacks = None
        self._updated_at = None
        self._created_at = None

        if id is not None:
          self.id = id
        if voip_id is not None:
          self.voip_id = voip_id
        if type is not None:
          self.type = type
        if event_type is not None:
          self.event_type = event_type
        if callbacks is not None:
          self.callbacks = callbacks
        if updated_at is not None:
          self.updated_at = updated_at
        if created_at is not None:
          self.created_at = created_at

    @property
    def id(self):
        """
        Gets the id of this ListenerFull.
        Integer ID. Read-only.

        :return: The id of this ListenerFull.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ListenerFull.
        Integer ID. Read-only.

        :param id: The id of this ListenerFull.
        :type: int
        """

        self._id = id

    @property
    def voip_id(self):
        """
        Gets the voip_id of this ListenerFull.

        :return: The voip_id of this ListenerFull.
        :rtype: int
        """
        return self._voip_id

    @voip_id.setter
    def voip_id(self, voip_id):
        """
        Sets the voip_id of this ListenerFull.

        :param voip_id: The voip_id of this ListenerFull.
        :type: int
        """

        self._voip_id = voip_id

    @property
    def type(self):
        """
        Gets the type of this ListenerFull.
        Type of listener: callback

        :return: The type of this ListenerFull.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ListenerFull.
        Type of listener: callback

        :param type: The type of this ListenerFull.
        :type: str
        """

        self._type = type

    @property
    def event_type(self):
        """
        Gets the event_type of this ListenerFull.
        Type of event subscribed by the listener: call.new, call.update, call.complete, call.log, sms.in, sms.out

        :return: The event_type of this ListenerFull.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """
        Sets the event_type of this ListenerFull.
        Type of event subscribed by the listener: call.new, call.update, call.complete, call.log, sms.in, sms.out

        :param event_type: The event_type of this ListenerFull.
        :type: str
        """

        self._event_type = event_type

    @property
    def callbacks(self):
        """
        Gets the callbacks of this ListenerFull.
        Array of Callback Object

        :return: The callbacks of this ListenerFull.
        :rtype: list[object]
        """
        return self._callbacks

    @callbacks.setter
    def callbacks(self, callbacks):
        """
        Sets the callbacks of this ListenerFull.
        Array of Callback Object

        :param callbacks: The callbacks of this ListenerFull.
        :type: list[object]
        """

        self._callbacks = callbacks

    @property
    def updated_at(self):
        """
        Gets the updated_at of this ListenerFull.

        :return: The updated_at of this ListenerFull.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this ListenerFull.

        :param updated_at: The updated_at of this ListenerFull.
        :type: int
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """
        Gets the created_at of this ListenerFull.

        :return: The created_at of this ListenerFull.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this ListenerFull.

        :param created_at: The created_at of this ListenerFull.
        :type: int
        """

        self._created_at = created_at

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
        if not isinstance(other, ListenerFull):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
