class GoodRepository:

    currentSavedGoods = []
    goodsFromDb = []

    def __init__(self):
        super().__init__()

    def save(self, good):  # make save to DB
        self.currentSavedGoods.append(good)

    def show_current_saved_goods(self):
        for g in self.currentSavedGoods:
            g.show()

    def get_goods_count(self, db):
        query = self.get_all_goods(db)
        return len(query)

    def get_all_goods(self, db):
        query = "SELECT * FROM goods"
        return db.select_script(query)



