import httplib
import json

from glusterapi.common import BaseAPI


class EventsApis(BaseAPI):
    def webhook_add(self, url, token, secret):
        """
        Gluster add webhook.

        :param url: (string) url to add webhook
        :param token: (string) token for webhook
        :param secret: (string) secret for webhook
        :raises: GlusterApiError  on failure
        """
        req = {
            "url": url,
            "token": token,
            "secret": secret
        }
        return self._handle_request(self._post, httplib.OK,
                                    "/v1/events/webhook", json.dumps(req))

    def webhook_delete(self, url):
        """
        Gluster delete webhook.

        :param url: (string) url to delete webhook
        :raises: GlusterApiError on failure
        """
        req = {
            "url": url,
        }
        return self._handle_request(self._delete, httplib.NO_CONTENT,
                                    "/v1/events/webhook", json.dumps(req))

    def webhooks(self):
        """
        Gluster list all webhooks.

        :raises: GlusterApiError on failure
        """
        return self._handle_request(self._get, httplib.OK,
                                    "/v1/events/webhook")
