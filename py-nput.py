from enum import Enum
from time import sleep

from pynput import keyboard

EXE_MODE = "PROD"  # "DEV" or "PROD"
# EXE_MODE = "DEV"  # "DEV" or "PROD"
MARKET_HOTKEY = "<alt>+d"
ABUSE_INTERVAL = 0.03 if EXE_MODE == "PROD" else 1
# 0.02: the max that python310+pynput+vscode can handle
# 0.03: trying, 0.02 will make the game force close after a while

KBC = keyboard.Controller()


class AbusingLevel(Enum):
    IDLE = 0
    WAITING = 1
    ABUSING = 2


abusing_level = AbusingLevel.IDLE


def on_select_market():
    global abusing_level

    if abusing_level == AbusingLevel.IDLE:
        abusing_level = AbusingLevel.WAITING
        sleep(0.5)
        print("waiting for second press")
        if abusing_level != AbusingLevel.ABUSING:
            abusing_level = AbusingLevel.IDLE
            print("not activated")
    abusing_level = AbusingLevel.ABUSING
    if abusing_level:
        print("start abusing")
    else:
        print("stop abusing")


def on_backtick():
    global abusing_level

    print("backtick pressed, force stop abusing")
    abusing_level = AbusingLevel.IDLE


def on_key_p():
    global abusing_level

    print("key_p pressed, force stop abusing")
    abusing_level = AbusingLevel.IDLE


def on_escape():
    print("escape pressed")


if __name__ == "__main__":
    print("Dev mode" if EXE_MODE == "DEV" else "Prod mode")

    h = keyboard.GlobalHotKeys(
        {
            "<esc>": on_escape,
            "`": on_backtick,
            "p": on_key_p,
            MARKET_HOTKEY: on_select_market,
        }
    )
    h.start()
    # h.join()

    counter = 0
    while True:
        if abusing_level == AbusingLevel.ABUSING:
            with KBC.pressed(keyboard.Key.shift):
                for c in "sxdcfv":
                    KBC.tap(c)
            counter += 1
            print(counter)
        sleep(ABUSE_INTERVAL)
