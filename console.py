import pdb 

from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository

merchant_1 = Merchant("Tesco")
merchant_repository.save(merchant_1)

merchant_2 = Merchant("Pizza Hut")
merchant_repository.save(merchant_2)







pdb.set_trace()