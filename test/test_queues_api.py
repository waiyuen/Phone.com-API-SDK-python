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
from swagger_client.apis.queues_api import QueuesApi


class TestQueuesApi(unittest.TestCase):
    """ QueuesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.queues_api.QueuesApi()

    def tearDown(self):
        pass

    def test_create_account_queue(self):
        """
        Test case for create_account_queue

        Create a queue
        """
        pass

    def test_delete_account_queue(self):
        """
        Test case for delete_account_queue

        Delete a queue
        """
        pass

    def test_get_account_queue(self):
        """
        Test case for get_account_queue

        Show details of an individual queue
        """
        pass

    def test_list_account_queues(self):
        """
        Test case for list_account_queues

        Get a list of queues for an account
        """
        pass

    def test_replace_account_queue(self):
        """
        Test case for replace_account_queue

        Replace a queue
        """
        pass


if __name__ == '__main__':
    unittest.main()
