import sys


def main(inputMessage):
    if len(inputMessage) >= 5:
        print(get_message(inputMessage))


def get_message(strMessage):
    return strMessage.lower()


if __name__ == "__main__":
    main(sys.argv[1])
