# -*- coding: utf-8 -*-
import urlparse
import requests


class Stockfighter(object):
    base_url = 'https://api.stockfighter.io/ob/api'

    def __init__(self, api_key, venue, account):
        self.api_key = api_key
        self.venue = venue
        self.account = account

    def heartbeat(self):
        """Check The API Is Up."""
        url = urlparse.urljoin(self.base_url, '/heartbeat')
        return requests.get(url).json()['ok']
