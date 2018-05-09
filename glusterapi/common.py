import json
from exceptions import GlusterApiError

import requests


class BaseAPI(object):
    def __init__(self, host, https=False, port=24007,
                 username=None, secret=None):
        self.host = host
        self.port = port
        self.scheme = "https" if https else "http"
        self.base_url = "%s://%s:%d" % (self.scheme, self.host, self.port)

    def _get(self, url):
        return requests.get(self.base_url + url)

    def _post(self, url, data):
        return requests.post(self.base_url + url, data=data)

    def _delete(self, url, data):
        return requests.delete(self.base_url + url, data=data)

    def _put(self, url, data):
        return requests.put(self.base_url + url, data=data)

    def _handle_request(self, func, expected_status_code, *args, **kwargs):
        resp = func(*args, **kwargs)
        if resp.status_code != expected_status_code:
            # TODO: Add additional error details
            raise GlusterApiError()

        return json.loads(resp.content)
