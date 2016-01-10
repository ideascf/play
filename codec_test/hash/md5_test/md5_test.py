import warnings
warnings.warn("the md5_test module is deprecated; use hashlib instead",
                DeprecationWarning, 2)

import md5


def main():
    m = md5.new()
    m.update('hello')
    m.hexdigest()

if __name__ == '__main__':
    main()