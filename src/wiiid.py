import sys
import cwiid
from zero_hid import Keyboard, Mouse, KeyCodes
import time
import json
import os
from button import Button
from tilt import Tilt
import actions

from strhid import hid

keyboard = Keyboard()
mouse = Mouse()

DIR = os.path.dirname(os.path.abspath(__file__))



class Wiiid:
    def __init__(self) -> None:
        if not self.connect():
            sys.exit()
        print("connected")
        self.rumble()
        self.wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
        self.buttons = {
            "a": Button(self, cwiid.BTN_A, "a"),
            "b": Button(self, cwiid.BTN_B, "b"),
            "up": Button(self, cwiid.BTN_UP, "up"),
            "down": Button(self, cwiid.BTN_DOWN, "down"),
            "left": Button(self, cwiid.BTN_LEFT, "left"),
            "right": Button(self, cwiid.BTN_RIGHT, "right"),
            "plus": Button(self, cwiid.BTN_PLUS, "plus"),
            "minus": Button(self, cwiid.BTN_MINUS, "minus"),
            "home": Button(self, cwiid.BTN_HOME, "home"),
            "1": Button(self, cwiid.BTN_1, "1"),
            "2": Button(self, cwiid.BTN_2, "2")
        }
        self.tilt = Tilt()
        self.data = ["button", "battery"]
        # with open(f"/boot/Wiiid/config.json") as f:
        with open(f"config.json") as f:
            self.config = json.load(f)


    def run(self):
        while True:
            btnState = self.wii.state["buttons"]
            for btn in self.buttons:
                button = self.buttons[btn]
                if button.value == 1:
                    self.data[0] = button.name
                state = button.state(btnState)
                if state != None:
                    self.act(button, *state)
            time.sleep(0)
            self.data[1] = str(self.wii.state["battery"])
            with open("data.txt", "w") as f:
                f.write("\n".join(self.data))


    def act(self, btn, action, args):
        try:
            config = self.config[action][args]
            actions.run[config["device"]][config["action"]](btn, *config["args"])
        except KeyError as e:
            print(e)
        

    def rumble(self, seconds:float=0.3):
        self.wii.rumble = 1
        time.sleep(seconds)
        self.wii.rumble = 0


    def connect(self):
        while True:
            try:
                self.wii = cwiid.Wiimote()
                break
            except RuntimeError:
                pass
        return True


if __name__ == "__main__":
    Wiiid().run()
