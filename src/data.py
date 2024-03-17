class Data:
    def __init__(self) -> None:
        self.file = open("data.txt", "w")
        self.default()
    
    def default(self):
        self.button = ""

    def update(self):
        self.file.write(f"{self.button}\n")
        self.default()
