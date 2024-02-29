class KeyboardDevice():
    def press(self, mods:list, key:str):
        print(mods, key)

    def hold(self, mods:list, key:str, duration:float|int):
        print(mods, key, duration)

    def cycle(self, keys:list):
        print(keys)
    
    def type(self, text, delay):
        print(text, delay)


class MouseDevice():
    def click(self, button:str, double:bool):
        print(button, double)

    def hold(self, button:str, duration:bool):
        print(button, duration)

    def move(self, point:tuple, speed:int):
        print(point, speed)
    
    def drag(self, pointA:tuple, pointB:tuple, speed:int):
        print(pointA, pointB, speed)

    def scroll(self, direction:str, amount:int, speed:int):
        print(direction, amount, speed)

run = {
    "keyboard": {
        "press": KeyboardDevice.press,
        "hold": KeyboardDevice.hold,
        "cycle": KeyboardDevice.cycle,
        "type": KeyboardDevice.type
    },
    "mouse": {
        "click": MouseDevice.click,
        "hold": MouseDevice.hold,
        "move": MouseDevice.move,
        "drag": MouseDevice.drag,
        "scroll": MouseDevice.scroll
    }
}
