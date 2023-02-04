from time import sleep

from pynput import keyboard

MARKET_HOTKEY = "<alt>+d"
KBC = keyboard.Controller()

is_abusing = False


def on_select_market():
    global is_abusing

    if not is_abusing:
        sleep(0.5)
    is_abusing = not is_abusing
    if is_abusing:
        print("start abusing")
    else:
        print("stop abusing")


def on_escape():
    print("escape pressed")


if __name__ == "__main__":
    print("Dev mode")

    h = keyboard.GlobalHotKeys(
        {
            "<esc>": on_escape,
            MARKET_HOTKEY: on_select_market,
        }
    )
    h.start()
    # h.join()

    counter = 0
    while True:
        if is_abusing:
            with KBC.pressed(keyboard.Key.shift):
                for c in "sxdcfv":
                    KBC.tap(c)
            counter += 1
            print(counter)
        sleep(0.02)
