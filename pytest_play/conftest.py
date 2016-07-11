# coding=utf8

class Foo():
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

def pytest_assertrepr_compare(op, left, right):
    """
    是一个Hook函数，return explanation for comparisons in failing assert expressions.

    Return None for no custom explanation, otherwise return a list of strings.
    The strings will be joined by newlines but any newlines in a string will be escaped.
    Note that all but the first line will be indented sligthly,
    the intention is for the first line to be a summary.

    get the custom output defined in the conftest file.
    """
    if isinstance(left, Foo) and isinstance(right, Foo) and op == '==':
        return ['Comparing Foo instances:',
                '    vals: %s != %s' % (left.val, right.val)]

def test_foo_equal():
    assert Foo(2) == Foo(1)

