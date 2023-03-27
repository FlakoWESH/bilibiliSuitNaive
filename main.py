import get_emoji
import get_suit

if __name__ == '__main__':
    soe = input("1.suit or 2.emoji?\n")
    if soe == 1:
        while True:
            get_suit.get_suit(eval(input("input id: ").strip()))
    if soe == 2:
        while True:
            get_emoji.get_charge(eval(input("input id: ").strip()))
