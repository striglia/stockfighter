import os
import requests
from six.moves.urllib.parse import urljoin


class GM(object):
    base_url = 'https://www.stockfighter.io/gm/'

    def __init__(self, api_key=None):
        self.api_key = os.environ['API_KEY'] if api_key is None else api_key
        self.headers = {'Cookie': 'api_key={api_key}'.format(api_key=self.api_key)}

    def start(self):
        url = urljoin(self.base_url, 'levels/first_steps')
        resp = requests.post(url, headers=self.headers)
        return resp.json()

    def restart(self, instance_id):
        url = urljoin(self.base_url, 'instances/{instance_id}/restart'.format(instance_id))
        resp = requests.post(url, headers=self.headers)
        return resp.json()

    def stop(self, instance_id):
        url = urljoin(self.base_url, 'instances/{instance_id}/stop'.format(instance_id))
        resp = requests.post(url, headers=self.headers)
        return resp.json()

    def resume(self, instance_id):
        url = urljoin(self.base_url, 'instances/{instance_id}'.format(instance_id))
        resp = requests.get(url, headers=self.headers)
        return resp.json()
