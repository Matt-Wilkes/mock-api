from lib.time_error import TimeError
from unittest.mock import Mock

'''
When we call #error
It should return the difference (seconds) between the ext. server and the local machine
'''

def test_error_returns_difference_in_seconds():
    requester_mock = Mock()
    requester_mock.get().json.return_value = {"unixtime":1717966301}
    time_now_mock = Mock()
    time_now_mock.time.return_value = 1717966300.000000
    time_error = TimeError(requester_mock,time_now_mock)
    assert time_error.error() == 1.0
