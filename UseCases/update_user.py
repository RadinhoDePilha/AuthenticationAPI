import json
from flask import Response
from .authentication import is_authenticated


def put_users(request):
    return Response(
        response=json.dumps({
            "text": "Updating User"
        }),
        status=200,
        content_type="application/json"
    )
