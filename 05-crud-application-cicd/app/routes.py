from flask import Blueprint, abort, jsonify, request

from .db import get_db

api = Blueprint("api", __name__)


@api.get("/items")
def list_items():
    rows = get_db().execute("SELECT id, name FROM items ORDER BY id")
    return jsonify([dict(row) for row in rows])


@api.post("/items")
def create_item():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        abort(400, "name is required")
    name = name.strip()
    cursor = get_db().execute("INSERT INTO items(name) VALUES (?)", (name,))
    get_db().commit()
    return jsonify({"id": cursor.lastrowid, "name": name}), 201


@api.put("/items/<int:item_id>")
def update_item(item_id):
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not isinstance(name, str) or not name.strip():
        abort(400, "name is required")
    name = name.strip()
    cursor = get_db().execute("UPDATE items SET name=? WHERE id=?", (name, item_id))
    get_db().commit()
    if cursor.rowcount == 0:
        abort(404)
    return jsonify({"id": item_id, "name": name})


@api.delete("/items/<int:item_id>")
def delete_item(item_id):
    cursor = get_db().execute("DELETE FROM items WHERE id=?", (item_id,))
    get_db().commit()
    if cursor.rowcount == 0:
        abort(404)
    return "", 204
