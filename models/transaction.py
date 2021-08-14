class Transaction:
    def __init__(self, amount, date, tag, merchant, id=None):
        self.amount = amount
        self.date = date
        self.tag = tag
        self.merchant = merchant
        self.id = id
