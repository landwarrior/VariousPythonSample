"""ファイル名を変更するスクリプト.

サンプルなのでファイル名は適当に変換します。
"""
import glob
import re
import os

PATH = 'D:\\MyDocuments\\test\\*.txt'


def main():
    for i, filepath in enumerate(glob.glob(PATH)):
        dir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        file_rename = re.sub(r'^.*.txt$', f"hoge{i + 1}.txt", filename)
        os.rename(filepath, f"{dir}/{file_rename}")


if __name__ == '__main__':
    main()
