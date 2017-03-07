# coding=utf-8
import itertools


l = [
    {
        'dtm': '2016-12-21 11:11:22',
        'd': 1,
    },
    {
        'dtm': '2016-12-21 22:33:44',
        'd': 1,
    },
    {
        'dtm': '2016-12-24 11:11:22',
        'd': 1,
    },
]


def main():
    g = itertools.groupby(
        l,
        lambda item: item['dtm'].split(' ')[0]
    )

    for dtm, dict_iter in g:
        print dtm
        for item in dict_iter:
            print item
        print


if __name__ == '__main__':
    main()
