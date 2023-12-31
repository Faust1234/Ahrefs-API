from datetime import date

from ahrefs_api.configs import Config, DefaultSettingOfRequest  # Replace 'your_module' with the actual module name


class TestConfig:

    @classmethod
    def setup_class(cls):
        # This method is called before any tests in the TestConfig class are run.
        # You can perform any setup operations here.
        pass

    @classmethod
    def teardown_class(cls):
        # This method is called after all tests in the TestConfig class have been run.
        # You can perform any cleanup operations here.
        pass

    def setup_method(self, method):
        # This method is called before each test method is run.
        # You can perform any setup operations specific to the test here.
        pass

    def teardown_method(self, method):
        # This method is called after each test method has been run.
        # You can perform any cleanup operations specific to the test here.
        pass

    def test_get_headers(self):
        config = Config()
        config.API_TOKEN = 'test_token'
        headers = config.get_headers
        assert headers == {
            "Accept": "application/json, application/xml",
            "Authorization": "Bearer test_token"
        }

    def test_change_api_token(self):
        config = Config()
        config.change_api_token('new_test_token')
        assert config.API_TOKEN == 'new_test_token'

    def test_set_api_query(self):
        config = Config()
        query = config.set_api_query("SERP Overview")
        expected_query = config.default_url + config.default_api_headlines["SERP Overview"]
        assert query == expected_query

    def test_default_values(self):
        default_settings = DefaultSettingOfRequest(target="example.com", date="2023-08-01", date_from="2023-07-01")
        assert default_settings.date_to == date.today()
        assert default_settings.country == "us"
        assert default_settings.output == "json"
        assert default_settings.protocol == "both"
        assert default_settings.mode == "subdomains"
        assert default_settings.volume_mode == "monthly"
        assert default_settings.history_grouping == "monthly"
