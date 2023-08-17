from typing import Dict


class Config:
    """
    Default config for request
    """

    API_TOKEN: str = ""  # default api_token from ahrefs.com, with this not works for gives data from API
    default_url: str = "https://api.ahrefs.com/v3/"  # default url for all  endpoint
    default_api_headlines: Dict[str, str] = {
        "Public": "public/",
        "SERP Overview": "serp-overview/",
        "Keywords Explorer": "keywords-explorer/",
        "Site Explorer": "site-explorer/",
    }

    @property
    def get_headers(self) -> Dict[str, str]:
        """
        :return default headers for request
        """
        return {
            "Accept": "application/json, application/xml",
            "Authorization": f"Bearer {self.API_TOKEN}",
        }

    @classmethod
    def change_api_token(cls, new_api_token: str) -> None:
        """
        change cls.API_TOKEN to the given one
        :param new_api_token: provide api token
        :return: None
        """
        cls.API_TOKEN = new_api_token

    def set_api_query(self, headlines_name: str) -> str:
        """
        Returns the default request for api requests
        :param headlines_name: name headlines API
        :return: api query
        """
        return self.default_url + self.default_api_headlines.get(headlines_name, "")
