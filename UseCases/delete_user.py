import json
from flask import Response
from .authentication import is_authenticated


def del_user(request):
    return Response(
        response=json.dumps({
            "text": "Deleting User"
        }),
        status=200,
        content_type="application/json"
    )
