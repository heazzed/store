class Good(object):
    name = ""
    quantity = 0
    buyPrice = 0
    salePrice = 0
    type = ""  # text or number? here or somewhere else?
    modification = ""  # text or number? here or somewhere else?

    def __init__(self):
        super().__init__()

    def show(self):
        print(self.name, self.quantity, self.buyPrice, self.salePrice, self.type, self.modification)
