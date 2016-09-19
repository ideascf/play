def foo():
    sum = 0
    for i in range(1000*1000):
        sum += 1

    return sum

if __name__ == '__main__':
    foo()
