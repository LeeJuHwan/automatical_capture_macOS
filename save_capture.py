import pynput
import time

keyboard_button = pynput.keyboard.Controller()
keyboard_key = pynput.keyboard.Key


def press_keys(keys):
    keyboard_controller = pynput.keyboard.Controller()
    for key in keys:
        keyboard_controller.press(key)

    time.sleep(0.1)

    for key in keys:
        keyboard_controller.release(key)


def keyboard_con():
    time.sleep(0.2)
    press_keys(
        [
            pynput.keyboard.Key.shift,
            pynput.keyboard.Key.cmd_l,
            pynput.keyboard.KeyCode.from_char("5"),
        ]
    )
    time.sleep(0.2)
    press_keys([pynput.keyboard.Key.enter])
    time.sleep(0.2)
    press_keys([pynput.keyboard.Key.right])


if __name__ == "__main__":
    time.sleep(1)
    for _ in range(274):  # PDF 페이지 개 수
        keyboard_con()
