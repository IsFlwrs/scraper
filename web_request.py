import urllib.request
import urllib.parse
import urllib.error
import json
import sys, os
import my_logging
import my_exceptions

class WebRequest:



    def __init__(self, url):
        self.url = url

    def __get_request(self, request):
        try:
            response = urllib.request.urlopen(request)
            return response
        except Exception as err:
            raise Exception('Error al procesar url', err)

    def __format_params(self, params):
        params = urllib.parse.urlencode(params)
        return params.encode('utf-8')

    def __format_headers(self, headers):
        headers = urllib.parse.urlencode(headers)
        return headers.encode('utf-8')


    def get(self):
        try:
            response = self.__get_request(self.url)
            return response
        except Exception as err:
            print('Error en la peticion get', err)


    def post(self, params = '', headers = ''):

        params = self.__format_params(params)
        headers = self.__format_headers(headers)      
        
        try: 
            req = urllib.request.Request(self.url, params)
            response = self.__get_request(req)
            return response
        except Exception as err:
            print('Error en la peticion POST', err)

    
