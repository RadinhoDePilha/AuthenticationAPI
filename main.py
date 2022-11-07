import json
from flask import Flask, Response, request
from UseCases.list_users import list_all_users
from UseCases.delete_user import del_user
from UseCases.update_user import put_users
from UseCases.create_user import add_user

app = Flask(__name__)


@app.route('/ola', methods=['GET', 'POST'])
def ola_route() -> Response:
    """
    Retorna um Olá mundo
    """
    if request.method == 'GET':
        return Response(
            response="Olá Mundo!",
            status="200"
        )

    if request.method == 'POST':
        body = request.json
        if body:
            nome = body['nome']
            return Response(
                response=json.dumps({
                    "text": f"Olá! {nome}",
                }),
                status=200,
                content_type="application/json",
            )

    return Response(
        response="Field 'name' is missing",
        status=400,
        content_type="text"
    )


@app.route('/users', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users_route():
    if request.method == 'GET':
        response = list_all_users(request)

    if request.method == 'POST':
        response = add_user(request)

    if request.method == 'PUT':
        response = put_users(request)

    if request.method == 'DELETE':
        response = del_user(request)

    return response


if __name__ == "__main__":
    app.run(debug=True, port=5000)
