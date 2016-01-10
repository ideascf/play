import hashlib

def main():
    m = hashlib.md5()
    m.update('xxxxx')
    m.hexdigest()

if __name__ == '__main__':
    main()
