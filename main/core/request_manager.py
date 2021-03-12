"""Module for requests"""
from http import HTTPStatus
import requests
from requests import Session
from main.utils.request_utils import RequestUtils as utils
from main.utils.logger_utils import LoggerUtils as log_util
from main.core.file_reader import FileReader as reader


class RequestsManager:
    """Request Manager basic Implementation"""

    __instance = None

    def __init__(self):
        data = reader.read_basic_data()
        self.basic_url = data['url']
        self.headers = {"Accept": "application/json"}
        # self.session = Session()

    @staticmethod
    def get_instance():
        """This method get a instance of the RequestsManager class.

        Returns:
            RequestManager -- return a instance of RequestsManager class.
        """
        if RequestsManager.__instance is None:
            RequestsManager.__instance = RequestsManager()
        return RequestsManager.__instance

    def do_request(self, http_method, endpoint, body=None, **kwargs):  # pylint: disable=R0913
        """Sends request

        :param http_method: HTTP method
        :type http_method: string
        :param endpoint: Application's endpoint method
        :type endpoint: obj
        """
        logger = log_util.config_logger('basic_logger')
        logger.info('http method: %s', http_method)
        logger.info('endpoint: %s', endpoint)
        if not isinstance(body, dict):
            body = utils.generate_data(body)
        logger.info('body: %s', str(body))
        url = f"{self.basic_url}{endpoint}"
        logger.info('complete URL: %s', url)
        logger.info('send request...')
        if http_method == "GET":
            response = requests.request(str(http_method), url, headers=self.headers)
        else:
            response = requests.request(str(http_method), url, params=body)
        logger.info('response status code: %s', str(response.status_code))
        if response.status_code is not HTTPStatus.OK.value:
            return response.status_code, {"message": response.text}
        logger.info('json response: %s', str(response.json()))
        return response.status_code, response.json()

    # def close_session(self):
    #     """This method close session for RequestsManager class.
    #     """
    #     self.session.close()
