# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class NumberSeriesTypeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def number_series_types_get(self, **kwargs):  # noqa: E501
        """number_series_types_get  # noqa: E501

        Query NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[NumberSeriesType]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.number_series_types_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.number_series_types_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def number_series_types_get_with_http_info(self, **kwargs):  # noqa: E501
        """number_series_types_get  # noqa: E501

        Query NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[NumberSeriesType]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method number_series_types_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/number-series-types', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[NumberSeriesType]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def number_series_types_id_delete(self, id, **kwargs):  # noqa: E501
        """number_series_types_id_delete  # noqa: E501

        Delete NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.number_series_types_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.number_series_types_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def number_series_types_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """number_series_types_id_delete  # noqa: E501

        Delete NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method number_series_types_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `number_series_types_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/number-series-types/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NumberSeriesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def number_series_types_id_get(self, id, **kwargs):  # noqa: E501
        """number_series_types_id_get  # noqa: E501

        Get NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.number_series_types_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.number_series_types_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def number_series_types_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """number_series_types_id_get  # noqa: E501

        Get NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method number_series_types_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `number_series_types_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/number-series-types/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NumberSeriesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def number_series_types_id_put(self, body, id, **kwargs):  # noqa: E501
        """number_series_types_id_put  # noqa: E501

        Update NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_put(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberSeriesType body: (required)
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.number_series_types_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.number_series_types_id_put_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def number_series_types_id_put_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """number_series_types_id_put  # noqa: E501

        Update NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_id_put_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberSeriesType body: (required)
        :param int id: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method number_series_types_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `number_series_types_id_put`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `number_series_types_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/number-series-types/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NumberSeriesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def number_series_types_post(self, body, **kwargs):  # noqa: E501
        """number_series_types_post  # noqa: E501

        Create NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_post(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberSeriesType body: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.number_series_types_post_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.number_series_types_post_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def number_series_types_post_with_http_info(self, body, **kwargs):  # noqa: E501
        """number_series_types_post  # noqa: E501

        Create NumberSeriesType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.number_series_types_post_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberSeriesType body: (required)
        :return: NumberSeriesType
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method number_series_types_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `number_series_types_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/number-series-types', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NumberSeriesType',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
