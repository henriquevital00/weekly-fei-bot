from bot import Bot
import sys


def main(argv):
    if argv[0] == "run":
        bot = Bot()
        #bot.load_config()
        bot.load_config()
        bot.login()
        bot.load_subjects()
    #elif sys.args[1] == "register":
    #    bot.create_config()
    else:
        print("Choose one option:" "1: Registrer a new account" "2: run")


if __name__ == "__main__":
    main(sys.argv[1:])
