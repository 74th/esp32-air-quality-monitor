import urequests
import ujson

class SimplePostServer:

    def __init__(self, host: str, target: str, auth: str):
        self._host = host
        self._target = target
        self._auth = auth

    def post(self, data: dict):
        header_data = {
            "content-type": "application/json; charset=utf-8",
            "Authorization": self._auth,
        }
        request_url = self._host + "/" + self._target
        post_data = ujson.dumps(data)
        print(request_url)
        res = urequests.post(request_url, headers = header_data, data = post_data)
        text = res.text
