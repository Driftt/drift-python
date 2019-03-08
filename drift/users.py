from .errors import InvalidFormatError


class User(object):
    """
    User API routes for querying and manipulating users.
    https://devdocs.drift.com/docs/user-model
    """

    USER_URL_BASE = 'https://driftapi.com/users'

    def __init__(self, client):
        self.client = client

    def get(self, user_id):
        url = "{}/{}".format(self.USER_URL_BASE, user_id)
        return self.client.get(url)

    def list(self):
        url = "{}/list".format(self.USER_URL_BASE)
        return self.client.get(url)

    def update(self, user_id, **attributes):
        url = "{}/update".format(self.USER_URL_BASE)
        params = {'userId': user_id}
        return self.client.patch(url, data=attributes, params=params)

