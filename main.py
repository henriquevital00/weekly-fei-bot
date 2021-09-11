from bot import Bot
import sys


def main():
    bot = Bot()
    bot.login()
    bot.load_subjects()


if __name__ == "__main__":
    main()
