from .errors import InvalidFormatError


class Playbook(object):
    """
    Contains API route for quering playbooks.
    https://devdocs.drift.com/docs/retrieve-conversational-landing-pages
    """

    CLP_URL = 'https://driftapi.com/playbooks/clp'

    def __init__(self, client):
        self.client = client

    def get(self):
        return self.client.get(self.CLP_URL)
