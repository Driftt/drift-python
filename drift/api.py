import json
import requests
from .contacts import Contact
from .conversations import Conversation
from .users import User
from . import __version__


SERVER_ERRORS = [500, 502, 503, 504]
DRIFT_ERROR_MESSAGE = "An error occurred while calling Drift. Please try again later."


class Drift(object):
    USER_AGENT = "Drift Python SDK %s" % __version__
    CONTENT_TYPE = 'application/json'
    BEARER_TOKEN_FORMAT = 'Bearer %s'

    def __init__(self, access_token):
        self._token = self.BEARER_TOKEN_FORMAT % access_token
        self._headers = {
            'Authorization': self._token,
            'User-Agent': self.USER_AGENT,
            'Content-Type': self.CONTENT_TYPE
        }
        self.contacts = Contact(self)
        self.conversations = Conversation(self)
        self.users = User(self)

    def post(self, url, data, **kwargs):
        response = requests.post(url, data=json.dumps(data), headers=self._headers, **kwargs)
        return self._parsed_response(response)

    def patch(self, url, data, **kwargs):
        response = requests.patch(url, data=json.dumps(data), headers=self._headers, **kwargs)
        return self._parsed_response(response)

    def get(self, url, **kwargs):
        response = requests.get(url, headers=self._headers, **kwargs)
        return self._parsed_response(response)

    def get_transcript(self, url, **kwargs):
        response = requests.get(url, headers=self._headers, **kwargs)
        return self._parsed_response(response, json_response=False)

    def delete(self, url, **kwargs):
        response = requests.delete(url, headers=self._headers, **kwargs)
        return self._parsed_response(response)

    def _parsed_response(self, response, json_response=True):
        try:
            if response.status_code in SERVER_ERRORS:
                return {'error': DRIFT_ERROR_MESSAGE, 'code': response.status_code}
            elif json_response:
                return response.json()
            return response.content

        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            return {'error': 'Connection Error'}
