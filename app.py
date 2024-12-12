from flask import Flask, jsonify, request

app = Flask(__name__)

data = {
    "items": []
}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data["items"].append(item)
    return jsonify(item), 201

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id < len(data["items"]):
        return jsonify(data["items"][item_id])
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id < len(data["items"]):
        data["items"][item_id] = request.json
        return jsonify(data["items"][item_id])
    return jsonify({"error": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id < len(data["items"]):
        deleted_item = data["items"].pop(item_id)
        return jsonify(deleted_item)
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
