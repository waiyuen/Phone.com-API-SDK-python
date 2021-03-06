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


class CreateExtensionParams(object):
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
        'voicemail': 'VoicemailInput',
        'call_notifications': 'CallNotifications',
        'caller_id': 'str',
        'usage_type': 'str',
        'extension': 'int',
        'include_in_directory': 'str',
        'name': 'str',
        'full_name': 'str',
        'timezone': 'str',
        'name_greeting': 'object',
        'local_area_code': 'str',
        'enable_outbound_calls': 'str',
        'enable_call_waiting': 'str'
    }

    attribute_map = {
        'voicemail': 'voicemail',
        'call_notifications': 'call_notifications',
        'caller_id': 'caller_id',
        'usage_type': 'usage_type',
        'extension': 'extension',
        'include_in_directory': 'include_in_directory',
        'name': 'name',
        'full_name': 'full_name',
        'timezone': 'timezone',
        'name_greeting': 'name_greeting',
        'local_area_code': 'local_area_code',
        'enable_outbound_calls': 'enable_outbound_calls',
        'enable_call_waiting': 'enable_call_waiting'
    }

    def __init__(self, voicemail=None, call_notifications=None, caller_id=None, usage_type=None, extension=None, include_in_directory=None, name=None, full_name=None, timezone=None, name_greeting=None, local_area_code=None, enable_outbound_calls=None, enable_call_waiting=None):
        """
        CreateExtensionParams - a model defined in Swagger
        """

        self._voicemail = None
        self._call_notifications = None
        self._caller_id = None
        self._usage_type = None
        self._extension = None
        self._include_in_directory = None
        self._name = None
        self._full_name = None
        self._timezone = None
        self._name_greeting = None
        self._local_area_code = None
        self._enable_outbound_calls = None
        self._enable_call_waiting = None

        if voicemail is not None:
          self.voicemail = voicemail
        if call_notifications is not None:
          self.call_notifications = call_notifications
        if caller_id is not None:
          self.caller_id = caller_id
        if usage_type is not None:
          self.usage_type = usage_type
        if extension is not None:
          self.extension = extension
        if include_in_directory is not None:
          self.include_in_directory = include_in_directory
        if name is not None:
          self.name = name
        if full_name is not None:
          self.full_name = full_name
        if timezone is not None:
          self.timezone = timezone
        if name_greeting is not None:
          self.name_greeting = name_greeting
        if local_area_code is not None:
          self.local_area_code = local_area_code
        if enable_outbound_calls is not None:
          self.enable_outbound_calls = enable_outbound_calls
        if enable_call_waiting is not None:
          self.enable_call_waiting = enable_call_waiting

    @property
    def voicemail(self):
        """
        Gets the voicemail of this CreateExtensionParams.

        :return: The voicemail of this CreateExtensionParams.
        :rtype: VoicemailInput
        """
        return self._voicemail

    @voicemail.setter
    def voicemail(self, voicemail):
        """
        Sets the voicemail of this CreateExtensionParams.

        :param voicemail: The voicemail of this CreateExtensionParams.
        :type: VoicemailInput
        """

        self._voicemail = voicemail

    @property
    def call_notifications(self):
        """
        Gets the call_notifications of this CreateExtensionParams.

        :return: The call_notifications of this CreateExtensionParams.
        :rtype: CallNotifications
        """
        return self._call_notifications

    @call_notifications.setter
    def call_notifications(self, call_notifications):
        """
        Sets the call_notifications of this CreateExtensionParams.

        :param call_notifications: The call_notifications of this CreateExtensionParams.
        :type: CallNotifications
        """

        self._call_notifications = call_notifications

    @property
    def caller_id(self):
        """
        Gets the caller_id of this CreateExtensionParams.
        Caller ID

        :return: The caller_id of this CreateExtensionParams.
        :rtype: str
        """
        return self._caller_id

    @caller_id.setter
    def caller_id(self, caller_id):
        """
        Sets the caller_id of this CreateExtensionParams.
        Caller ID

        :param caller_id: The caller_id of this CreateExtensionParams.
        :type: str
        """

        self._caller_id = caller_id

    @property
    def usage_type(self):
        """
        Gets the usage_type of this CreateExtensionParams.
        Extension type

        :return: The usage_type of this CreateExtensionParams.
        :rtype: str
        """
        return self._usage_type

    @usage_type.setter
    def usage_type(self, usage_type):
        """
        Sets the usage_type of this CreateExtensionParams.
        Extension type

        :param usage_type: The usage_type of this CreateExtensionParams.
        :type: str
        """

        self._usage_type = usage_type

    @property
    def extension(self):
        """
        Gets the extension of this CreateExtensionParams.
        Extension number (auto-generated if empty)

        :return: The extension of this CreateExtensionParams.
        :rtype: int
        """
        return self._extension

    @extension.setter
    def extension(self, extension):
        """
        Sets the extension of this CreateExtensionParams.
        Extension number (auto-generated if empty)

        :param extension: The extension of this CreateExtensionParams.
        :type: int
        """

        self._extension = extension

    @property
    def include_in_directory(self):
        """
        Gets the include_in_directory of this CreateExtensionParams.
        Include in dial-by-name directory

        :return: The include_in_directory of this CreateExtensionParams.
        :rtype: str
        """
        return self._include_in_directory

    @include_in_directory.setter
    def include_in_directory(self, include_in_directory):
        """
        Sets the include_in_directory of this CreateExtensionParams.
        Include in dial-by-name directory

        :param include_in_directory: The include_in_directory of this CreateExtensionParams.
        :type: str
        """

        self._include_in_directory = include_in_directory

    @property
    def name(self):
        """
        Gets the name of this CreateExtensionParams.
        Name (auto-generated if empty)

        :return: The name of this CreateExtensionParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateExtensionParams.
        Name (auto-generated if empty)

        :param name: The name of this CreateExtensionParams.
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """
        Gets the full_name of this CreateExtensionParams.
        Contact name

        :return: The full_name of this CreateExtensionParams.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """
        Sets the full_name of this CreateExtensionParams.
        Contact name

        :param full_name: The full_name of this CreateExtensionParams.
        :type: str
        """

        self._full_name = full_name

    @property
    def timezone(self):
        """
        Gets the timezone of this CreateExtensionParams.
        Timezone

        :return: The timezone of this CreateExtensionParams.
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """
        Sets the timezone of this CreateExtensionParams.
        Timezone

        :param timezone: The timezone of this CreateExtensionParams.
        :type: str
        """

        self._timezone = timezone

    @property
    def name_greeting(self):
        """
        Gets the name_greeting of this CreateExtensionParams.
        Recording lookup object

        :return: The name_greeting of this CreateExtensionParams.
        :rtype: object
        """
        return self._name_greeting

    @name_greeting.setter
    def name_greeting(self, name_greeting):
        """
        Sets the name_greeting of this CreateExtensionParams.
        Recording lookup object

        :param name_greeting: The name_greeting of this CreateExtensionParams.
        :type: object
        """

        self._name_greeting = name_greeting

    @property
    def local_area_code(self):
        """
        Gets the local_area_code of this CreateExtensionParams.
        Local area code

        :return: The local_area_code of this CreateExtensionParams.
        :rtype: str
        """
        return self._local_area_code

    @local_area_code.setter
    def local_area_code(self, local_area_code):
        """
        Sets the local_area_code of this CreateExtensionParams.
        Local area code

        :param local_area_code: The local_area_code of this CreateExtensionParams.
        :type: str
        """

        self._local_area_code = local_area_code

    @property
    def enable_outbound_calls(self):
        """
        Gets the enable_outbound_calls of this CreateExtensionParams.
        Enable outgoing calls

        :return: The enable_outbound_calls of this CreateExtensionParams.
        :rtype: str
        """
        return self._enable_outbound_calls

    @enable_outbound_calls.setter
    def enable_outbound_calls(self, enable_outbound_calls):
        """
        Sets the enable_outbound_calls of this CreateExtensionParams.
        Enable outgoing calls

        :param enable_outbound_calls: The enable_outbound_calls of this CreateExtensionParams.
        :type: str
        """

        self._enable_outbound_calls = enable_outbound_calls

    @property
    def enable_call_waiting(self):
        """
        Gets the enable_call_waiting of this CreateExtensionParams.
        Enable Call Waiting

        :return: The enable_call_waiting of this CreateExtensionParams.
        :rtype: str
        """
        return self._enable_call_waiting

    @enable_call_waiting.setter
    def enable_call_waiting(self, enable_call_waiting):
        """
        Sets the enable_call_waiting of this CreateExtensionParams.
        Enable Call Waiting

        :param enable_call_waiting: The enable_call_waiting of this CreateExtensionParams.
        :type: str
        """

        self._enable_call_waiting = enable_call_waiting

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
        if not isinstance(other, CreateExtensionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
