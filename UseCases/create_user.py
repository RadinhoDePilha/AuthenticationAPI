import json
from flask import Response
from .authentication import is_authenticated


def add_user(request):
    return Response(
        response=json.dumps({
            "text": "Adding User"
        }),
        status=200,
        content_type="application/json"
    )
