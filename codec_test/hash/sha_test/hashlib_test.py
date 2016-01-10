import hashlib

def main():
    s = hashlib.sha1()
    s.update('hello')
    print(s.hexdigest())

if __name__ == '__main__':
    main()
