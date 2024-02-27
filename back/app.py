from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 0, "name": "Notebook Acer Swift", "price": 45900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0147295/A0147295_s.jpg"},
    {"id": 1, "name": "Notebook Asus Vivo", "price": 19900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0146010/A0146010_s.jpg"},
    {"id": 2, "name": "Notebook Lenovo Ideapad", "price": 32900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0149009/A0149009_s.jpg"},
    {"id": 3, "name": "Notebook MSI Prestige", "price": 54900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0149954/A0149954_s.jpg"},
    {"id": 4, "name": "Notebook DELL XPS", "price": 99900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0146335/A0146335_s.jpg"},
    {"id": 5, "name": "Notebook HP Envy", "price": 46900, "img": "https://img.advice.co.th/images_nas/pic_product4/A0145712/A0145712_s.jpg"}
]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Get all products
@app.route("/products", methods=["GET"])
def get_all_products():
    return jsonify(products)

# Add a new product
@app.route("/products", methods=["POST"])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify({"message": "Product added successfully"})

# Delete a product
@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    global products
    products = [product for product in products if product['id'] != product_id]
    return jsonify({"message": "Product deleted successfully"})

# Update a product
@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    updated_product = request.json
    for i, product in enumerate(products):
        if product['id'] == product_id:
            products[i] = updated_product
            return jsonify({"message": "Product updated successfully"})
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
