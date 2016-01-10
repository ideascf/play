import base64

def main():
    en = base64.b64encode('hello world')

    print(en)
    print(base64.b64decode(en))

if __name__ == '__main__':
    main()
