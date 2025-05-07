#from bson import ObjectId
from pymongo import MongoClient

from flask import Flask, jsonify, request


app = Flask(__name__)
# Conexão com o banco de dados MongoDB

client = MongoClient('mongodb://localhost:27017/')

db = client['ecommerce']

produtos_collection = db['produtos']

# Rota para adicionar um novo produto (CREATE)
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    
    novo_produto = request.get_json()
    produto_id = produtos_collection.insert_one(novo_produto).inserted_id
    
    return jsonify({"mensagem": "Produto adicionado com sucesso!", "id": str(produto_id)}), 201


if __name__ == '__main__':
    app.run(debug=True)


# Conexão com o MongoDB: a aplicação se conecta ao MongoDB utilizando a biblioteca pymongo. O banco de dados ecommerce é usado para armazenar os produtos.
# Operações CRUD: a aplicação suporta operações CRUD:
# POST /produtos: insere um novo produto no banco;
# GET /produtos: lista todos os produtos ou recupera um produto específico por ID;
# PUT /produtos/{id}: atualiza um produto existente com os dados enviados;
# DELETE /produtos/{id}: remove um produto por ID.
# Documentos em MongoDB: cada produto é armazenado como um documento no formato JSON, permitindo flexibilidade na estrutura dos dados.
# pip install pymongo