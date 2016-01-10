import warnings
warnings.warn("the sha module is deprecated; use the hashlib module instead",
                DeprecationWarning, 2)

import sha

def main():
    s = sha.new()
    s.update('hello')
    print(s.hexdigest())

if __name__ == '__main__':
    main()
