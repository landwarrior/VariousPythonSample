"""Javaのコンストラクタ内の変数初期化だけ作る."""

targets = """\
    /** テスト1 */
    public String test1;
    /** テスト2 */
    public Integer test2;
    /** テスト3 */
    public BigDecimal test3;
"""


def main():
    items = targets.split('\n')
    for item in items:
        if item.strip().startswith('/') or len(item) == 0:
            continue
        item = item.replace('public', '').replace(
            'private', '').replace(';', '').strip()
        argtype = item.split(' ')[0]
        argname = item.split(' ')[1]
        init = '""'
        if argtype in ['Integer', 'int']:
            init = '0'
        elif argtype == 'BigDecimal':
            init = 'BigDecimal.ZERO'
        print(f'this.{argname} = {init};')


if __name__ == '__main__':
    main()
