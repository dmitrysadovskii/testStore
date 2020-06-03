import requests
import json


class ApiHelper:

    def __init__(self):
        self.header = {"Content-Type": "application/json"}
        self.session = requests.Session()

    def send_request(self, method_type, url, data=None, status_code=200, files=None, header=None):
        if files is None:
            resp = self.session.request(
                method=method_type, url=url, headers=self.header, data=json.dumps(data)
            )
        else:
            resp = self.session.request(
                method=method_type, url=url, files=files
            )

        assert resp.status_code == int(status_code), f"Status code {resp.status_code} != {status_code}. " \
                                                     f"\nError message {resp.content}"
        return json.loads(resp.text)
