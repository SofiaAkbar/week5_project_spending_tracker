from db.run_sql import run_sql

from models.transaction import Transaction
from models.merchant import Merchant
from models.tag import Tag
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (amount, date, tag_id, merchant_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [transaction.amount, transaction.date, transaction.tag.id, transaction.merchant.id]
    results = run_sql(sql, values)
    transaction.id = results[0]['id']
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions"
    results = run_sql(sql)

    for row in results:
        tag = tag_repository.select(row['tag_id'])
        merchant = merchant_repository.select(row['merchant_id'])
        transaction = Transaction(row['amount'], row['date'], tag, merchant, row['id'])
        transactions.append(transaction)
    return transactions

