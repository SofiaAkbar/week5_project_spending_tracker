from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.merchant import Merchant
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.transaction_repository as transaction_repository

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", merchants=merchants)

# NEW MERCHANT
@merchants_blueprint.route("/merchants/new", methods=['GET'])
def new_merchant():
    tags = tag_repository.select_all()
    transactions = transaction_repository.select_all()
    return render_template("merchants/new.html", tags=tags, transactions=transactions)

