# coding=utf8

def f():
    return 3

def test_function():
    assert f() == 4

def test_show_msg():
    assert f() == 2, 'f() should got 3'

def test_set_comparison():
    set1 = set('1308')
    set2 = set('8035')

    # 失败
    # comparing long strings: a context diff is shown
    # comparing long sequences: first failing indices
    # comparing dicts: different entries

    assert set1 == set2


