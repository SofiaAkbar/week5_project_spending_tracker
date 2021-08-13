from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (type) VALUES (%s) RETURNING id"
    values = [tag.type]
    results = run_sql(sql, values)
    id = results[0]['id']
    tag.id = id