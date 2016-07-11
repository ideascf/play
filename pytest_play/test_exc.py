import pytest

def test_zero_devision():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()

    # excinfo is a ExceptionInfo instance.
    # main attributes: .type, .value, .traceback
    assert excinfo.type is RuntimeError
    assert 'maximum recursion' in str(excinfo.value)

@pytest.mark.xfail(raises=NameError)
def test_mark_xfail():
    print a
