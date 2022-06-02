class GoodRepository:

    currentSavedGoods = []

    def __init__(self):
        super().__init__()

    def save(self, good):
        self.currentSavedGoods.append(good)

    def show_saved_goods(self):
        for g in self.currentSavedGoods:
            g.show()


