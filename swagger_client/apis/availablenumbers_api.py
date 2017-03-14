# coding: utf-8

"""
    Phone.com API

    This is a Phone.com api Swagger definition

    OpenAPI spec version: 1.0.0
    Contact: apisupport@phone.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AvailablenumbersApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def list_available_phone_numbers(self, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_available_phone_numbers(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] filters_phone_number: Phone number filter
        :param list[str] filters_country_code: Country Code filter
        :param list[str] filters_npa: Area Code filter (North America only)
        :param list[str] filters_nxx: 2nd set of 3 digits filter (North America only)
        :param list[str] filters_xxxx: NANP XXXX filter
        :param list[str] filters_city: City filter
        :param list[str] filters_province: State or Province (postal code) filter
        :param list[str] filters_country: Country (postal code) filter
        :param list[str] filters_price: Price filter
        :param list[str] filters_category: Category filter
        :param str sort_internal: Internal (quasi-random) sorting
        :param str sort_price: Price sorting
        :param str sort_phone_number: Phone number sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListAvailableNumbers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_available_phone_numbers_with_http_info(**kwargs)
        else:
            (data) = self.list_available_phone_numbers_with_http_info(**kwargs)
            return data

    def list_available_phone_numbers_with_http_info(self, **kwargs):
        """
        
        
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_available_phone_numbers_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param list[str] filters_phone_number: Phone number filter
        :param list[str] filters_country_code: Country Code filter
        :param list[str] filters_npa: Area Code filter (North America only)
        :param list[str] filters_nxx: 2nd set of 3 digits filter (North America only)
        :param list[str] filters_xxxx: NANP XXXX filter
        :param list[str] filters_city: City filter
        :param list[str] filters_province: State or Province (postal code) filter
        :param list[str] filters_country: Country (postal code) filter
        :param list[str] filters_price: Price filter
        :param list[str] filters_category: Category filter
        :param str sort_internal: Internal (quasi-random) sorting
        :param str sort_price: Price sorting
        :param str sort_phone_number: Phone number sorting
        :param int limit: Max results
        :param int offset: Results to skip
        :param str fields: Field set
        :return: ListAvailableNumbers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filters_phone_number', 'filters_country_code', 'filters_npa', 'filters_nxx', 'filters_xxxx', 'filters_city', 'filters_province', 'filters_country', 'filters_price', 'filters_category', 'sort_internal', 'sort_price', 'sort_phone_number', 'limit', 'offset', 'fields']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_available_phone_numbers" % key
                )
            params[key] = val
        del params['kwargs']

        if 'sort_internal' in params and not re.search('asc|desc', params['sort_internal']):
            raise ValueError("Invalid value for parameter `sort_internal` when calling `list_available_phone_numbers`, must conform to the pattern `/asc|desc/`")
        if 'sort_price' in params and not re.search('asc|desc', params['sort_price']):
            raise ValueError("Invalid value for parameter `sort_price` when calling `list_available_phone_numbers`, must conform to the pattern `/asc|desc/`")
        if 'sort_phone_number' in params and not re.search('asc|desc', params['sort_phone_number']):
            raise ValueError("Invalid value for parameter `sort_phone_number` when calling `list_available_phone_numbers`, must conform to the pattern `/asc|desc/`")

        collection_formats = {}

        resource_path = '/phone-numbers/available'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filters_phone_number' in params:
            query_params['filters[phone_number]'] = params['filters_phone_number']
            collection_formats['filters[phone_number]'] = 'multi'
        if 'filters_country_code' in params:
            query_params['filters[country_code]'] = params['filters_country_code']
            collection_formats['filters[country_code]'] = 'multi'
        if 'filters_npa' in params:
            query_params['filters[npa]'] = params['filters_npa']
            collection_formats['filters[npa]'] = 'multi'
        if 'filters_nxx' in params:
            query_params['filters[nxx]'] = params['filters_nxx']
            collection_formats['filters[nxx]'] = 'multi'
        if 'filters_xxxx' in params:
            query_params['filters[xxxx]'] = params['filters_xxxx']
            collection_formats['filters[xxxx]'] = 'multi'
        if 'filters_city' in params:
            query_params['filters[city]'] = params['filters_city']
            collection_formats['filters[city]'] = 'multi'
        if 'filters_province' in params:
            query_params['filters[province]'] = params['filters_province']
            collection_formats['filters[province]'] = 'multi'
        if 'filters_country' in params:
            query_params['filters[country]'] = params['filters_country']
            collection_formats['filters[country]'] = 'multi'
        if 'filters_price' in params:
            query_params['filters[price]'] = params['filters_price']
            collection_formats['filters[price]'] = 'multi'
        if 'filters_category' in params:
            query_params['filters[category]'] = params['filters_category']
            collection_formats['filters[category]'] = 'multi'
        if 'sort_internal' in params:
            query_params['sort[internal]'] = params['sort_internal']
        if 'sort_price' in params:
            query_params['sort[price]'] = params['sort_price']
        if 'sort_phone_number' in params:
            query_params['sort[phone_number]'] = params['sort_phone_number']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'fields' in params:
            query_params['fields'] = params['fields']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['apiKey']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListAvailableNumbers',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
