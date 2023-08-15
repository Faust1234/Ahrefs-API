from ahrefs_api.configs import Config  # Replace 'your_module' with the actual module name


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
