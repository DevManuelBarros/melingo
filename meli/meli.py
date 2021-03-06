#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
requeriments:
pip install requests
""" 


from configparser import SafeConfigParser
from .ssl_helper import SSLAdapter
from urllib.parse import urlencode
import json
import os
import re
import requests
import ssl
from .settingsMeli import settingsMeli
class Meli(object):
    def __init__(self, access_token=None, refresh_token=None, charge_data=False):
        self.settings = settingsMeli()
        self.client_id = self.settings.client_id
        self.client_secret = self.settings.client_secret
        if charge_data == False:
            self.access_token = access_token
            self.refresh_token = refresh_token
            self.expires_in = None
        else:
            data_session = self.settings.getDataSession()
            print(data_session[0])
            print(data_session[1])
            self.access_token = data_session[0]
            self.refresh_token = data_session[1]
            self.expires_in = data_session[2]
        
        self.redirect_uri = self.settings.redirect_uri
        self.callbacks = self.settings.callbacks

        parser = SafeConfigParser()
        parser.read(os.path.dirname(os.path.abspath(__file__))+'/config.ini')

        self._requests = requests.Session()
        try:
            self.SSL_VERSION = parser.get('config', 'ssl_version')
            self._requests.mount('https://', SSLAdapter(ssl_version=getattr(ssl, self.SSL_VERSION)))
        except:
            self._requests = requests

        self.API_ROOT_URL = parser.get('config', 'api_root_url')
        self.SDK_VERSION = parser.get('config', 'sdk_version')
        self.AUTH_URL = parser.get('config', 'auth_url')
        self.OAUTH_URL = parser.get('config', 'oauth_url')

    #AUTH METHODS
    def auth_url(self,redirect_URI):
        params = {'client_id':self.client_id,'response_type':'code','redirect_uri': redirect_URI}
        url = self.AUTH_URL  + '/authorization' + '?' + urlencode(params)
        return url

    def auth_url_melingo(self):
        url = self.auth_url(self.redirect_uri)
        return url

    def authorize(self, code, redirect_URI):
        params = { 'grant_type' : 'authorization_code', 'client_id' : self.client_id, 'client_secret' : self.client_secret, 'code' : code, 'redirect_uri' : redirect_URI}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        uri = self.make_path(self.OAUTH_URL)

        response = self._requests.post(uri, params=urlencode(params), headers=headers)
        

        if response.ok:
            response_info = response.json()
            self.access_token = response_info['access_token']
            if 'refresh_token' in response_info:
                self.refresh_token = response_info['refresh_token']
            else:
                self.refresh_token = '' # offline_access not set up
                self.expires_in = response_info['expires_in']

            return response.json()
        else:
            # response code isn't a 200; raise an exception
            response.raise_for_status()

    def authorize_melingo(self, code):
        access_token = self.authorize(code, self.redirect_uri)
        return access_token
        
    # REQUEST METHODS
    def get(self, path, params=None, extra_headers=None):
        params = params or {}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        if extra_headers:
            headers.update(extra_headers)
        uri = self.make_path(path)
        response = self._requests.get(uri, params=urlencode(params), headers=headers)
        return response

    def post(self, path, body=None, params=None, extra_headers=None):
        params = params or {}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        if extra_headers:
            headers.update(extra_headers)
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)

        response = self._requests.post(uri, data=body, params=urlencode(params), headers=headers)
        return response

    def put(self, path, body=None, params=None, extra_headers=None):
        params = params or {}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        if extra_headers:
            headers.update(extra_headers)
        uri = self.make_path(path)
        if body:
            body = json.dumps(body)

        response = self._requests.put(uri, data=body, params=urlencode(params), headers=headers)
        return response

    def delete(self, path, params=None, extra_headers=None):
        params = params or {}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        if extra_headers:
            headers.update(extra_headers)
        uri = self.make_path(path)
        response = self._requests.delete(uri, params=params, headers=headers)
        return response

    def options(self, path, params=None, extra_headers=None):
        params = params or {}
        headers = {'Accept': 'application/json', 'User-Agent':self.SDK_VERSION, 'Content-type':'application/json'}
        if extra_headers:
            headers.update(extra_headers)
        uri = self.make_path(path)
        response = self._requests.options(uri, params=urlencode(params), headers=headers)
        return response

    def make_path(self, path, params=None):
        params = params or {}
        # Making Path and add a leading / if not exist
        if not (re.search("^\/", path)):
            path = "/" + path
        path = self.API_ROOT_URL + path
        if params:
            path = path + "?" + urlencode(params)

        return path