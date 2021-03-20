"""キャメルケースからスネークケースに変換する."""
import re

words = [
    'testHoge',
    'camelCase',
]


def main():
    for word in words:
        snake = re.sub(r'([A-Z])', r'_\1', word).lower()
        print(snake)


if __name__ == '__main__':
    main()
