from bot import Bot
import sys


def main():
    bot = Bot()
    bot.load_config()
    bot.login()
    bot.load_subjects()


if __name__ == "__main__":
    main()
