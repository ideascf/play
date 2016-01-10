def dir_class(cls):
    """
    just print member function
    :param cls:
    :return:
    """
    def _print(name):
        print(name)

    list(
        map(
            lambda name: _print(name),
            filter(
                lambda name: not name.startswith('__'),
                dir(cls)
            )
        )
    )

