from flask import Blueprint, request, jsonify
from app import db
from app.models.inventory import Inventory

inventory_bp = Blueprint("inventory", __name__, url_prefix="/api/inventory")


# ✅ Get all inventory items
@inventory_bp.route("/", methods=["GET"])
def get_inventory():
    items = Inventory.query.order_by(Inventory.id.desc()).all()
    return jsonify([item.to_dict() for item in items])


# ✅ Add new item
@inventory_bp.route("/", methods=["POST"])
def add_inventory():
    data = request.json

    if not data.get("description") or not data.get("rate"):
        return jsonify({"message": "Missing fields"}), 400

    item = Inventory(
        description=data["description"],
        rate=data["rate"]
    )

    db.session.add(item)
    db.session.commit()

    return jsonify(item.to_dict()), 201


# ✅ Update item
@inventory_bp.route("/<int:item_id>", methods=["PUT"])
def update_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)
    data = request.json

    item.description = data.get("description", item.description)
    item.rate = data.get("rate", item.rate)

    db.session.commit()
    return jsonify(item.to_dict())


# ✅ Delete item
@inventory_bp.route("/<int:item_id>", methods=["DELETE"])
def delete_inventory(item_id):
    item = Inventory.query.get_or_404(item_id)

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Item deleted successfully"})
