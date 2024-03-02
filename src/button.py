import time

class Tilt:
    x: int
    z: int

class Button:
    def __init__(self, wiiid, ID:int, name:str, value:int=0, holdtime:float=-1):
        self.wiiid = wiiid
        self.ID = ID
        self.name = name
        self.value = value
        self.holdtime = holdtime
        self.holding = False
        self.tilt = Tilt

    def state(self, btnState):
        if (btnState & self.ID):
            if self.value == 0:
                return self.pressed()
        elif self.value == 1:
            return self.released()
        if self.holdtime != -1 and time.time() - self.holdtime > 0.5:
            return self.held()
        return None

    def btap(self):
        if self.wiiid.buttons["b"].value == 1:
            return True
        return False

    def pressed(self):
        self.value = 1
        self.holdtime = time.time()

    def released(self):
        self.value = 0
        self.holdtime = -1
        if not self.holding and self.name != "b":
            if self.btap():
                return ["btap", self.name]
            else:
                return ["tap", self.name]
        else:
            self.holding = False
            return ["release", [self.name]]

    def held(self):
        if self.name != "b":
            self.holdtime = -1
            self.holding = True
            return ["hold", [self.name]]
