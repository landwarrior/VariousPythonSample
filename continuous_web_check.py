import datetime
import time
import requests
import sys


def main():
    url = sys.argv[1]
    check_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    test = requests.get(url)
    print(check_time)
    if test:
        print('OK')
    else:
        print('NG')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('please 1 arg: url')
    try:
        while True:
            main()
            time.sleep(600)
    except KeyboardInterrupt:
        print('終了')
