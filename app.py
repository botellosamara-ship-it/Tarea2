from flask import Flask, jsonify, request

app = Flask(__name__)

productos = [
    {
        "id": 1,
        "nombre": "Compu",
        "precio": 2500000
    },
    {
        "id": 2,
        "nombre": "Celular",
        "precio": 1200000
    },
    {
        "id": 3,
        "nombre": "Audifonos",
        "precio": 150000
    }
]


@app.route("/")
def inicio():
    return "API de productos funcionando"


# GET - Obtiene todos los productos
@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)


# GET - Obtiene producto por ID
@app.route("/productos/<int:id>", methods=["GET"])
def obtener_producto(id):
    for producto in productos:
        if producto["id"] == id:
            return jsonify(producto)

    return jsonify({"mensaje": "Producto no encontrado"}), 404


# POST - Crea
@app.route("/productos", methods=["POST"])
def crear_producto():
    datos = request.get_json()

    nuevo_producto = {
        "id": max([p["id"] for p in productos], default=0) + 1,
        "nombre": datos["nombre"],
        "precio": datos["precio"]
    }

    productos.append(nuevo_producto)

    return jsonify(nuevo_producto), 201


# PUT - Actualizar producto
@app.route("/productos/<int:id>", methods=["PUT"])
def actualizar_producto(id):
    datos = request.get_json()

    for producto in productos:
        if producto["id"] == id:
            producto["nombre"] = datos["nombre"]
            producto["precio"] = datos["precio"]

            return jsonify(producto)

    return jsonify({"mensaje": "Producto no encontrado"}), 404


# DELETE - Elimina
@app.route("/productos/<int:id>", methods=["DELETE"])
def eliminar_producto(id):
    for producto in productos:
        if producto["id"] == id:
            productos.remove(producto)

            return jsonify({"mensaje": "Producto eliminado correctamente"})

    return jsonify({"mensaje": "Producto no encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)