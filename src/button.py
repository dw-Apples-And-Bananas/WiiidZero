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

    def holdtap(self):
        for btn in self.wiiid.buttons:
            if self.wiiid.buttons[btn].value == 1:
                return btn
        return None

    def pressed(self):
        if self.name == "home":
            accState = self.wiiid.wii.state["acc"]
            self.tilt.z = accState[0]
            self.tilt.x = accState[1]
        self.value = 1
        self.holdtime = time.time()

    def released(self):
        self.value = 0
        self.holdtime = -1
        if not self.holding:
            heldBtn = self.holdtap()
            if heldBtn != None:
                return ["hold+tap", [heldBtn,self.name]]
            else:
                return ["tap", [self.name]]
        else:
            self.holding = False
            return ["release", [self.name]]

    def held(self):
        self.holdtime = -1
        self.holding = True
        return ["hold", [self.name]]
    
    def tilting(self, acc):
        z = acc[0]
        if z < self.tilt.z-5:
            return ["tilt", ["-z"]]
        elif z > self.tilt.z+5:
            return ["tilt", ["+z"]]
