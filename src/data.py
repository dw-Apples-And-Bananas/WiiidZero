class Data:
    def __init__(self) -> None:
        self.file = open("data.txt", "w")
        self.default()
    
    def default(self):
        self.button = ""

    def update(self):
        with open("data.txt", "w") as f:
            f.write(f"{self.button}\n")
        self.default()
