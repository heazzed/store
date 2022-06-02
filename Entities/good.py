class Good:
    name = ""
    quantity = ""
    buyPrice = 0
    salePrice = 0
    type = ""  # text or number? here or somewhere else?
    gender = []  # text or number? here or somewhere else?

    def __init__(self):
        super().__init__()

    def show(self):
        print(self.name, self.quantity, self.buyPrice, self.salePrice, self.type, self.gender)

    def validate(self):
        if not self.quantity.isdigit():
            self.quantity = "0"
            print("Количество должно быть целым числом")
            return False
        else:
            return True


