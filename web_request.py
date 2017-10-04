import urllib.request
import urllib.parse
import urllib.error
import json
import sys, os
import my_logging
import my_exceptions




class WebRequest:
    ''' make http request '''

    # url where make the requests
    url = {}    

    

    # for storage cache
    response = {
        'server'    : '',
        'header'    : '',
        'body'      : ''
    }    

    # for return response content in specific format
    return_response_content_format = True

    # for auto detect and update format (Content Type) of of the response
    auto_detect_format_response = False

    # specific format to process the response
    format_to_response = 'text/plain'

    # storage cache the last response
    __last_response = {}

    # parameters to send in each request
    __request = {
        'headers'   : '',
        'params'    : ''
    }    

    __log = my_logging.Log()

    # obtain the name of this file
    __file = os.path.basename(__file__)



    def __init__(self, url, headers = False, params = False):
        self.url = url

        ''' default config params '''
        self.return_response_content_format = True
        self.auto_detect_format_response = False
        self.format_to_response = 'text/plain'

        if(headers):
            self.set_headers(headers)

        if(params):
            self.set_params(params)

    def __get_request(self):
        ''' Make get request '''
        try:
            self.__last_response = urllib.request.urlopen(self.url)
            self.response['server'] = self.__last_response.__dict__
            self.response['header'] = self.response['server']['headers'].__dict__
            if self.auto_detect_format_response:
                self.format_to_response = self.response['header']['_default_type']

            # logging here
            self.__log.info(self.__file, 'request',self.url, 'url request successfull')
            self.__log.debug(self.url)
            
        except Exception as err:
            #aquí podemos poner Custum error
            print(self.url)
            raise self.__log.critical(sys.exc_info(), 'Error en la url')
            
            
    def __post_request(self):
        ''' make post request '''
        try:
            self.__last_response = urllib.request.Request(self.url, self.__request['params'])
            with urllib.request.urlopen(self.url) as response:
                the_page = response.read()
                print('La página: ')
                print(the_page)

            # logging here
            self.__log.info(self.__file, 'request',self.url, 'url request successfull')
            self.__log.debug(self.url)

        except:
            raise self.__log.critical(sys.exc_info(), 'Error en la url post')

    def __read_from_request(self):
        ''' read content of the last response (cache) '''
        try:
            self.response['body'] = self.__last_response.read()
            print('saja')
            print(self.__last_response.read())
        except:
            raise self.__log.critical(sys.exc_info(), 'No se puede procesar el body response')

    def return_in_format(self):
        ''' process the body response in a valid format '''
        available_formats = {
            'text/json' : self.return_json_format,
            'text/html' : self.return_html_format,
            'text/plain': self.return_text_plain_format,
        }
        try:            
            return available_formats[self.format_to_response]()
        except:
            pass
        
        
    def return_json_format(self):          
        ''' precess the body response in json format '''
        try:
            self.response['body'] = json.loads(self.response['body'])
        except Exception as err:
            raise(sys.exc_info(), 'Error in format to process data')


    
    def return_html_format(self):
        pass

    def return_text_plain_format(self):
        pass


    def set_headers(self, headers):
        ''' set headers to config, accept only a dictionary'''
        if headers.__class__ != dict:
            raise TypeError('set_headers, only accept dictionaries')
        
        self.__request['headers'] = urllib.parse.urlencode(headers).encode('utf-8')
        
    
    def set_params(self, params):
        ''' set params to config, accept only a dictionary '''
        if params.__class__ != dict:
            raise TypeError('set_params, only accept dictionaries')

        #self.__request['params'] = urllib.parse.urlencode(params).encode('utf-8')        
        data = urllib.parse.urlencode(values)
        data = data.encode('ascii') # data should be bytes
        self.__request['params']

    def get(self):
        ''' make a get request '''
        self.__get_request()
        
        try:            
            self.__get_request()
            self.__read_from_request()    
            #if return automaticaly format in request    
            if self.return_response_content_format:
                self.return_in_format()
        
            return self.response['body']
        except Exception as err:
            raise self.__log.critical(sys.exc_info(), 'Ocurrio un al procesar la petición')
        

    def post(self, params):
        params = urllib.parse.urlencode(params)
        params = params.encode('utf-8') # data should be bytes
        req = urllib.request.Request(self.url, params)
        response = urllib.request.urlopen(req)
        return response.read()


    
'''
    how to use:

    >>>
        import web_request
        url = 'http://jsonplaceholder.typicode.com'
        obj = web_request.WebRequest(url)
        obj.get()
        values = {'userId':123}
        obj.url = 'http://jsonplaceholder.typicode.com/posts'
        obj.post(values)
    
'''

