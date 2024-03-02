import time
from zero_hid import Keyboard, Mouse, KeyCodes
from strhid import hid

k = Keyboard()
m = Mouse()

class KeyboardDevice():
    def __init__(self) -> None:
        pass

    def tap(self, btn, mods:list, key:str):
        k.press(mods, hid[key], release=True)

    def hold(self, btn, mods:list, key:str, duration:float):
        k.press(mods, hid[key], release=False)
        time.sleep(duration)
        k.release()

    def cycle(self, btn, keys:list):
        mods, key = keys[btn.cycle]
        k.press(mods, hid[key], release=True)
        btn.cycle += 1
        if btn.cycle == len(keys):
            btn.cycle = 0
    
    def type(self, btn, text:str, delay:float):
        k.type(text, delay)


class MouseDevice():
    def __init__(self) -> None:
        pass

    def click(self, btn, button:str, double:bool):
        print(button, double)

    def hold(self, btn, button:str, duration:bool):
        print(button, duration)

    def move(self, btn, point:tuple, speed:int):
        print(point, speed)
    
    def drag(self, btn, pointA:tuple, pointB:tuple, speed:int):
        print(pointA, pointB, speed)

    def scroll(self, btn, direction:str, amount:int, speed:int):
        print(direction, amount, speed)


class WiiidDevice():
    def __init__(self) -> None:
        pass
    
    def delay(self, btn, duration:float):
        time.sleep(1)

    def macro(self, btn, actions:list):
        for m in actions:
            run[m["device"]][m["action"]](btn,*m["args"])



kd = KeyboardDevice()
md = MouseDevice()
wd = WiiidDevice()
run = {
    "keyboard": {
        "tap": kd.tap,
        "hold": kd.hold,
        "cycle": kd.cycle,
        "type": kd.type
    },
    "mouse": {
        "click": md.click,
        "hold": md.hold,
        "move": md.move,
        "drag": md.drag,
        "scroll": md.scroll
    },
    "wiiid": {
        "delay": wd.delay,
        "macro": wd.macro
    }
}
