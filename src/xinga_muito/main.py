from xinga_muito import consumer
from xinga_muito.settings import KEY_WORDS


def main():
    consumer.from_twitter(KEY_WORDS)


if __name__ == '__main__':
    main()
