class Good:

    id = 0
    name = ""
    quantity = 0
    buyPrice = 0
    salePrice = 0
    isAvailable = 0
    type = 0  # text or number? here or somewhere else?
    gender = []  # text or number? here or somewhere else?

    def __init__(self):
        super().__init__()

    def show(self):
        print(self.name, self.quantity, self.buyPrice, self.salePrice, self.type, self.gender)

    def validate(self):  # make in GoodRepos?
        if not self.quantity.isdigit():
            self.quantity = 0
            print("Количество должно быть числом")
            return False
        if not self.buyPrice.isdigit():
            self.buyPrice = 0
            print("Закупочная цена должна быть целым числом")
            return False
        if not self.salePrice.isdigit():
            self.salePrice = 0
            print("Количество должно быть целым числом")
            return False
        else:
            return True


