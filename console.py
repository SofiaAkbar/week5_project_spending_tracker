import pdb 

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

from models.tag import Tag
import repositories.tag_repository as tag_repository

merchant_repository.delete_all()

merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Pizza Hut")
merchant_repository.save(merchant_2)

tag_1 = Tag("Groceries")
tag_repository.save(tag_1)

tag_2 = Tag("Food")
tag_repository.save(tag_2)



pdb.set_trace()