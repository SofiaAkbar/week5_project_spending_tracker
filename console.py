import pdb 

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository

merchant_repository.delete_all()
tag_repository.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Pizza Hut")
merchant_repository.save(merchant_2)

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Food")
tag_repository.save(tag_2)

transaction_1 = Transaction(5, "01/01/2021", tag_1, merchant_1)
transaction_repository.save(transaction_1)

transaction_2 = Transaction(7.50, "02/02/2021", tag_1, merchant_2)
transaction_repository.save(transaction_2)


pdb.set_trace()