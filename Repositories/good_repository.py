class GoodRepository:

    currentSavedGoods = []
    goodsFromDb = []

    def __init__(self):
        super().__init__()

    def save(self, good, db):  # make save to DB
        self.currentSavedGoods.append(good)
        self.prepare_to_db(good, db)

    def prepare_to_db(self, good, db):
        good.isAvailable = 1
        count_goods = self.get_goods_count(db)
        good.id = count_goods+1
        self.save_to_db(good, db)

    def save_to_db(self, item, db):
        query = "INSERT INTO goods VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}');"\
            .format(item.isAvailable, item.id, item.name, int(item.quantity), int(item.buyPrice), int(item.salePrice),
                    item.type, item.gender)
        res = db.insert_script(query)

    def show_current_saved_goods(self):
        for g in self.currentSavedGoods:
            g.show()

    def get_goods_count(self, db):
        query = self.get_all_goods(db)
        return len(query)

    def get_all_goods(self, db):
        query = "SELECT * FROM goods"
        return db.select_script(query)



