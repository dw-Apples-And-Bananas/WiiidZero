class KeyboardDevice():
    def __init__(self) -> None:
        pass

    def tap(self, mods:list, key:str):
        print(mods, key)

    def hold(self, mods:list, key:str, duration:float):
        print(mods, key, duration)

    def cycle(self, keys:list):
        print(keys)
    
    def type(self, text:str, delay:float):
        print(text, delay)


class MouseDevice():
    def __init__(self) -> None:
        pass

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


kd = KeyboardDevice()
md = MouseDevice()
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
    }
}
