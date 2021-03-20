"""10分に1回FTPサーバーのファイルを確認して、更新があればコンソールに出力します.

初回起動時はファイルの確認のみ、2回目からの実行で差分を確認するため、
起動する前に変更があった場合は判定できません。
WindowsServer上に構築されたFTPサーバーへのチェックでしか動かないと思います。
"""

import datetime
from ftplib import FTP
import re
import time
import traceback

TARGET_DIR = '/'
ITEM_CACHE = {}
CURRENT = {}
ENCODING = 'sjis'
HOST = ''
PORT = 21
USER = ''
PW = ''
SLEEP_TIME = 10 * 60
dirs = []
first = True


def main():
    global dirs
    dir = []
    with FTP() as ftp:
        ftp.encoding = 'sjis'
        ftp.connect(host=HOST, port=PORT)
        ftp.login(user=USER, passwd=PW)
        ftp.cwd(TARGET_DIR)
        ftp.dir(dir.append)
        for item in dir:
            time, _, dir_name = re.split(' {4,}', item)
            dirs.append(dir_name)
            search_dir(ftp, dirs)


def search_dir(ftp, target_dirs):
    global dirs, ITEM_CACHE, CURRENT
    _dir = []
    path = TARGET_DIR + '/' + '/'.join(target_dirs)
    ftp.cwd(path)
    ftp.dir(_dir.append)
    for item in _dir:
        bunkatsu = re.split(' {4,}', item)
        if len(bunkatsu) == 3:
            time, _, dir_name = bunkatsu
            dirs.append(dir_name)
            search_dir(ftp, dirs)
        else:
            key = '/'.join(dirs) + '/' + ''.join(bunkatsu[1].split(' ')[1:])
            if ITEM_CACHE.get(key, None) is not None and ITEM_CACHE[key] != bunkatsu[0]:
                print(f"ファイルが更新されたようです: {key} ")
            elif first is False and ITEM_CACHE.get(key, None) is None:
                print(f"新しいファイルが追加されました: {key}")
            ITEM_CACHE[key] = bunkatsu[0]
            CURRENT[key] = bunkatsu[0]
    dirs.pop(-1)


if __name__ == '__main__':
    try:
        while True:
            if first:
                print(f"初回準備: {datetime.datetime.now()}")
            else:
                print(f"確認時刻: {datetime.datetime.now()}")
            CURRENT = {}
            main()
            if first is False:
                current_keys = [a for a in CURRENT.keys()]
                cache_keys = [a for a in ITEM_CACHE.keys()]
                if len(cache_keys) > len(current_keys):
                    for key in current_keys:
                        cache_keys.remove(key)
                    print(f"これらのファイルがなくなったようです: {','.join(cache_keys)}")
                    for remove_key in cache_keys:
                        del ITEM_CACHE[remove_key]
            first = False
            time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print('処理終了')
    except Exception:
        print(traceback.format_exc())
