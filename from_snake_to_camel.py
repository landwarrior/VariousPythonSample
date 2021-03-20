"""スネークケースからキャメルケースに変換する.

パスカルケースにしてからキャメルケースにしているので、パスカルケースもイケる
"""
words = [
    'test_hoge',
    'camel_case',
]


def main():
    for word in words:
        pascal = ''.join([a[0].upper() + a[1:] for a in word.split('_')])
        camel = pascal[0].lower() + pascal[1:]
        print(camel)


if __name__ == '__main__':
    main()
