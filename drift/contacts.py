from .errors import InvalidFormatError


class Contact(object):
    """
    Contains API routes for querying and manipulating contacts.
    https://devdocs.drift.com/docs/contact-model
    """

    CONTACT_URL_BASE = 'https://driftapi.com/contacts'

    def __init__(self, client):
        self.client = client

    def get(self, contact_id, **kwargs):
        url = "{}/{}".format(self.CONTACT_URL_BASE, contact_id)
        params = {}
        if kwargs:
            params = kwargs
        return self.client.get(url, params=params)

    def create(self, **attributes):
        data = {'attributes': attributes}
        return self.client.post(self.CONTACT_URL_BASE, data=data)

    def add_tags(self, contact_id, tags):
        url = "{}/{}/tags".format(self.CONTACT_URL_BASE, contact_id)
        self._validate_tags(tags)
        return self.client.post(url, data=tags)

    def remove_tag(self, contact_id, tag_name):
        url = "{}/{}/tags/{}".format(self.CONTACT_URL_BASE, contact_id, tag_name)
        return self.client.delete(url)

    def remove_tags_bulk(self, contact_id, tags):
        url = "{}/{}/tags/delete/_bulk".format(self.CONTACT_URL_BASE, contact_id)
        self._validate_tags(tags, False)
        return self.client.post(url, data=tags)

    def update(self, contact_id, **attributes):
        url = "{}/{}".format(self.CONTACT_URL_BASE, contact_id)
        data = {'attributes': attributes}
        return self.client.patch(url, data=data)

    def delete(self, contact_id):
        url = "{}/{}".format(self.CONTACT_URL_BASE, contact_id)
        return self.client.delete(url)

    def _validate_tags(self, tags, require_dict_items=True):
        if not isinstance(tags, list):
            raise InvalidFormatError("Tags must be a list.")

        if require_dict_items:
            for item in tags:
                if not self._is_dict(item):
                    raise InvalidFormatError("%s is not a dictionary. Valid formats is: {'name': 'My Tag'}" % item)

        return tags

    def _is_dict(self, item):
        return isinstance(item, dict)
