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


class CreateContactParams(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, first_name=None, middle_name=None, last_name=None, prefix=None, phonetic_first_name=None, phonetic_middle_name=None, phonetic_last_name=None, suffix=None, nickname=None, company=None, department=None, job_title=None, emails=None, phone_numbers=None, addresses=None, group=None):
        """
        CreateContactParams - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'first_name': 'str',
            'middle_name': 'str',
            'last_name': 'str',
            'prefix': 'str',
            'phonetic_first_name': 'str',
            'phonetic_middle_name': 'str',
            'phonetic_last_name': 'str',
            'suffix': 'str',
            'nickname': 'str',
            'company': 'str',
            'department': 'str',
            'job_title': 'str',
            'emails': 'list[object]',
            'phone_numbers': 'list[object]',
            'addresses': 'list[object]',
            'group': 'object'
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'middle_name': 'middle_name',
            'last_name': 'last_name',
            'prefix': 'prefix',
            'phonetic_first_name': 'phonetic_first_name',
            'phonetic_middle_name': 'phonetic_middle_name',
            'phonetic_last_name': 'phonetic_last_name',
            'suffix': 'suffix',
            'nickname': 'nickname',
            'company': 'company',
            'department': 'department',
            'job_title': 'job_title',
            'emails': 'emails',
            'phone_numbers': 'phone_numbers',
            'addresses': 'addresses',
            'group': 'group'
        }

        self._first_name = first_name
        self._middle_name = middle_name
        self._last_name = last_name
        self._prefix = prefix
        self._phonetic_first_name = phonetic_first_name
        self._phonetic_middle_name = phonetic_middle_name
        self._phonetic_last_name = phonetic_last_name
        self._suffix = suffix
        self._nickname = nickname
        self._company = company
        self._department = department
        self._job_title = job_title
        self._emails = emails
        self._phone_numbers = phone_numbers
        self._addresses = addresses
        self._group = group

    @property
    def first_name(self):
        """
        Gets the first_name of this CreateContactParams.
        First Name

        :return: The first_name of this CreateContactParams.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this CreateContactParams.
        First Name

        :param first_name: The first_name of this CreateContactParams.
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """
        Gets the middle_name of this CreateContactParams.
        Middle Name

        :return: The middle_name of this CreateContactParams.
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """
        Sets the middle_name of this CreateContactParams.
        Middle Name

        :param middle_name: The middle_name of this CreateContactParams.
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """
        Gets the last_name of this CreateContactParams.
        Last Name

        :return: The last_name of this CreateContactParams.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this CreateContactParams.
        Last Name

        :param last_name: The last_name of this CreateContactParams.
        :type: str
        """

        self._last_name = last_name

    @property
    def prefix(self):
        """
        Gets the prefix of this CreateContactParams.
        Prefix

        :return: The prefix of this CreateContactParams.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CreateContactParams.
        Prefix

        :param prefix: The prefix of this CreateContactParams.
        :type: str
        """

        self._prefix = prefix

    @property
    def phonetic_first_name(self):
        """
        Gets the phonetic_first_name of this CreateContactParams.
        Phonetic First Name

        :return: The phonetic_first_name of this CreateContactParams.
        :rtype: str
        """
        return self._phonetic_first_name

    @phonetic_first_name.setter
    def phonetic_first_name(self, phonetic_first_name):
        """
        Sets the phonetic_first_name of this CreateContactParams.
        Phonetic First Name

        :param phonetic_first_name: The phonetic_first_name of this CreateContactParams.
        :type: str
        """

        self._phonetic_first_name = phonetic_first_name

    @property
    def phonetic_middle_name(self):
        """
        Gets the phonetic_middle_name of this CreateContactParams.
        Phonetic Middle Name

        :return: The phonetic_middle_name of this CreateContactParams.
        :rtype: str
        """
        return self._phonetic_middle_name

    @phonetic_middle_name.setter
    def phonetic_middle_name(self, phonetic_middle_name):
        """
        Sets the phonetic_middle_name of this CreateContactParams.
        Phonetic Middle Name

        :param phonetic_middle_name: The phonetic_middle_name of this CreateContactParams.
        :type: str
        """

        self._phonetic_middle_name = phonetic_middle_name

    @property
    def phonetic_last_name(self):
        """
        Gets the phonetic_last_name of this CreateContactParams.
        Phonetic Last Name

        :return: The phonetic_last_name of this CreateContactParams.
        :rtype: str
        """
        return self._phonetic_last_name

    @phonetic_last_name.setter
    def phonetic_last_name(self, phonetic_last_name):
        """
        Sets the phonetic_last_name of this CreateContactParams.
        Phonetic Last Name

        :param phonetic_last_name: The phonetic_last_name of this CreateContactParams.
        :type: str
        """

        self._phonetic_last_name = phonetic_last_name

    @property
    def suffix(self):
        """
        Gets the suffix of this CreateContactParams.
        Suffix

        :return: The suffix of this CreateContactParams.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this CreateContactParams.
        Suffix

        :param suffix: The suffix of this CreateContactParams.
        :type: str
        """

        self._suffix = suffix

    @property
    def nickname(self):
        """
        Gets the nickname of this CreateContactParams.
        Nickname

        :return: The nickname of this CreateContactParams.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """
        Sets the nickname of this CreateContactParams.
        Nickname

        :param nickname: The nickname of this CreateContactParams.
        :type: str
        """

        self._nickname = nickname

    @property
    def company(self):
        """
        Gets the company of this CreateContactParams.
        Company Name

        :return: The company of this CreateContactParams.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this CreateContactParams.
        Company Name

        :param company: The company of this CreateContactParams.
        :type: str
        """

        self._company = company

    @property
    def department(self):
        """
        Gets the department of this CreateContactParams.
        Department Name

        :return: The department of this CreateContactParams.
        :rtype: str
        """
        return self._department

    @department.setter
    def department(self, department):
        """
        Sets the department of this CreateContactParams.
        Department Name

        :param department: The department of this CreateContactParams.
        :type: str
        """

        self._department = department

    @property
    def job_title(self):
        """
        Gets the job_title of this CreateContactParams.
        Job Title

        :return: The job_title of this CreateContactParams.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this CreateContactParams.
        Job Title

        :param job_title: The job_title of this CreateContactParams.
        :type: str
        """

        self._job_title = job_title

    @property
    def emails(self):
        """
        Gets the emails of this CreateContactParams.
        Email Addresses

        :return: The emails of this CreateContactParams.
        :rtype: list[object]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """
        Sets the emails of this CreateContactParams.
        Email Addresses

        :param emails: The emails of this CreateContactParams.
        :type: list[object]
        """

        self._emails = emails

    @property
    def phone_numbers(self):
        """
        Gets the phone_numbers of this CreateContactParams.
        Phone Numbers

        :return: The phone_numbers of this CreateContactParams.
        :rtype: list[object]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """
        Sets the phone_numbers of this CreateContactParams.
        Phone Numbers

        :param phone_numbers: The phone_numbers of this CreateContactParams.
        :type: list[object]
        """

        self._phone_numbers = phone_numbers

    @property
    def addresses(self):
        """
        Gets the addresses of this CreateContactParams.
        Addresses

        :return: The addresses of this CreateContactParams.
        :rtype: list[object]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this CreateContactParams.
        Addresses

        :param addresses: The addresses of this CreateContactParams.
        :type: list[object]
        """

        self._addresses = addresses

    @property
    def group(self):
        """
        Gets the group of this CreateContactParams.
        Contact Group

        :return: The group of this CreateContactParams.
        :rtype: object
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this CreateContactParams.
        Contact Group

        :param group: The group of this CreateContactParams.
        :type: object
        """

        self._group = group

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
        if not isinstance(other, CreateContactParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
