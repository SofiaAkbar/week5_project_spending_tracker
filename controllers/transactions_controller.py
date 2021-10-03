from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
from models.tag import Tag
from models.transaction import Transaction
import repositories.transaction_repository as transaction_repository
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import pdb

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    return render_template("transactions/index.html", transactions=transactions)

# NEW TRANSACTION
@transactions_blueprint.route("/transactions/new", methods=['GET'])
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants=merchants, tags=tags)

# CREATE MERCHANT
@transactions_blueprint.route("/transactions", methods=['POST'])
def create_transaction():
    amount = request.form['amount']
    date = request.form['date']

    tag_id = request.form['tag']
    tag = tag_repository.select(tag_id)

    merchant_id = request.form['merchant']
    merchant = merchant_repository.select(merchant_id)
    
    transaction = Transaction(amount, date, tag, merchant)
    transaction_repository.save(transaction)
    return redirect('/transactions')