# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.models.recipient import Recipient


class TestRecipient(unittest.TestCase):
    """ Recipient unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRecipient(self):
        """
        Test Recipient
        """
        model = swagger_client.models.recipient.Recipient()


if __name__ == '__main__':
    unittest.main()
