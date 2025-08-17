class APIKeyError(Exception):
    error_message = 'Giphy API key is missing , ' \
                    'Please Visit https://developers.giphy.com/dashboard/ ' \
                    'to get a working API key.'

    def __str__(self):
        return self.error_message


class RequiredError(Exception):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'{self.param} is required !!'
