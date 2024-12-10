from .errors import QueryFormatError
from .utils import normalize_keys


class Conversation(object):
    """
    Contains API routes for querying and manipulating conversations.
    https://devdocs.drift.com/docs/conversation-overview
    """

    REPORTS_URL = 'https://driftapi.com/reports/conversation-summary'
    ATTACHMENTS_URL = 'https://driftapi.com/attachments/%s/data'
    CONVERSATIONS_BASE_URL = 'https://driftapi.com/conversations'

    def __init__(self, client):
        self.client = client

    def get(self, conversation_id):
        url = "{}/{}".format(self.CONVERSATIONS_BASE_URL, conversation_id)
        params = {'conversationId': conversation_id}
        return self.client.get(url=url, params=params)

    def get_transcript(self, conversation_id):
        url = "{}/{}/transcript".format(self.CONVERSATIONS_BASE_URL, conversation_id)
        params = {'conversationId': conversation_id}
        return self.client.get_transcript(url=url, params=params)

    def list(self, limit=50, page_token=None):
        url = "{}/{}".format(self.CONVERSATIONS_BASE_URL, "list")
        params = {
            'limit': limit,
            'page_token': page_token or ''
        }
        return self.client.get(url=url, params=params)

    def get_metrics(self, query):
        self._validate_query(query)
        return self.client.post(url=self.REPORTS_URL, data=query)

    def get_messages(self, conversation_id, next_=None):
        params = {}
        url = "{}/{}/messages".format(self.CONVERSATIONS_BASE_URL, conversation_id)
        if next_:
            params = {'next': next_}
        return self.client.get(url=url, params=params)

    def create_message(self, conversation_id, org_id, type_, **kwargs):
        url = '{}/{}/messages'.format(self.CONVERSATIONS_BASE_URL, conversation_id)
        data = {'orgId': org_id, 'type': type_}
        if kwargs:
            cleaned_data = self._normalize_message_keys(**kwargs)
            data.update(**cleaned_data)
        return self.client.post(url, data=data)

    def get_attachments(self, doc_id):
        url = self.ATTACHMENTS_URL % doc_id
        return self.client.get(url)

    def _validate_query(self, query):
        if not isinstance(query, dict):
            raise QueryFormatError("Query must be a dictionary.")

        if not query:
            raise QueryFormatError("Query is required.")
        return query

    def _normalize_message_keys(self, **kwargs):
        """
        Converts snake-case to camel-case as required
        by Drift's API.

        Note: Also drops unknown keys.
        """
        allowed_keys = ['edited_message_id', 'edit_type', 'body', 'buttons']
        return normalize_keys(allowed_keys, kwargs)
