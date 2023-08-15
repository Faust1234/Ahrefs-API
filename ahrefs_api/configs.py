from typing import Dict


class Config:
    """
    Default config for request
    """

    API_TOKEN = ''  # default api_token from ahrefs.com, with this not works for gives data from API

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
