from dataclasses import dataclass
from datetime import date as default_date
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


@dataclass
class DefaultSettingOfRequest:
    """
    Default data for api request to api.ahrefs.com
    """
    target: str  # The target of the search: a domain or a URL.
    date: str  # A date to report metrics on in YYYY-MM-DD format.
    date_from: str  # The start date of the historical period in YYYY-MM-DD format.

    date_to: str = default_date.today()  # The end date of the historical period in YYYY-MM-DD format.
    country: str = "us"  # A two-letter country code.
    output: str = "json"  # The protocol of your target. Allowed values: both, http, https
    protocol: str = "both"  # The output format. Allowed values: json, csv, xml, php
    mode: str = "subdomains"  # The scope of the search based on the target you entered. Allowed values: exact, prefix, domain, subdomains
    volume_mode: str = "monthly"  # The search volume calculation mode: monthly or average. It affects volume, traffic, and traffic value. Allowed values: monthly, average
    history_grouping: str = "monthly"  # The time interval used to group historical data. Allowed values: daily, weekly, monthly
