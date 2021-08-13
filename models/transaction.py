class Transaction:
    def __init__(self, date, amount, tag, merchant, id=None):
        self.date = date
        self.amount = amount
        self.tag = tag
        self.merchant = merchant
        self.id = id
