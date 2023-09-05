import aiohttp
import asyncio
import requests

from ahrefs_api.configs import Config, DefaultSettingOfRequest


class APIAhrefs:
    def __init__(self, api_token: str, headlines_name: str, target: str, date: str,  **params) -> None:
        config: Config = Config()
        config.change_api_token(api_token)
        self.headers = config.get_headers
        self.api_query = config.set_api_query(headlines_name)
        self.params = DefaultSettingOfRequest(target=target, date=date, **params)

    @property
    def get_response_data(self):
        req = requests.get(self.api_query, params=self.params.__dict__, headers=self.headers)
        return req.json()


def get_ahres_data():
    a_class = APIAhrefs("TEst", headlines_name="Metrics", target="test.com", date="2022-02-02")
    return a_class.get_response_data
