from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.tag import Tag
import repositories.tag_repository as tag_repository
import repositories.merchant_repository as merchant_repository
import repositories.transaction_repository as transaction_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags=tags)

# NEW TAG
@tags_blueprint.route("/tags/new", methods=['GET'])
def new_tag():
    return render_template("tags/new.html")

# CREATE TAG
@tags_blueprint.route("/tags", methods=['POST'])
def create_tag():
    type = request.form['type']
    tag = Tag(type)
    tag_repository.save(tag)
    return redirect('/tags')

# EDIT TAG
@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template('tags/edit.html', tag=tag)

# UPDATE TAG
@tags_blueprint.route("/tags/<id>", methods=["POST"])
def update_tag(id):
    type = request.form["type"]
    tag = Tag(type, id)
    tag_repository.update(tag)
    return redirect("/tags")

# SHOW TAG
@tags_blueprint.route("/tags/<id>")
def show_tag(id):
    tag = tag_repository.select(id)
    return render_template("tags/show.html", tag=tag)

