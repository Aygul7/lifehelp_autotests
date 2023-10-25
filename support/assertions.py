from support.errors import Errors


class Assertions:
    @staticmethod
    def verify(expected, actual):
        assert expected == actual, Errors.ERROR_EQUAL_ASSERTION.format(expected, actual)

    @staticmethod
    def verify_value(expected_result_value, actual_result_value):
        assert expected_result_value == actual_result_value, Errors.ERROR_EQUAL_ASSERTION.\
            format(actual_result_value, actual_result_value)
