from nose.tools import *

"""
This class stores all the assertions methods
"""
class Assert:
    assert_equal.__self__.maxDiff = None

    @staticmethod
    def assert_equal(first, second, msg=None):
        assert_equal(first, second, msg)


    @staticmethod
    def assert_true(expr, msg=None):
        assert_true(expr, msg)

    @staticmethod
    def assert_false(expr, msg=None):
        assert_false(expr, msg)


